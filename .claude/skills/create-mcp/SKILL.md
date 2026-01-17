---
name: create-mcp
description: Add, configure, or build MCP servers in Claude Code. USE WHEN user says 'add an MCP', 'connect to', 'add integration', 'setup MCP', 'connect MCP server', 'add notion', 'add youtube', 'configure MCP', 'build an MCP', 'create MCP server'.
---

# Create MCP

Teaches Claude how to add existing MCP servers OR build custom ones from scratch.

---

## Two Paths

| Path | When to Use | Complexity |
|------|-------------|------------|
| **Connect Existing** | Using a published MCP (YouTube, Notion, GitHub) | Easy (5 min) |
| **Build Custom** | Creating your own MCP server for a custom API | Medium (1-2 hours) |

Ask the user: **"Are you connecting to an existing MCP or building a custom one?"**

---

# PATH 1: Connect Existing MCP

## The 3-Phase Process

### Phase 1: IDENTIFY
Ask the user:
- "What service do you want to connect to?" (YouTube, Notion, GitHub, etc.)
- "Do you already have an API key or need to create one?"

### Phase 2: SCOPE
Ask the user:
- "Should this be available in all your projects, or just this one?"
  - **User scope** → Available everywhere (personal tools)
  - **Project scope** → Only this project, shared with team via git
  - **Local scope** → Only this project, private to you

### Phase 3: CONFIGURE
- Add the MCP server using CLI or .mcp.json
- Set up environment variables for secrets
- Test the connection

---

## Adding Existing MCP Servers

### Method 1: CLI (Recommended)

```bash
# HTTP transport (remote servers)
claude mcp add --transport http <name> <url>

# Stdio transport (local/npm packages)
claude mcp add --transport stdio <name> -- <command> [args...]

# With environment variables
claude mcp add --transport stdio <name> --env API_KEY=value -- npx -y @package/name

# With scope
claude mcp add --scope project --transport http notion https://mcp.notion.com/mcp
```

**Important:** All options (`--transport`, `--env`, `--scope`) must come BEFORE the server name.

### Method 2: Edit .mcp.json

Create or edit `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@package/mcp-server"],
      "env": {
        "API_KEY": "${API_KEY}"
      }
    }
  }
}
```

---

## .mcp.json Structure

```json
{
  "mcpServers": {
    "server-name": {
      "type": "http|sse|stdio",
      "url": "https://...",
      "command": "node|npx|python|uv",
      "args": ["arg1", "arg2"],
      "env": {
        "VAR_NAME": "${ENV_VAR}"
      },
      "headers": {
        "Authorization": "Bearer ${TOKEN}"
      }
    }
  }
}
```

### Supported Fields

| Field | Type | Required | Transport | Purpose |
|-------|------|----------|-----------|---------|
| `type` | string | Yes | All | `http`, `sse`, or `stdio` |
| `url` | string | Yes* | HTTP/SSE | Remote server endpoint |
| `command` | string | Yes* | Stdio | Executable to run |
| `args` | array | No | Stdio | Command-line arguments |
| `env` | object | No | Stdio | Environment variables |
| `headers` | object | No | HTTP/SSE | HTTP headers (auth, etc.) |

---

## Transport Types

### HTTP (Remote Servers)
For cloud-hosted MCP servers:

```json
{
  "notion": {
    "type": "http",
    "url": "https://mcp.notion.com/mcp",
    "headers": {
      "Authorization": "Bearer ${NOTION_TOKEN}"
    }
  }
}
```

### Stdio (Local/NPM Packages)
For npm packages or local scripts:

```json
{
  "youtube": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/youtube-mcp"],
    "env": {
      "YOUTUBE_API_KEY": "${YOUTUBE_API_KEY}"
    }
  }
}
```

**Windows Note:** NPX requires cmd wrapper:
```json
{
  "notion": {
    "command": "cmd",
    "args": ["/c", "npx", "-y", "@notionhq/notion-mcp-server"],
    "env": {
      "NOTION_TOKEN": "${NOTION_TOKEN}"
    }
  }
}
```

---

## Common MCP Servers

### YouTube
```json
{
  "youtube": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@anthropic/youtube-mcp"],
    "env": { "YOUTUBE_API_KEY": "${YOUTUBE_API_KEY}" }
  }
}
```

