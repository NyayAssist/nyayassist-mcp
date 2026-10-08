# Contributing

Thank you for your interest in NyayAssist.

## What this repository covers

This repository contains the public packaging for the hosted NyayAssist MCP
server: client manifests, skills and documentation. The server itself is run
by NyayAssist and is not open source, so changes to tools or server behaviour
cannot be made here.

## Issues

Issues are welcome for:

- setup instructions that are wrong or out of date for a client;
- manifest problems (a plugin or extension that does not install);
- unclear or incorrect documentation and skills.

For problems with your NyayAssist account, billing or a specific result,
email support@nyayassist.ai instead. For security issues, follow
[SECURITY.md](SECURITY.md) and do not open a public issue.

## Pull requests

Small documentation and manifest fixes are welcome. Before opening a pull
request, run the packaging checks:

```bash
python3 -m pip install pytest
python3 -m pytest -q tests
```

Keep versions consistent across `server.json`, `.claude-plugin/plugin.json`,
`.cursor-plugin/plugin.json` and `gemini-extension.json`, and use only tool
names listed in `tests/tool_names.txt`.

By contributing, you agree that your contribution is licensed under the
[MIT License](LICENSE).
