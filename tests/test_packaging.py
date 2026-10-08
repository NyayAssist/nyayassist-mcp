"""Static checks for the NyayAssist MCP packaging repository.

The repository holds manifests, skills and documentation only, so these tests
check file content: manifests parse and agree with each other, URLs are
consistent, every tool name used in skills and docs exists on the server, and
nothing that must not be published is present.

Run with: python3 -m pytest -q tests
"""

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
THIS_FILE = Path(__file__).resolve()

VERSION = "1.0.0"
MAIN_URL = "https://mcp.nyayassist.ai/mcp"
REGISTRY_NAME = "ai.nyayassist/nyayassist"
REPO_URL = "https://github.com/NyayAssist/nyayassist-mcp"
SUPPORT_EMAIL = "support@nyayassist.ai"

JSON_MANIFESTS = [
    "server.json",
    ".mcp.json",
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    "gemini-extension.json",
]
VERSIONED_MANIFESTS = [
    "server.json",
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    "gemini-extension.json",
]
SKILLS = ["indian-legal-research", "case-review", "drafting-assistant"]
SKILL_FILES = [f"skills/{name}/SKILL.md" for name in SKILLS]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GEMINI.md",
    ".gitignore",
    "assets/README.md",
    "docs/tools.md",
    "docs/security-and-privacy.md",
    "docs/troubleshooting.md",
    "docs/faq.md",
    "docs/setup/claude.md",
    "docs/setup/chatgpt.md",
    "docs/setup/gemini.md",
    "docs/setup/cursor.md",
    "docs/setup/vscode.md",
    "docs/setup/other-clients.md",
    *JSON_MANIFESTS,
    *SKILL_FILES,
]

TEXT_SUFFIXES = {".md", ".json", ".txt", ".py", ".toml", ".yml", ".yaml", ""}
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__"}


def read(relpath: str) -> str:
    return (REPO_ROOT / relpath).read_text(encoding="utf-8")


def load_json(relpath: str) -> dict:
    return json.loads(read(relpath))


def repo_text_files():
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def markdown_files():
    return [p for p in repo_text_files() if p.suffix == ".md"]


def server_tool_names() -> set:
    names = {
        line.strip()
        for line in read("tests/tool_names.txt").splitlines()
        if line.strip() and not line.startswith("#")
    }
    return names


# ---------------------------------------------------------------------------
# Repository layout
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("relpath", REQUIRED_FILES)
def test_required_file_exists(relpath):
    assert (REPO_ROOT / relpath).is_file(), f"missing {relpath}"


def test_no_junk_in_tree():
    # __pycache__ is created by running these tests and is gitignored.
    junk = [
        p.relative_to(REPO_ROOT)
        for p in REPO_ROOT.rglob("*")
        if not SKIP_DIRS.intersection(p.relative_to(REPO_ROOT).parts)
        and p.name in {".DS_Store", "Thumbs.db"}
    ]
    assert not junk, f"remove junk files: {junk}"


def test_gitignore_covers_artefacts():
    text = read(".gitignore")
    for entry in (".pytest_cache/", "__pycache__/", ".DS_Store"):
        assert entry in text


# ---------------------------------------------------------------------------
# Manifests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("relpath", JSON_MANIFESTS)
def test_manifest_is_valid_json_object(relpath):
    assert isinstance(load_json(relpath), dict)


@pytest.mark.parametrize("relpath", VERSIONED_MANIFESTS)
def test_manifest_version_is_consistent(relpath):
    assert load_json(relpath)["version"] == VERSION


def test_changelog_has_current_version():
    assert f"## [{VERSION}] - 2026-10-08" in read("CHANGELOG.md")


def test_server_json_structure():
    data = load_json("server.json")
    assert data["$schema"].startswith("https://static.modelcontextprotocol.io/schemas/")
    assert data["name"] == REGISTRY_NAME
    assert re.fullmatch(r"[a-zA-Z0-9.-]+/[a-zA-Z0-9._-]+", data["name"])
    assert 1 <= len(data["title"]) <= 100
    # The registry schema caps description at 100 characters.
    assert 1 <= len(data["description"]) <= 100
    assert data["websiteUrl"] == "https://nyayassist.ai"
    assert data["repository"] == {"url": REPO_URL, "source": "github"}
    remotes = data["remotes"]
    assert [r["url"] for r in remotes] == [MAIN_URL]
    assert all(r["type"] == "streamable-http" for r in remotes)
    assert "packages" not in data, "hosted server: remotes only, no packages"


