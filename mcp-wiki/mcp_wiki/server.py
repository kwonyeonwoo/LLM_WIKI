"""
MCP server exposing the LLM Wiki as structured tools.

Source of truth = markdown files under WIKI_ROOT. The server never holds a
separate database; every tool reads and writes the markdown files directly.

Tools (MVP, see mcp-wiki/03-prd.md):
  read:        search_wiki, read_page, list_pages
  write:       create_page, update_page   (auto index + log append)
  maintenance: link_check

Run:
  WIKI_ROOT=/path/to/repo python -m mcp_wiki.server
"""

from __future__ import annotations

import os
import re
from datetime import date
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# --- Wiki root resolution -------------------------------------------------

# Default: repo root = two levels up from this file (mcp-wiki/mcp_wiki/server.py).
_DEFAULT_ROOT = Path(__file__).resolve().parents[2]
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", _DEFAULT_ROOT)).resolve()

# Domain -> index.md heading used for auto-registration.
_DOMAIN_HEADINGS = {
    "cv": "## Concepts — Computer Vision",
    "physical-ai": "## Concepts — Physical AI",
    "intersection": "## Concepts — Intersection (CV × Physical AI)",
}

_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_META_RE = re.compile(r"Domain:\s*([^·\n]+?)\s*(?:·\s*Maturity:\s*([^\n]+))?$", re.MULTILINE)
_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

mcp = FastMCP("cv-physical-ai-wiki")


# --- Helpers --------------------------------------------------------------

def _resolve(rel_path: str) -> Path:
    """Resolve a repo-root-relative path, rejecting traversal outside WIKI_ROOT."""
    p = (WIKI_ROOT / rel_path).resolve()
    if WIKI_ROOT not in p.parents and p != WIKI_ROOT:
        raise ValueError(f"path escapes wiki root: {rel_path}")
    return p


def _rel(p: Path) -> str:
    return p.relative_to(WIKI_ROOT).as_posix()


