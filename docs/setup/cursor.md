# Connect NyayAssist to Cursor

## One-click install

Open this link on a computer with Cursor installed:

[Add NyayAssist to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=nyayassist&config=eyJ1cmwiOiJodHRwczovL21jcC5ueWF5YXNzaXN0LmFpL21jcCJ9)

Cursor shows the server details; confirm to install.

## Manual configuration

Add the server to `~/.cursor/mcp.json` (all projects) or `.cursor/mcp.json`
(one project):

```json
{
  "mcpServers": {
    "nyayassist": {
      "url": "https://mcp.nyayassist.ai/mcp"
    }
  }
}
```

## Plugin

This repository is also a Cursor plugin (`.cursor-plugin/plugin.json`) that
adds the NyayAssist server and the three skills in `skills/`. Install it from
the Cursor Marketplace once it is listed there.

## Sign in

Open **Cursor Settings → MCP** (or **Tools & MCP**). NyayAssist shows a
**Needs login** or **Connect** button; select it and sign in on the NyayAssist
page that opens. When connected, the server shows a green status and its tools.

See also: [troubleshooting](../troubleshooting.md).
