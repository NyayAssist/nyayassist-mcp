# Changelog

All notable changes to the NyayAssist MCP packaging are recorded here. The
format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
the project uses [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-08

Initial public release.

### Added

- Hosted remote MCP endpoint: `https://mcp.nyayassist.ai/mcp`.
- Sign-in with a NyayAssist account through OAuth 2.1 with PKCE.
- 44 tools covering account and plan, matters and documents, uploads, the
  Legal Library, research, drafting, translation, OCR, due diligence,
  workflows, meetings and jobs.
- MCP Registry entry (`server.json`) as `ai.nyayassist/nyayassist`.
- Claude plugin (`.claude-plugin/plugin.json`), Cursor plugin
  (`.cursor-plugin/plugin.json`) and Gemini CLI extension
  (`gemini-extension.json`, `GEMINI.md`).
- Skills: `indian-legal-research`, `case-review` and `drafting-assistant`.
- Setup guides for Claude, ChatGPT, Gemini CLI, Cursor, VS Code and other MCP
  clients; tool reference; security and privacy, troubleshooting and FAQ
  documentation.

[1.0.0]: https://github.com/NyayAssist/nyayassist-mcp/releases/tag/v1.0.0
