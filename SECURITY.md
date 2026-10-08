# Security policy

## Reporting a vulnerability

If you believe you have found a security vulnerability in the NyayAssist MCP
server, the NyayAssist sign-in flow, or the packaging in this repository,
please report it privately to **support@nyayassist.ai** with the subject line
`Security report: MCP connector`.

Please include:

- a description of the issue and its potential impact;
- the steps to reproduce it, including the endpoint, tool name and client
  used;
- any proof-of-concept, with personal data and tokens removed.

Please do not open a public GitHub issue for security problems, and do not
access, modify or delete data that is not your own while investigating.

We will acknowledge your report, keep you informed as we investigate, and let
you know when the issue is resolved. We ask that you give us reasonable time
to fix the issue before any public disclosure.

## Scope

In scope:

- `https://mcp.nyayassist.ai/mcp`
- the OAuth sign-in and token handling used by this endpoint
- the manifests, skills and documentation in this repository

Out of scope:

- vulnerabilities in third-party AI apps or MCP clients (report those to
  their vendors);
- prompt-injection reports that depend on an AI app ignoring the
  `<untrusted_document>` boundary, unless they lead to an action the
  connector is documented not to allow (for example, deleting or sharing
  data);
- denial-of-service and volumetric testing;
- social engineering of NyayAssist staff or users.

## Supported versions

The MCP server is hosted by NyayAssist and always runs the current version.
For this repository, only the latest release is supported.
