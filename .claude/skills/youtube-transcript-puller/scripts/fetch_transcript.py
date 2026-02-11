#!/usr/bin/env python3
"""
Fetch YouTube transcript using youtube-transcript-api.
Usage: python fetch_transcript.py "VIDEO_ID_OR_URL" [--timestamps]
"""

import sys
import re

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("ERROR: youtube-transcript-api not installed.")
    print("Run: pip3 install youtube-transcript-api")
    sys.exit(1)


def extract_video_id(url_or_id: str) -> str:
    """Extract video ID from YouTube URL or return as-is if already an ID."""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]

    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)

    return url_or_id.strip()


def format_timestamp(seconds: float) -> str:
    """Convert seconds to MM:SS or H:MM:SS format."""
    total_seconds = int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"


def fetch_transcript(video_id: str, include_timestamps: bool = False) -> str:
    """Fetch transcript and return as plain text or with timestamps."""
    try:
        # Create API instance and fetch transcript
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=['en', 'en-US', 'en-GB'])

        if include_timestamps:
            # Return with timestamps in [M:SS] format
            lines = []
            for entry in transcript_data:
                timestamp = format_timestamp(entry.start)
                lines.append(f"[{timestamp}] {entry.text}")
            return '\n'.join(lines)
        else:
            # Combine all text segments (original behavior)
            text_parts = [entry.text for entry in transcript_data]
            return ' '.join(text_parts)

    except Exception as e:
        error_msg = str(e).lower()
        if 'disabled' in error_msg:
            return "ERROR: Transcripts are disabled for this video."
        elif 'no transcript' in error_msg or 'not found' in error_msg:
            return "ERROR: No transcript found for this video."
        elif 'unavailable' in error_msg:
            return "ERROR: Video is unavailable (may be private, deleted, or region-locked)."
        else:
            return f"ERROR: {str(e)}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_transcript.py VIDEO_ID_OR_URL [--timestamps]")
        print("Example: python fetch_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("         python fetch_transcript.py dQw4w9WgXcQ --timestamps")
        sys.exit(1)

    video_input = sys.argv[1]
    include_timestamps = '--timestamps' in sys.argv

    video_id = extract_video_id(video_input)
    transcript = fetch_transcript(video_id, include_timestamps)
    print(transcript)


if __name__ == "__main__":
    main()
