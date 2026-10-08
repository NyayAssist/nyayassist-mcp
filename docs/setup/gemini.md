# Connect NyayAssist to Gemini CLI

This repository is a Gemini CLI extension. It adds the NyayAssist server, a
short context file (`GEMINI.md`) and the three skills in `skills/`.

## Install the extension

```bash
gemini extensions install https://github.com/NyayAssist/nyayassist-mcp
```

Restart Gemini CLI. The first time a NyayAssist tool is needed, Gemini CLI
detects that the server requires sign-in and opens the NyayAssist sign-in page
in your browser. You can also start sign-in yourself:

```text
/mcp auth nyayassist
```

Check the connection with `/mcp list`; NyayAssist should show as connected
with its tools.

Update or remove the extension with:

```bash
gemini extensions update nyayassist
gemini extensions uninstall nyayassist
```

## Manual configuration

To add the server without the extension, add it to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "nyayassist": {
      "httpUrl": "https://mcp.nyayassist.ai/mcp"
    }
  }
}
```

## Gemini in other Google apps

Gemini apps that accept a remote MCP server URL with OAuth can use the same
endpoint. Follow that app's instructions for adding an MCP server.

See also: [troubleshooting](../troubleshooting.md).
