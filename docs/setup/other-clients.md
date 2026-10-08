# Connect NyayAssist to other MCP clients

Any client that supports remote MCP servers over Streamable HTTP with OAuth
can use NyayAssist.

## Connection details

| Setting | Value |
|---|---|
| Transport | Streamable HTTP |
| Server URL | `https://mcp.nyayassist.ai/mcp` |
| Authentication | OAuth 2.1 authorisation code flow with PKCE |
| Client registration | Automatic (dynamic client registration or a client ID metadata document); no client ID or secret to enter |
| API key | None |

The server publishes OAuth protected-resource metadata, from which a client
discovers the NyayAssist authorisation server and the supported scopes:

- `https://mcp.nyayassist.ai/.well-known/oauth-protected-resource/mcp`

An unauthenticated request to the server URL returns `401 Unauthorized` with a
`WWW-Authenticate` header pointing at this metadata. That is expected; your
client then starts sign-in.

## Typical configuration

Most clients accept a JSON block like this:

```json
{
  "mcpServers": {
    "nyayassist": {
      "type": "http",
      "url": "https://mcp.nyayassist.ai/mcp"
    }
  }
}
```

Some clients call the URL field `serverUrl` or `httpUrl`, or the type
`streamable-http`. Use whatever your client documents for a remote HTTP
server.

## Clients without remote OAuth support

If your client supports only local (stdio) servers, use a local MCP bridge
that supports OAuth, such as the open-source `mcp-remote` package:

```json
{
  "mcpServers": {
    "nyayassist": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.nyayassist.ai/mcp"]
    }
  }
}
```

`mcp-remote` is a third-party project and is not maintained by NyayAssist.

## Scopes

The client requests the scopes it needs during sign-in. Each tool requires one
of these scopes:

| Scope | Tools |
|---|---|
| `library:read` | Legal Library search and fetch |
| `cases:read` / `cases:write` | Reading matters and documents / creating matters, adding and uploading documents |
| `research` | Research |
| `draft` | Drafting |
| `translate` | Translation |
| `docproc` | Document tools (OCR) |
| `dd` | Due diligence |
| `workflows` | Workflows |
| `meetings:read` / `meetings:write` | Reading meetings / notetaker and recordings |
| `offline_access` | Staying signed in between sessions |

Account and job tools need only a valid sign-in.

See also: [troubleshooting](../troubleshooting.md).
