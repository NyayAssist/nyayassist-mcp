# Connect NyayAssist to ChatGPT

ChatGPT connects to remote MCP servers as custom connectors (apps). Adding
your own connector needs developer mode, which is available on eligible ChatGPT
plans. Menu names change between ChatGPT releases; if a label below differs,
look for the equivalent under **Settings → Apps & Connectors**.

## Add the connector

1. Open **Settings → Apps & Connectors → Advanced settings** and turn on
   **Developer mode**.
2. Back in **Apps & Connectors**, choose **Create** (or **Add connector**).
3. Fill in:
   - **Name:** `NyayAssist`
   - **Description:** `Indian legal research, drafting and matters`
   - **MCP server URL:** `https://mcp.nyayassist.ai/mcp`
   - **Authentication:** OAuth
4. Confirm that you trust the application and select **Create**.
5. Sign in on the NyayAssist page that opens and approve access.

On ChatGPT Business, Enterprise and Edu workspaces, an admin may need to allow
custom connectors before members can add or use them.

## Use it in a chat

Start a new chat, open the **+** menu, choose the developer mode or connector
option and select NyayAssist. Then ask, for example:

> Using NyayAssist, list my matters and summarise the documents in the most
> recent one.

ChatGPT shows a confirmation before calling tools that create something.
Review it before approving.

## Disconnect

Open **Settings → Apps & Connectors**, select NyayAssist and disconnect or
delete it. Your NyayAssist account and data are unchanged.

See also: [troubleshooting](../troubleshooting.md).