def test_server_json_validates_against_cached_schema_if_available():
    """Validates against the official schema when jsonschema and a local copy
    of the schema (tests/server.schema.json, not committed) are present."""
    jsonschema = pytest.importorskip("jsonschema")
    schema_path = REPO_ROOT / "tests" / "server.schema.json"
    if not schema_path.exists():
        pytest.skip("download the schema to tests/server.schema.json to run this check")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.validate(load_json("server.json"), schema)


def test_mcp_json_points_at_main_url():
    server = load_json(".mcp.json")["mcpServers"]["nyayassist"]
    assert server == {"type": "http", "url": MAIN_URL}


def test_gemini_extension():
    data = load_json("gemini-extension.json")
    assert data["name"] == "nyayassist"
    assert data["contextFileName"] == "GEMINI.md"
    assert data["mcpServers"]["nyayassist"]["httpUrl"] == MAIN_URL


@pytest.mark.parametrize("relpath", [".claude-plugin/plugin.json", ".cursor-plugin/plugin.json"])
def test_plugin_manifest_common_fields(relpath):
    data = load_json(relpath)
    assert data["name"] == "nyayassist"
    assert re.fullmatch(r"[a-z0-9][a-z0-9.-]*[a-z0-9]", data["name"])
    assert data["author"]["name"] == "NyayAssist"
    assert data["repository"] == REPO_URL
    assert data["license"] == "MIT"
    assert data["homepage"].startswith(("https://nyayassist.ai", "https://docs.nyayassist.ai"))


def test_plugin_descriptions_match():
    descs = {
        load_json(p)["description"]
        for p in (".claude-plugin/plugin.json", ".cursor-plugin/plugin.json", "gemini-extension.json")
    }
    assert len(descs) == 1, f"plugin descriptions differ: {descs}"


def test_cursor_plugin_references_existing_paths():
    data = load_json(".cursor-plugin/plugin.json")
    assert data["mcpServers"] == ".mcp.json"
    assert (REPO_ROOT / data["mcpServers"]).is_file()
    assert (REPO_ROOT / data["skills"]).is_dir()
    if "logo" in data:
        assert (REPO_ROOT / data["logo"]).is_file()


# ---------------------------------------------------------------------------
# URL consistency across files
# ---------------------------------------------------------------------------

MCP_URL_RE = re.compile(r"https://mcp\.nyayassist\.ai[^\s\"'`)<>\]]*")
ALLOWED_MCP_URLS = {
    MAIN_URL,
    "https://mcp.nyayassist.ai/.well-known/oauth-protected-resource/mcp",
}


def test_only_known_server_urls_are_used():
    bad = {}
    for path in repo_text_files():
        if path == THIS_FILE:
            continue
        for url in MCP_URL_RE.findall(path.read_text(encoding="utf-8")):
            url = url.rstrip(".,;:")
            if url not in ALLOWED_MCP_URLS:
                bad.setdefault(str(path.relative_to(REPO_ROOT)), set()).add(url)
    assert not bad, f"unexpected server URLs: {bad}"


def test_encoded_install_links_point_at_known_urls():
    import base64
    from urllib.parse import unquote

    cursor = read("docs/setup/cursor.md")
    configs = re.findall(r"config=([A-Za-z0-9+/=]+)\)", cursor)
    assert configs, "Cursor install links missing"
    for b64 in configs:
        assert json.loads(base64.b64decode(b64))["url"] == MAIN_URL

    vscode = read("docs/setup/vscode.md")
    payloads = re.findall(r"vscode:mcp/install\?([^)\s]+)\)", vscode)
    assert payloads, "VS Code install links missing"
    for payload in payloads:
        cfg = json.loads(unquote(payload))
        assert cfg["type"] == "http" and cfg["url"] == MAIN_URL


def test_main_endpoint_documented():
    for relpath in ("README.md", "docs/setup/other-clients.md"):
        assert MAIN_URL in read(relpath), relpath


def test_no_private_endpoint_anywhere_in_repo():
    # Built from parts so this file does not contain the string itself.
    needles = [("enterprise" + sep + "mcp").encode() for sep in ("/", "%2F", "%2f")]
    hits = []
    for path in sorted(REPO_ROOT.rglob("*")):
        rel = path.relative_to(REPO_ROOT)
        if not path.is_file() or ".git" in rel.parts:
            continue
        data = path.read_bytes()
        if any(n in data for n in needles):
            hits.append(str(rel))
    assert not hits, f"private endpoint mentioned in: {hits}"


