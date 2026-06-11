"""
Local Wiki Guide bridge — keyless chatbot backend for the static site.

The site's chatbot POSTs a question here. This bridge:
  1. retrieves the most relevant wiki pages (keyword score over WIKI_ROOT/wiki),
  2. asks the locally logged-in Claude CLI (`claude -p`, your subscription —
     NO API key) to answer using only those pages,
  3. returns {answer, cites:[{title, path}]}.

No API key, no cloud secret. Reuses the `claude` CLI you already log into.
(Swap CLAUDE_CMD below for any local model CLI, e.g. `ollama run <model>`.)

Run:
  WIKI_ROOT=/path/to/repo python serve/guide_bridge.py        # serves :8765
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(os.environ.get("WIKI_ROOT", Path(__file__).resolve().parents[2])).resolve()
WIKI = ROOT / "wiki"
PORT = int(os.environ.get("GUIDE_PORT", "8765"))
CLAUDE = os.environ.get("CLAUDE_BIN") or shutil.which("claude") or "claude"
TOP_K = 4

SYS = (
    "너는 이 LLM Wiki의 Wiki Guide다. 아래 '참고 위키 페이지' 내용만 근거로 한국어로 간결히 답한다. "
    "위키에 없으면 '위키에 없음'이라고 명시한다. 추측을 사실처럼 단정하지 않는다. "
    "답 끝에 근거로 쓴 페이지 제목을 적는다."
)


def pages():
    if not WIKI.exists():
        return
    for p in sorted(WIKI.rglob("*.md")):
        yield p, p.read_text(encoding="utf-8")


def title_of(text, fallback):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def retrieve(q, k=TOP_K):
    low = q.lower()
    # whitespace tokens + latin/number substrings (so "DETR의" still matches "detr")
    terms = {t for t in re.split(r"\s+", low) if len(t) > 1}
    terms |= set(re.findall(r"[a-z0-9]{2,}", low))
    terms = [t for t in terms if len(t) > 1]
    scored = []
    for p, text in pages():
        title = title_of(text, p.stem)
        low = (title + "\n" + text).lower()
        s = sum((3 if t in title.lower() else 0) + (1 if t in low else 0) for t in terms)
        if s:
            scored.append((s, p, title, text))
    scored.sort(key=lambda x: -x[0])
    return scored[:k]


def _decode(b):
    if not b:
        return ""
    for enc in ("utf-8", "cp949", "cp1252"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            continue
    return b.decode("utf-8", errors="replace")


def ask_claude(question, hits):
    context = "\n\n---\n\n".join(
        f"# {title}  (path: {p.relative_to(ROOT).as_posix()})\n{text[:1800]}"
        for _, p, title, text in hits
    ) or "(관련 페이지 없음)"
    prompt = f"{SYS}\n\n질문: {question}\n\n참고 위키 페이지:\n\n{context}"
    # bytes capture + defensive decode: Windows claude.exe may emit cp949, not utf-8.
    out = subprocess.run([CLAUDE, "-p", prompt], capture_output=True, timeout=120, cwd=str(ROOT))
    so, se = _decode(out.stdout), _decode(out.stderr)
    if out.returncode != 0:
        raise RuntimeError((se or so or "claude failed").strip()[:500])
    return so.strip()


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    def _json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self._cors()
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_GET(self):
        self._json(200, {"ok": True, "wiki_root": str(ROOT), "claude": CLAUDE})

    def do_POST(self):
        if self.path.rstrip("/") != "/ask":
            return self._json(404, {"error": "POST /ask"})
        try:
            n = int(self.headers.get("content-length", 0))
            raw = self.rfile.read(n) or b"{}"
            q = (json.loads(_decode(raw) or "{}").get("question") or "").strip()
            if not q:
                return self._json(400, {"error": "question required"})
            hits = retrieve(q)
            answer = ask_claude(q, hits)
            cites = [{"title": t, "path": p.relative_to(ROOT).as_posix()} for _, p, t, _ in hits]
            self._json(200, {"answer": answer, "cites": cites})
        except subprocess.TimeoutExpired:
            self._json(504, {"error": "claude 응답 시간 초과"})
        except Exception as e:
            self._json(500, {"error": str(e)})

    def log_message(self, *a):
        pass


def main():
    if not shutil.which(CLAUDE) and not Path(CLAUDE).exists():
        print(f"warn: claude CLI not found ({CLAUDE}). 로그인된 claude CLI 필요(무키). "
              f"또는 CLAUDE_BIN으로 다른 로컬 모델 CLI 지정.")
    print(f"Wiki Guide bridge: http://localhost:{PORT}  (WIKI_ROOT={ROOT}, claude={CLAUDE})")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
