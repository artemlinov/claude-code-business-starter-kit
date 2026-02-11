#!/usr/bin/env python3
"""
YouTube Outlier Research Tool

Finds videos that massively outperform their channel's average views.
Uses YouTube Data API v3 (free tier: 10,000 quota units/day).

Usage:
    python3 outlier_research.py --query "video editing" --max-channels 10
    python3 outlier_research.py --query "productivity" --months 6 --min-outlier-score 5
"""

import argparse
import json
import os
import sys
import statistics
from datetime import datetime, timezone, timedelta

try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print(json.dumps({
        "error": "Missing dependency. Run: pip install google-api-python-client",
        "type": "missing_dependency"
    }))
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional, user can set env var directly


def get_api_key():
    """Get YouTube Data API key from environment."""
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        # Try loading from .env in common locations
        for path in [".env", "../.env", "../../.env"]:
            if os.path.exists(path):
                with open(path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("YOUTUBE_API_KEY="):
                            key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
            if key:
                break
    return key


def search_channels(youtube, query, max_results=10):
    """Search for channels matching a topic. Costs 100 quota units per call."""
    channels = []
    page_token = None
    remaining = max_results

    while remaining > 0:
        batch_size = min(remaining, 50)
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="channel",
            maxResults=batch_size,
            pageToken=page_token,
            order="relevance"
        )
        response = request.execute()

        for item in response.get("items", []):
            channels.append({
                "id": item["snippet"]["channelId"],
                "title": item["snippet"]["title"],
            })

        page_token = response.get("nextPageToken")
        remaining -= batch_size
        if not page_token:
            break

    return channels


def get_channel_details(youtube, channel_ids):
    """Get channel stats and uploads playlist ID. Costs 1 unit per 50 channels."""
    details = {}
    # Batch in groups of 50
    for i in range(0, len(channel_ids), 50):
        batch = channel_ids[i:i+50]
        request = youtube.channels().list(
            part="statistics,contentDetails,snippet",
            id=",".join(batch)
        )
        response = request.execute()

        for item in response.get("items", []):
            channel_id = item["id"]
            subs = item["statistics"].get("subscriberCount", "0")
            details[channel_id] = {
                "title": item["snippet"]["title"],
                "subscribers": int(subs) if subs != "0" else 0,
                "total_videos": int(item["statistics"].get("videoCount", 0)),
                "uploads_playlist": item["contentDetails"]["relatedPlaylists"]["uploads"],
            }

    return details


def get_recent_videos(youtube, playlist_id, months=12, max_videos=200):
    """Get recent video IDs from uploads playlist. Costs 1 unit per page of 50."""
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=months * 30)
    video_ids = []
    page_token = None

    while len(video_ids) < max_videos:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=page_token
        )
        response = request.execute()

        all_before_cutoff = True
        for item in response.get("items", []):
            published = item["contentDetails"].get("videoPublishedAt", "")
            if published:
                pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                if pub_date >= cutoff_date:
                    video_ids.append(item["contentDetails"]["videoId"])
                    all_before_cutoff = False
                # Videos are in reverse chronological order, so if we hit
                # the cutoff, all subsequent videos are older
            else:
                all_before_cutoff = False

        page_token = response.get("nextPageToken")
        if not page_token or all_before_cutoff:
            break

    return video_ids


def get_video_stats(youtube, video_ids):
    """Get video statistics. Costs 1 unit per page of 50 videos."""
    videos = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        request = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(batch)
        )
        response = request.execute()

        for item in response.get("items", []):
            stats = item["statistics"]
            published = item["snippet"].get("publishedAt", "")
            pub_date = None
            days_ago = None
            if published:
                pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                days_ago = (datetime.now(timezone.utc) - pub_date).days

            videos.append({
                "id": item["id"],
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "channel": item["snippet"]["channelTitle"],
                "channel_id": item["snippet"]["channelId"],
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "comments": int(stats.get("commentCount", 0)),
                "published": pub_date.strftime("%Y-%m-%d") if pub_date else "unknown",
                "days_ago": days_ago,
            })

    return videos


def calculate_outliers(all_videos, min_outlier_score=3.0):
    """Calculate outlier scores: video views / channel median views."""
    # Group videos by channel
    by_channel = {}
    for video in all_videos:
        cid = video["channel_id"]
        if cid not in by_channel:
            by_channel[cid] = []
        by_channel[cid].append(video)

    # Calculate median views per channel
    channel_medians = {}
    for cid, videos in by_channel.items():
        view_counts = [v["views"] for v in videos]
        if len(view_counts) >= 3:  # Need at least 3 videos for meaningful median
            channel_medians[cid] = statistics.median(view_counts)

    # Score each video
    outliers = []
    for video in all_videos:
        cid = video["channel_id"]
        if cid in channel_medians and channel_medians[cid] > 0:
            score = video["views"] / channel_medians[cid]
            if score >= min_outlier_score:
                video["outlier_score"] = round(score, 1)
                video["channel_median_views"] = int(channel_medians[cid])
                outliers.append(video)

    # Sort by outlier score (highest first)
    outliers.sort(key=lambda x: x["outlier_score"], reverse=True)
    return outliers


