# Security and privacy

This page explains how the NyayAssist MCP connector handles your account and
data. The NyayAssist [Privacy Policy](https://nyayassist.ai/privacy) and
[Terms of Use](https://nyayassist.ai/terms) apply to all use of the connector
and take precedence over this summary.

## How a request flows

1. Your AI app (the client) connects to `https://mcp.nyayassist.ai/mcp` over
   HTTPS.
2. The server answers `401` and points the client at its OAuth metadata. The
   client opens the NyayAssist sign-in page, where you sign in with your
   NyayAssist account and approve access.
3. Sign-in uses OAuth 2.1 with PKCE. The client receives an access token
   issued for the NyayAssist MCP server only, plus a refresh token so you stay
   signed in.
4. For each tool call, the server checks the token and the scope the tool
   needs, then exchanges your token on the server side for access to your own
   NyayAssist account. Your app never sees NyayAssist backend credentials, and
   no NyayAssist password or API key is stored in your app.
5. The result is shaped to a fixed, documented set of fields before it is
   returned. Internal identifiers are replaced with opaque handles.

## What the connector can access

- Only what your own NyayAssist account can access: your matters, documents,
  drafts, research, translations, due-diligence projects, workflows and
  meetings, plus the shared Legal Library of judgments and Acts.
- Access is limited by OAuth scopes (for example `cases:read`, `draft`, `dd`).
  A tool refuses a call if your token lacks its scope. The full list is in
  [setup/other-clients.md](setup/other-clients.md#scopes).
- Your plan's limits apply exactly as in the web app. A locked matter stays
  locked.

## What the connector cannot do

- **No delete, overwrite, share or send.** There are no tools to delete
  anything, share or invite, send email, route for e-signature, or change
  billing or settings. Revising a draft always creates a new version.
- **One outward-facing action.** `start_meeting` sends a NyayAssist notetaker
  into the Google Meet or Microsoft Teams call you give it. It joins as a
  visible participant and records. Use it only for calls you are entitled to
  record.
- **Links you give.** `upload_documents`, `upload_meeting_recording` and
  `add_document_to_case` download a file from a link only when you supply
  one.
- **Workflow safety.** Workflows that send email, route for e-signature or
  file outside NyayAssist are not offered through the connector. At a review
  step, the connector can only reject or cancel; approval is given in the web
  app.

## Untrusted content

Judgments, Acts and your own documents can contain text that looks like an
instruction. The server returns such content inside `<untrusted_document>`
tags and tells the assistant that it is data and must not be followed. The
bundled skills repeat this. Even so, review what your assistant proposes
before approving tool calls that create work.

## Handles

Items are identified by opaque handles tied to your account. A handle cannot be guessed,
and a handle issued to one user does not work for another.

## Your data

- Data created through the connector (matters, drafts, research, uploads and
  so on) is stored in your NyayAssist account, the same as data created in the
  web app, and you can see and manage it there.
- Content returned to your AI app is also processed by that app's provider
  under its own terms. Review your AI app's data settings for how it stores
  conversations.
- NyayAssist processes and retains personal data as described in the
  [Privacy Policy](https://nyayassist.ai/privacy), including how to exercise
  your rights and contact the grievance officer.

## Ending access

Disconnect NyayAssist in your AI app to stop it using your account. Your
NyayAssist data remains in your account.

## Reporting a vulnerability

See [SECURITY.md](../SECURITY.md).
