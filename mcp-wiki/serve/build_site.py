"""
Static-site builder (Stack A) for the CV / Physical AI LLM Wiki.

Scans markdown under WIKI_ROOT/wiki, extracts metadata + Related links, and
emits a self-contained static site:
  site/data.json   nodes (pages) + edges (Related links) + raw markdown
  site/index.html  graph view + page reader + keyword search (D3 + marked via CDN)

Pure stdlib. No build framework. Rendering happens client-side.

Run:
  python serve/build_site.py            # writes mcp-wiki/site/
  python -m http.server -d mcp-wiki/site 8000   # serve locally
"""

from __future__ import annotations

import json
import os
import re
import shutil
from pathlib import Path

ROOT = Path(os.environ.get("WIKI_ROOT", Path(__file__).resolve().parents[2])).resolve()
WIKI = ROOT / "wiki"
OUT = Path(__file__).resolve().parent.parent / "site"

_META_RE = re.compile(r"Domain:\s*([^·\n]+?)\s*(?:·\s*Maturity:\s*([^\n]+))?$", re.MULTILINE)
_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def title_of(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def meta_of(text: str):
    m = _META_RE.search(text)
    if not m:
        return None, None
    d = m.group(1).strip().split("(")[0].split(",")[0].strip() if m.group(1) else None
    mat = m.group(2).strip() if m.group(2) else None
    return d, mat


def build() -> dict:
    nodes, edges = [], []
    ids = set()
    pages = sorted(WIKI.rglob("*.md"))
    for p in pages:
        ids.add(p.resolve())
    for p in pages:
        text = p.read_text(encoding="utf-8")
        domain, maturity = meta_of(text)
        rel = p.relative_to(ROOT).as_posix()
        nodes.append({
            "id": rel,
            "title": title_of(text, p.stem),
            "domain": domain or "meta",
            "maturity": maturity or "",
            "markdown": text,
        })
        # edges from internal links pointing to other existing pages
        for _label, link in _LINK_RE.findall(text):
            if link.startswith(("http", "#", "mailto:")):
                continue
            target = (p.parent / link.split("#")[0]).resolve()
            if target in ids and target != p.resolve():
                edges.append({"source": rel, "target": target.relative_to(ROOT).as_posix()})
    return {"nodes": nodes, "edges": edges}


def main() -> None:
    if not WIKI.exists():
        raise SystemExit(f"no wiki/ under {ROOT}")
    OUT.mkdir(exist_ok=True)
    data = build()
    (OUT / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    here = Path(__file__).resolve().parent
    shutil.copyfile(here / "template.html", OUT / "index.html")
    # Chatbot bridge config (no API key): prefer local guide-config.js, else example.
    cfg = here / "guide-config.js"
    if not cfg.exists():
        cfg = here / "guide-config.example.js"
    shutil.copyfile(cfg, OUT / "guide-config.js")
    print(f"built {len(data['nodes'])} pages, {len(data['edges'])} links -> {OUT}")


if __name__ == "__main__":
    main()