def main():
    parser = argparse.ArgumentParser(description="YouTube Outlier Research Tool")
    parser.add_argument("--query", required=True, help="Topic/niche to search")
    parser.add_argument("--max-channels", type=int, default=10, help="Max channels to analyze (default: 10)")
    parser.add_argument("--months", type=int, default=12, help="Look at videos from last N months (default: 12)")
    parser.add_argument("--min-subscribers", type=int, default=1000, help="Min subscriber count (default: 1000)")
    parser.add_argument("--min-outlier-score", type=float, default=3.0, help="Min outlier score to include (default: 3.0)")
    parser.add_argument("--max-videos-per-channel", type=int, default=100, help="Max videos to fetch per channel (default: 100)")

    args = parser.parse_args()

    # Get API key
    api_key = get_api_key()
    if not api_key:
        print(json.dumps({
            "error": "YOUTUBE_API_KEY not found. Add it to .env file or set as environment variable.",
            "type": "missing_api_key"
        }))
        sys.exit(1)

    # Build YouTube API client
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
    except Exception as e:
        print(json.dumps({"error": f"Failed to initialize YouTube API: {str(e)}", "type": "api_init_error"}))
        sys.exit(1)

    quota_used = 0

    # Phase 1: Search for channels
    sys.stderr.write(f"Searching for channels matching '{args.query}'...\n")
    try:
        channels = search_channels(youtube, args.query, max_results=args.max_channels)
        quota_used += 100 * ((args.max_channels + 49) // 50)  # 100 units per search page
    except HttpError as e:
        print(json.dumps({"error": f"Search failed: {str(e)}", "type": "search_error"}))
        sys.exit(1)

    if not channels:
        print(json.dumps({"error": f"No channels found for '{args.query}'", "type": "no_results"}))
        sys.exit(1)

    sys.stderr.write(f"Found {len(channels)} channels. Getting details...\n")

    # Phase 2: Get channel details
    channel_ids = [c["id"] for c in channels]
    try:
        channel_details = get_channel_details(youtube, channel_ids)
        quota_used += (len(channel_ids) + 49) // 50  # 1 unit per page of 50
    except HttpError as e:
        print(json.dumps({"error": f"Channel details failed: {str(e)}", "type": "channel_error"}))
        sys.exit(1)

    # Filter by minimum subscribers
    qualified_channels = {
        cid: details for cid, details in channel_details.items()
        if details["subscribers"] >= args.min_subscribers
    }

    sys.stderr.write(f"{len(qualified_channels)} channels meet minimum {args.min_subscribers} subscribers.\n")

    if not qualified_channels:
        print(json.dumps({
            "error": f"No channels with {args.min_subscribers}+ subscribers found for '{args.query}'",
            "type": "no_qualifying_channels"
        }))
        sys.exit(1)

    # Phase 3: Fetch videos for each channel
    all_videos = []
    channels_analyzed = []

    for cid, details in qualified_channels.items():
        sys.stderr.write(f"Analyzing: {details['title']} ({details['subscribers']:,} subs)...\n")

        try:
            video_ids = get_recent_videos(
                youtube, details["uploads_playlist"],
                months=args.months,
                max_videos=args.max_videos_per_channel
            )
            quota_used += (len(video_ids) + 49) // 50 + 1  # playlist + video stats pages

            if video_ids:
                videos = get_video_stats(youtube, video_ids)
                quota_used += (len(video_ids) + 49) // 50
                all_videos.extend(videos)

                channels_analyzed.append({
                    "title": details["title"],
                    "id": cid,
                    "subscribers": details["subscribers"],
                    "videos_analyzed": len(videos),
                })
        except HttpError as e:
            sys.stderr.write(f"  Skipping {details['title']}: {str(e)}\n")
            continue

    sys.stderr.write(f"Scanned {len(all_videos)} total videos. Calculating outliers...\n")

    # Phase 4: Calculate outlier scores
    outliers = calculate_outliers(all_videos, min_outlier_score=args.min_outlier_score)

    # Add channel subscriber count to outliers
    for outlier in outliers:
        cid = outlier["channel_id"]
        if cid in qualified_channels:
            outlier["channel_subscribers"] = qualified_channels[cid]["subscribers"]

    # Build result
    result = {
        "query": args.query,
        "params": {
            "max_channels": args.max_channels,
            "months": args.months,
            "min_subscribers": args.min_subscribers,
            "min_outlier_score": args.min_outlier_score,
        },
        "channels_analyzed": len(channels_analyzed),
        "channels": channels_analyzed,
        "total_videos_scanned": len(all_videos),
        "outlier_count": len(outliers),
        "outliers": outliers,
        "quota_used": quota_used,
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
