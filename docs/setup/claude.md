# Connect NyayAssist to Claude

Works in Claude on the web, the Claude desktop app and the Claude mobile apps.
A connector added on the web or desktop is available on mobile too.

## Add the connector

1. Open **Settings → Connectors**.
2. Choose **Add custom connector**.
3. Enter a name (for example, `NyayAssist`) and the server URL
   `https://mcp.nyayassist.ai/mcp`.
4. Select **Add**, then **Connect**.
5. Sign in on the NyayAssist page that opens, using the same account you use
   on nyayassist.ai, and approve access.

Leave the advanced OAuth client fields empty; Claude registers itself with
NyayAssist automatically.

When NyayAssist appears in the Claude connector directory, you can add it from
there instead of entering the URL.

### Team and Enterprise plans on Claude

On Claude Team and Enterprise plans, an owner first adds the custom connector
under the organisation's connector settings. Each member then opens
**Settings → Connectors**, finds NyayAssist and selects **Connect** to sign in
with their own NyayAssist account. Every member sees only their own NyayAssist
data.

## Use it in a chat

Open the tools menu in the message box and make sure NyayAssist is enabled for
the conversation. Then ask in plain language, for example:

> Search for Bombay High Court judgments since 2020 on the Maharashtra Rent
> Control Act, section 16, and list the five most relevant.

Claude asks for your approval before it uses a tool that creates something,
such as starting research or a draft, depending on your Claude settings.

## Plugin package

This repository is also a Claude plugin (`.claude-plugin/plugin.json`). The
plugin adds the NyayAssist server (`.mcp.json`) and the three skills in
`skills/` together, for Claude apps that install plugins from a marketplace.

## Disconnect

Open **Settings → Connectors**, select NyayAssist and choose **Disconnect** or
remove it. This ends the connector's access; your NyayAssist account and data
are unchanged.

See also: [troubleshooting](../troubleshooting.md).