def test_public_links_are_the_agreed_ones():
    readme = read("README.md")
    for url in (
        "https://nyayassist.ai/privacy",
        "https://nyayassist.ai/terms",
        "https://docs.nyayassist.ai/get-started-with-mcp/",
        SUPPORT_EMAIL,
    ):
        assert url in readme, url


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def test_only_the_public_support_email_is_used():
    emails = set()
    for path in repo_text_files():
        if path == THIS_FILE:
            continue
        emails |= set(EMAIL_RE.findall(path.read_text(encoding="utf-8")))
    assert emails == {SUPPORT_EMAIL}, emails


# ---------------------------------------------------------------------------
# Tool names
# ---------------------------------------------------------------------------

TOOL_PREFIXES = (
    "get_", "list_", "search_", "read_", "create_", "add_", "start_", "stop_",
    "revise_", "translate_", "run_", "approve_", "cancel_", "upload_",
)
TOOL_TOKEN_RE = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")
# Input and output field names share prefixes with tool names
# (upload_handle, run_type); they are not tools.
FIELD_SUFFIXES = ("_handle", "_handles", "_type", "_url", "_id", "_cursor", "_offset", "_page")


def test_tool_fixture_has_44_unique_names():
    lines = [l.strip() for l in read("tests/tool_names.txt").splitlines() if l.strip()]
    assert len(lines) == len(set(lines)) == 44


def test_every_tool_mentioned_in_docs_and_skills_exists():
    known = server_tool_names()
    unknown = {}
    for path in markdown_files():
        for token in TOOL_TOKEN_RE.findall(path.read_text(encoding="utf-8")):
            if (
                token.startswith(TOOL_PREFIXES)
                and not token.endswith(FIELD_SUFFIXES)
                and token not in known
            ):
                unknown.setdefault(str(path.relative_to(REPO_ROOT)), set()).add(token)
    assert not unknown, f"tool names not on the server: {unknown}"


def test_tool_reference_documents_every_tool():
    documented = set(re.findall(r"^### `([a-z_]+)`$", read("docs/tools.md"), re.M))
    assert documented == server_tool_names()


def test_readme_tool_table_lists_every_tool():
    readme = read("README.md")
    table = readme.split("| Group | Tools |", 1)[1].split("\n\n", 1)[0]
    listed = re.findall(r"`([a-z_]+)`", table)
    assert len(listed) == len(set(listed))
    assert set(listed) == server_tool_names()


def test_dropped_tools_are_not_mentioned():
    for path in markdown_files():
        assert "search_case_documents" not in path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Skills
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


@pytest.mark.parametrize("name", SKILLS)
def test_skill_frontmatter(name):
    text = read(f"skills/{name}/SKILL.md")
    match = FRONTMATTER_RE.match(text)
    assert match, "SKILL.md must start with YAML frontmatter"
    fields = dict(
        line.split(":", 1) for line in match.group(1).splitlines() if ":" in line
    )
    fields = {k.strip(): v.strip() for k, v in fields.items()}
    assert set(fields) == {"name", "description", "license"}
    assert fields["name"] == name
    assert fields["description"].startswith("Use when")
    assert len(fields["description"]) <= 1024
    assert fields["license"] == "MIT"


@pytest.mark.parametrize("relpath", SKILL_FILES)
def test_skill_has_legal_positioning(relpath):
    text = read(relpath)
    assert "## Legal positioning" in text
    assert "not a\nsubstitute" in text or "not a substitute" in text


@pytest.mark.parametrize("relpath", SKILL_FILES)
def test_skill_respects_user_intent_and_untrusted_content(relpath):
    text = " ".join(read(relpath).split())
    assert "never starts work the user did not ask for" in text
    assert "<untrusted_document>" in text


def test_drafting_skill_does_not_promise_download_link():
    assert "download link" not in read("skills/drafting-assistant/SKILL.md").lower()


def test_research_skill_does_not_claim_auto_pagination():
    text = " ".join(read("skills/indian-legal-research/SKILL.md").split())
    assert "paginates automatically" not in text
    assert "request later pages explicitly" in text