### Notion
```json
{
  "notion": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@notionhq/notion-mcp-server"],
    "env": { "NOTION_TOKEN": "${NOTION_TOKEN}" }
  }
}
```

### GitHub
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

### Filesystem
```bash
claude mcp add --transport stdio files -- npx -y @modelcontextprotocol/server-filesystem /path/to/dir
```

---

## Scopes

| Scope | Storage | Visibility | Use Case |
|-------|---------|------------|----------|
| **user** | `~/.claude.json` | All your projects | Personal tools |
| **project** | `.mcp.json` (git) | Team via version control | Shared team tools |
| **local** | `~/.claude.json` (project path) | Only you, this project | Private/sensitive |

**Precedence:** Local > Project > User

---

## Environment Variables & API Keys

### Never Hardcode Secrets!

```json
// BAD - secrets exposed in git
"env": { "API_KEY": "sk-abc123..." }

// GOOD - uses environment variable
"env": { "API_KEY": "${API_KEY}" }
```

### Secure API Key Storage (Recommended)

Store API keys in a `.env` file that's git-ignored. Use `dotenv-cli` to load them automatically.

**Step 1: Create .env file**
```
YOUTUBE_API_KEY=your_youtube_api_key_here
NOTION_API_KEY=your_notion_integration_token_here
```

**Step 2: Ensure .gitignore includes .env**
```
# Add to .gitignore
.env
```

**Step 3: Configure .mcp.json to use dotenv-cli**

Use `dotenv-cli` to load `.env` before running the MCP server:

```json
{
  "mcpServers": {
    "youtube": {
      "command": "npx",
      "args": ["-y", "dotenv-cli", "-e", ".env", "--", "npx", "-y", "@anthropic/youtube-mcp"],
      "env": {}
    }
  }
}
```

This pattern:
1. Runs `dotenv-cli` which loads `.env` into the environment
2. Then runs the actual MCP server with those env vars available
3. No system environment variables needed!

### Quick Setup Flow

When user provides an API key:

1. **Check if .env exists** - Create if not
2. **Add key to .env** - Append the key
3. **Check .gitignore** - Ensure .env is ignored
4. **Update .mcp.json** - Use dotenv-cli wrapper pattern
5. **Tell user to reload** - Restart VS Code or reload window

Example interaction:
```
User: "Here's my YouTube API key: AIzaSy..."

Claude:
1. Creates/updates .env with YOUTUBE_API_KEY=AIzaSy...
2. Verifies .gitignore has .env
3. Updates .mcp.json to use dotenv-cli wrapper
4. Says: "Done! Reload VS Code window (Ctrl+Shift+P → Reload Window)
   to connect the YouTube MCP."
```

### Where to Get API Keys

| Service | Where to Get Key |
|---------|------------------|
| YouTube | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) → Create credentials → API Key → Enable YouTube Data API v3 |
| Notion | [Notion Integrations](https://www.notion.so/my-integrations) → New integration → Copy token |
| GitHub | [GitHub Settings](https://github.com/settings/tokens) → Personal access tokens |

---

# PATH 2: Build Custom MCP Server

## When to Build Custom

- API doesn't have an existing MCP server
- You need specific tools for your business
- You want to wrap internal services

---

## The 4-Phase Process

### Phase 1: DEFINE
Ask the user:
- "What API or service do you want to connect?"
- "What tools should Claude have access to?" (e.g., search, create, update)

### Phase 2: SETUP
Choose language and create project structure

### Phase 3: BUILD
Implement the MCP server with tools

### Phase 4: CONNECT
Add to .mcp.json and test

---

## Quick Start: Python (Recommended)

### Setup

```bash
# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project
uv init my-mcp-server
cd my-mcp-server
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install MCP SDK
uv add "mcp[cli]" httpx
```

### Minimal Server (server.py)

```python
from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("my-server")

@mcp.tool()
async def my_tool(param: str) -> str:
    """Description of what this tool does.

    Args:
        param: Description of this parameter
    """
    # Your implementation here
    return f"Result for {param}"

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
```

### Run

```bash
uv run server.py
```

---

## Quick Start: TypeScript

### Setup

```bash
mkdir my-mcp-server
cd my-mcp-server
npm init -y
npm install @modelcontextprotocol/sdk zod
npm install -D typescript @types/node

mkdir src
```

### package.json

```json
{
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
```

### Minimal Server (src/index.ts)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
});

