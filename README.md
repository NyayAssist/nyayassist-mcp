# NyayAssist MCP

**Indian legal research, drafting and matter work from NyayAssist, inside the AI apps you already use.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![MCP: remote server](https://img.shields.io/badge/MCP-remote%20server-black.svg)](https://modelcontextprotocol.io)

NyayAssist is a research and drafting platform for advocates practising Indian
law. The NyayAssist MCP server connects your NyayAssist account to any app that
supports the [Model Context Protocol](https://modelcontextprotocol.io), so you
can search judgments and Acts, research a legal question, draft and revise
documents, translate, review your matters, run due diligence and more, all from
a chat.

This repository holds the public packaging for the hosted server: client
manifests, skills, and documentation. The server itself is run by NyayAssist;
there is nothing to install or host.

## What it does

- **Legal Library:** search reported Indian judgments and central and state
  Acts, and fetch their details and summaries.
- **Research:** ask a legal research question and get an answer that cites
  Indian judgments and Acts, optionally grounded in one of your matters.
- **Drafting:** create a legal draft from instructions (optionally using a
  matter's facts), then revise it; every revision is a new version.
- **Matters and documents:** list and read your matters and their documents,
  create matters, and add or upload documents.
- **Translation and OCR:** translate a document into English or one of nine Indian
  languages, and run text recognition on scanned documents.
- **Due diligence:** create projects, add documents and run reports.
- **Workflows and meetings:** run your NyayAssist workflows, send a notetaker
  to a Google Meet or Microsoft Teams call, or process a recording.

Everything runs in your own NyayAssist account and follows your plan, exactly
as in the NyayAssist web app.

## Supported apps

| App | How to connect | Guide |
|---|---|---|
| Claude (web, desktop, mobile) | Add a custom connector with the server URL | [docs/setup/claude.md](docs/setup/claude.md) |
| ChatGPT | Add a connector in developer mode | [docs/setup/chatgpt.md](docs/setup/chatgpt.md) |
| Gemini CLI | Install the extension from this repository | [docs/setup/gemini.md](docs/setup/gemini.md) |
| Cursor | One-click install link, or the plugin in this repository | [docs/setup/cursor.md](docs/setup/cursor.md) |
| VS Code | Install link, or a `mcp.json` entry | [docs/setup/vscode.md](docs/setup/vscode.md) |
| Any other MCP client | Remote server URL with OAuth | [docs/setup/other-clients.md](docs/setup/other-clients.md) |

### Quick start

**Claude:** open **Settings → Connectors → Add custom connector**, enter
`https://mcp.nyayassist.ai/mcp`, then **Connect** and sign in with your
NyayAssist account.

**ChatGPT:** turn on developer mode under **Settings → Apps & Connectors →
Advanced settings**, create a connector with the URL
`https://mcp.nyayassist.ai/mcp` and OAuth authentication, then sign in.

**Gemini CLI:**

```bash
gemini extensions install https://github.com/NyayAssist/nyayassist-mcp
```

**Cursor:** use the install link in [docs/setup/cursor.md](docs/setup/cursor.md),
or add this to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "nyayassist": { "url": "https://mcp.nyayassist.ai/mcp" }
  }
}
```

**VS Code:**

```bash
code --add-mcp '{"name":"nyayassist","type":"http","url":"https://mcp.nyayassist.ai/mcp"}'
```

The first time a tool is used, your app opens the NyayAssist sign-in page.
Sign in with the same account you use on nyayassist.ai.

## Endpoint

| Account type | Server URL |
|---|---|
| NyayAssist accounts (all plans) | `https://mcp.nyayassist.ai/mcp` |

The endpoint uses the Streamable HTTP transport and OAuth 2.1.

NyayAssist Enterprise customers: your organisation receives its own setup
instructions from your NyayAssist account team.

## Authentication and data access

- You sign in with your existing NyayAssist login through OAuth 2.1 with PKCE.
  There is no API key to create or paste.
- Your app receives a token for the NyayAssist MCP server only. The server
  exchanges it for access to your account on its side; your app never sees
  NyayAssist backend credentials.
- The connector sees only what your own account can see: your matters,
  documents, drafts, research, due-diligence projects, workflows and meetings,
  plus the shared Legal Library.
- Nothing can be deleted, shared or sent through the connector. See
  [Privacy and security](#privacy-and-security).

## Tools

The server offers 44 tools. The list is the same for every user; what a call
may do depends on your plan. Full reference: [docs/tools.md](docs/tools.md).

| Group | Tools |
|---|---|
| Account and plan | `get_my_plan_and_usage` |
| Matters and documents | `list_cases`, `get_case`, `list_case_documents`, `read_case_document`, `create_case`, `add_document_to_case` |
| Uploads | `get_document_upload_urls`, `upload_documents` |
| Legal Library | `search_judgments`, `get_judgment`, `search_acts`, `get_act_section` |
| Research | `start_research`, `get_research` |
| Drafting | `create_draft`, `revise_draft`, `list_drafts`, `get_draft` |
| Translation and document tools | `translate_document`, `get_translation`, `run_document_tool`, `get_document_tool_result` |
| Due diligence | `list_dd`, `create_dd`, `add_dd_documents`, `run_dd`, `get_dd_status`, `get_dd_report` |
| Workflows | `list_workflows`, `start_workflow`, `get_workflow_run`, `approve_workflow_gate`, `get_workflow_output` |
| Meetings | `list_meetings`, `get_meeting`, `start_meeting`, `stop_meeting`, `get_meeting_upload_url`, `upload_meeting_recording` |
| Jobs | `get_job_status`, `get_job_result`, `list_my_jobs`, `cancel_job` |

### Example prompts

- "Find Supreme Court judgments from the last five years on adverse possession
  and summarise the three most relevant."
- "List the documents in my matter 'Sharma v. State' and tell me the key dates
  in the charge sheet."
- "Draft a reply to a legal notice for non-payment of rent under a leave and
  licence agreement, using the facts in my matter 'Verma Tenancy'."
- "Translate the order I uploaded yesterday into Marathi."
- "Start a key-issues due-diligence report on the 'Acme Acquisition' project."

## Skills

Three skills teach the assistant how to sequence the tools well. They are
bundled with the Claude, Cursor and Gemini CLI packages in this repository:

- [`indian-legal-research`](skills/indian-legal-research/SKILL.md): searching
  judgments and Acts, research questions and accurate citation.
- [`case-review`](skills/case-review/SKILL.md): reviewing a matter and reading
  its documents in page ranges.
- [`drafting-assistant`](skills/drafting-assistant/SKILL.md): creating,
  following and revising drafts.

## Plans and limits

- The connector is available on every NyayAssist plan. Tools that create work
  (research, drafts, translations, OCR, matters, uploads, due diligence,
  workflow runs and meetings) use the same allowances as the web app.
  Reading and listing your existing material does not.
- Ask the assistant to run `get_my_plan_and_usage` to see what is left before
  a long piece of work. Plans and pricing: https://nyayassist.ai/pricing.
- Long-running work returns a job instead of a result. The assistant checks it
  with `get_job_status` and fetches the result with `get_job_result`.
- A feature that is not on your plan is still listed; calling it returns a
  clear message instead of a result.

## Privacy and security

- **Create, never delete.** No tool deletes, shares or sends anything, or
  changes billing or settings. The one tool that reaches outside NyayAssist on
  its own is `start_meeting`, which sends a NyayAssist notetaker into the call
  you give it.
- **Documents are data, not instructions.** Text from judgments, Acts and your
  documents is returned inside `<untrusted_document>` tags, and the server
  tells the assistant never to follow instructions found there.
- **Opaque handles.** Matters, documents, drafts and jobs are referred to by
  opaque handles tied to your account; one user's handle does not work for
  anyone else.
- **Your data stays in your NyayAssist account** and is handled under the
  NyayAssist [Privacy Policy](https://nyayassist.ai/privacy).

More detail: [docs/security-and-privacy.md](docs/security-and-privacy.md). To
report a vulnerability, see [SECURITY.md](SECURITY.md).

## Research support, not legal advice

NyayAssist output is research and drafting support for a qualified advocate to
verify. It is not legal advice and not a finished filing. Check every
citation, section number and date against the source before relying on it.

## Troubleshooting

- **Sign-in window does not open or loops:** remove the connector, add it
  again, and sign in with the same account you use on nyayassist.ai.
- **"Not found" for a handle:** handles come only from earlier tool results;
  ask the assistant to list the item again.
- **Limit reached or feature not on plan:** run `get_my_plan_and_usage`.

Full guide: [docs/troubleshooting.md](docs/troubleshooting.md). Common
questions: [docs/faq.md](docs/faq.md).

## Links

- Website: https://nyayassist.ai
- Connector documentation: https://docs.nyayassist.ai/get-started-with-mcp/
- Privacy Policy: https://nyayassist.ai/privacy
- Terms of Use: https://nyayassist.ai/terms
- Support: support@nyayassist.ai
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Licence

The files in this repository are released under the [MIT License](LICENSE).
The NyayAssist service, the hosted MCP server and the NyayAssist name and logo
are not covered by this licence; use of the service is governed by the
NyayAssist [Terms of Use](https://nyayassist.ai/terms).