def _title_of(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _meta_of(text: str) -> tuple[str | None, str | None]:
    m = _META_RE.search(text)
    if not m:
        return None, None
    domain = m.group(1).strip() if m.group(1) else None
    maturity = m.group(2).strip() if m.group(2) else None
    return domain, maturity


def _iter_pages():
    """Yield (Path, text) for every markdown page under wiki/."""
    wiki_dir = WIKI_ROOT / "wiki"
    if not wiki_dir.exists():
        return
    for p in sorted(wiki_dir.rglob("*.md")):
        yield p, p.read_text(encoding="utf-8")


def _append_log(action: str, detail: str) -> None:
    log = WIKI_ROOT / "log.md"
    if not log.exists():
        return
    text = log.read_text(encoding="utf-8")
    entry = f"\n## [{date.today().isoformat()}] {action} | {detail}\n"
    # Insert after the first paragraph (keep header + intro line on top).
    lines = text.splitlines(keepends=True)
    insert_at = 3 if len(lines) >= 3 else len(lines)
    lines.insert(insert_at, entry)
    log.write_text("".join(lines), encoding="utf-8")


def _register_in_index(rel_path: str, title: str, domain: str) -> bool:
    """Insert a bullet under the domain heading in index.md. Returns True if added."""
    index = WIKI_ROOT / "index.md"
    if not index.exists():
        return False
    text = index.read_text(encoding="utf-8")
    if f"]({rel_path})" in text:
        return False  # already present
    heading = _DOMAIN_HEADINGS.get(domain)
    bullet = f"- [{title}]({rel_path})\n"
    lines = text.splitlines(keepends=True)
    if heading and any(line.rstrip("\n") == heading for line in lines):
        for i, line in enumerate(lines):
            if line.rstrip("\n") == heading:
                # insert after the heading and its following blank line
                j = i + 1
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                # place after existing bullets in this section
                while j < len(lines) and lines[j].startswith("- "):
                    j += 1
                lines.insert(j, bullet)
                break
    else:
        lines.append(f"\n## Uncategorized\n\n{bullet}")
    index.write_text("".join(lines), encoding="utf-8")
    return True


# --- Tools: read ----------------------------------------------------------

@mcp.tool()
def search_wiki(query: str, domain: str | None = None) -> list[dict]:
    """Search wiki page titles and bodies for a keyword.

    Args:
        query: keyword(s) to match (case-insensitive).
        domain: optional filter — one of cv, physical-ai, intersection.
    Returns: list of {path, title, snippet} for matching pages.
    """
    q = query.lower()
    results: list[dict] = []
    for p, text in _iter_pages():
        pdomain, _ = _meta_of(text)
        if domain and (pdomain or "").split("(")[0].split(",")[0].strip() != domain:
            continue
        low = text.lower()
        if q not in low:
            continue
        idx = low.index(q)
        start = max(0, idx - 60)
        snippet = text[start: idx + 60].replace("\n", " ").strip()
        results.append({"path": _rel(p), "title": _title_of(text, p.stem), "snippet": snippet})
    return results


@mcp.tool()
def read_page(path: str) -> dict:
    """Read a single wiki page by repo-root-relative path.

    Returns: {path, title, domain, maturity, content}.
    """
    p = _resolve(path)
    if not p.exists() or p.suffix != ".md":
        raise FileNotFoundError(f"no markdown page at {path}")
    text = p.read_text(encoding="utf-8")
    domain, maturity = _meta_of(text)
    return {"path": _rel(p), "title": _title_of(text, p.stem),
            "domain": domain, "maturity": maturity, "content": text}


@mcp.tool()
def list_pages(domain: str | None = None, subdir: str | None = None) -> list[dict]:
    """List wiki pages, optionally filtered by domain or subdirectory.

    Args:
        domain: cv | physical-ai | intersection.
        subdir: path under wiki/, e.g. "concepts/cv".
    Returns: list of {path, title, domain, maturity}.
    """
    out: list[dict] = []
    for p, text in _iter_pages():
        rel = _rel(p)
        if subdir and f"wiki/{subdir}/" not in rel + "/":
            continue
        pdomain, maturity = _meta_of(text)
        if domain and (pdomain or "").split("(")[0].split(",")[0].strip() != domain:
            continue
        out.append({"path": rel, "title": _title_of(text, p.stem),
                    "domain": pdomain, "maturity": maturity})
    return out


# --- Tools: write ---------------------------------------------------------

@mcp.tool()
def create_page(path: str, title: str, domain: str, content: str) -> dict:
    """Create a new wiki page, auto-register it in index.md, and append to log.md.

    Refuses overwrite (use update_page), enforces wiki/ scope and kebab-case names.
    Args:
        path: repo-root-relative, e.g. "wiki/concepts/cv/depth-estimation.md".
        title: page H1 title.
        domain: cv | physical-ai | intersection.
        content: markdown body to write (full page).
    """
    p = _resolve(path)
    if "wiki/" not in _rel(p):
        raise ValueError("pages must live under wiki/")
    if not _SLUG_RE.match(p.stem):
        raise ValueError(f"page name must be kebab-case: {p.stem}")
    if p.exists():
        raise FileExistsError(f"page exists, use update_page: {path}")
    if domain not in _DOMAIN_HEADINGS:
        raise ValueError(f"domain must be one of {list(_DOMAIN_HEADINGS)}")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    indexed = _register_in_index(_rel(p), title, domain)
    _append_log("create", f"{_rel(p)} ({domain})")
    return {"path": _rel(p), "created": True, "indexed": indexed}


@mcp.tool()
def update_page(path: str, content: str) -> dict:
    """Overwrite an existing wiki page and append to log.md.

    Args:
        path: repo-root-relative path to an existing page.
        content: new full markdown body.
    """
    p = _resolve(path)
    if not p.exists():
        raise FileNotFoundError(f"no page at {path}, use create_page")
    old = p.read_text(encoding="utf-8")
    p.write_text(content, encoding="utf-8")
    delta = len(content.splitlines()) - len(old.splitlines())
    _append_log("update", f"{_rel(p)} ({delta:+d} lines)")
    return {"path": _rel(p), "updated": True, "line_delta": delta}


# --- Tools: maintenance ---------------------------------------------------

@mcp.tool()
def link_check() -> dict:
    """Scan all markdown for broken internal links and index-missing concept pages.

    Returns: {broken_links: [...], unindexed_pages: [...]}.
    """
    broken: list[dict] = []
    md_files = list(WIKI_ROOT.rglob("*.md"))
    for p in md_files:
        if ".git" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        for link in _LINK_RE.findall(text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (p.parent / link.split("#")[0]).resolve()
            if not target.exists():
                broken.append({"file": _rel(p), "link": link})

    index_text = (WIKI_ROOT / "index.md").read_text(encoding="utf-8")
    unindexed = [
        _rel(p) for p, _ in _iter_pages()
        if "concepts/" in _rel(p) and f"]({_rel(p)})" not in index_text
    ]
    return {"broken_links": broken, "unindexed_pages": unindexed}


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
