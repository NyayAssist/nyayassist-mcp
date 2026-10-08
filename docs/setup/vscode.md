# Connect NyayAssist to VS Code

NyayAssist works with MCP support in VS Code (agent mode in the Chat view).

## Install link

Open on a computer with VS Code installed:

[Install NyayAssist in VS Code](vscode:mcp/install?%7B%22name%22%3A%22nyayassist%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.nyayassist.ai%2Fmcp%22%7D)

## Command line

```bash
code --add-mcp '{"name":"nyayassist","type":"http","url":"https://mcp.nyayassist.ai/mcp"}'
```

## Configuration file

Add the server to `.vscode/mcp.json` in a workspace, or to your user MCP
configuration (Command Palette: **MCP: Open User Configuration**):

```json
{
  "servers": {
    "nyayassist": {
      "type": "http",
      "url": "https://mcp.nyayassist.ai/mcp"
    }
  }
}
```

## Sign in

Start the server from the **MCP: List Servers** command or the CodeLens in
`mcp.json`. VS Code asks to sign in; allow it and sign in on the NyayAssist
page that opens. Then open the Chat view in agent mode and check that the
NyayAssist tools are enabled in the tools picker.

See also: [troubleshooting](../troubleshooting.md).