// Register a tool
server.registerTool(
  "my_tool",
  {
    description: "Description of what this tool does",
    inputSchema: {
      type: "object",
      properties: {
        param: {
          type: "string",
          description: "Description of this parameter"
        }
      },
      required: ["param"]
    }
  },
  async ({ param }) => {
    // Your implementation here
    return {
      content: [{
        type: "text",
        text: `Result for ${param}`
      }]
    };
  }
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Server running on stdio");
}

main().catch(console.error);
```

### Build and Run

```bash
npm run build
npm start
```

---

## Adding Tools

Tools are functions Claude can call. Each tool needs:
- **Name**: What Claude uses to call it
- **Description**: Helps Claude know when to use it
- **Parameters**: What inputs it accepts
- **Implementation**: What it actually does

### Python Example

```python
@mcp.tool()
async def search_products(query: str, limit: int = 10) -> str:
    """Search for products in the catalog.

    Args:
        query: Search terms
        limit: Maximum results to return (default 10)
    """
    # Call your API
    results = await api.search(query, limit)
    return json.dumps(results)

@mcp.tool()
async def get_order(order_id: str) -> str:
    """Get details for a specific order.

    Args:
        order_id: The order ID to look up
    """
    order = await api.get_order(order_id)
    return json.dumps(order)
```

### TypeScript Example

```typescript
server.registerTool(
  "search_products",
  {
    description: "Search for products in the catalog",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Search terms" },
        limit: { type: "number", description: "Max results", default: 10 }
      },
      required: ["query"]
    }
  },
  async ({ query, limit = 10 }) => {
    const results = await api.search(query, limit);
    return {
      content: [{ type: "text", text: JSON.stringify(results) }]
    };
  }
);
```

---

## Connect Custom MCP to Claude Code

### Add to .mcp.json

**Python:**
```json
{
  "mcpServers": {
    "my-server": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/absolute/path/to/my-mcp-server", "run", "server.py"],
      "env": {
        "API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

**TypeScript:**
```json
{
  "mcpServers": {
    "my-server": {
      "type": "stdio",
      "command": "node",
      "args": ["/absolute/path/to/my-mcp-server/dist/index.js"],
      "env": {
        "API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

**Important:** Use ABSOLUTE paths, not relative.

---

## Critical: Logging Rules

**For stdio servers, NEVER write to stdout!**

```python
# BAD - breaks JSON-RPC
print("Processing...")

# GOOD - use stderr or logging
import logging
logging.info("Processing...")
```

```typescript
// BAD
console.log("Started");

// GOOD
console.error("Started");  // stderr is safe
```

---

## Testing Your MCP

1. Run `claude mcp list` - verify server shows as connected
2. Ask Claude to use a tool: "Search for products about X"
3. Check logs if issues:
   ```bash
   # Mac
   tail -f ~/Library/Logs/Claude/mcp*.log
   ```

---

## MCP Server Structure Summary

```
my-mcp-server/
├── server.py          # Main server (Python)
├── src/
│   └── index.ts       # Main server (TypeScript)
├── package.json       # (TypeScript)
├── pyproject.toml     # (Python)
└── README.md          # How to use
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Server not connected | Invalid path | Use absolute paths |
| No tools available | Server crashed | Check stderr/logs |
| Tool returns error | Implementation bug | Debug your code |
| ${VAR} not expanding | Env var not set | Set before running Claude |

---

## Creation Checklist

### Connecting Existing MCP:
- [ ] Correct transport type (http vs stdio)
- [ ] Environment variables use `${VAR}` syntax
- [ ] Secrets NOT hardcoded
- [ ] Windows: npx uses `cmd /c` wrapper
- [ ] Tested with `claude mcp list`

### Building Custom MCP:
- [ ] Tools have clear descriptions
- [ ] Parameters documented
- [ ] No stdout writes (stdio transport)
- [ ] Absolute paths in .mcp.json
- [ ] Error handling implemented
- [ ] Tested each tool

---

**Connecting:** `.mcp.json` + `claude mcp add`
**Building:** Python (`mcp[cli]`) or TypeScript (`@modelcontextprotocol/sdk`)
**Testing:** `claude mcp list` + try tools in chat
