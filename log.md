# Log

Append-only 작업 기록이다. 새 ingest, query, lint 작업이 끝나면 최신 항목을 위에 추가한다.

## [2026-06-06] domain-switch | Computer Vision / Physical AI

- 지식 도메인을 Agentic Coding Basics → 컴퓨터비전 / 피지컬 AI로 전환 (완전 교체).
- 삭제: `sources/agentic-coding-basics/` 전체, ACB 개념 페이지 9개, `wiki/analyses/agentic-coding-basics-synthesis.md`.
- 보존: 위키 시스템 메타 개념 4개(llm-wiki, rag-vs-llm-wiki, persistent-knowledge-artifact, markdown-only-constraint), workflows/schema/pipelines/templates.
- 신규 source note 7개 (`sources/cv-physical-ai/`) — 검증 출처(arXiv, Meta AI, INRIA)에서 web search로 수집.
- 신규 wiki 개념 페이지 7개: cv 4(object-detection, SAM family, NeRF/GS, vision foundation models), physical-ai 2(sim-to-real, sensor fusion), intersection 1(VLA models).
- `index.md` 재구성, `wiki/overview.md` scope 갱신.

## [2026-06-01] ingest | Agentic Coding Basics source pack

- Imported `Agentic_Coding_Basics.zip` as a Markdown-only source pack.
- Created 9 source notes under `sources/agentic-coding-basics/`.
- Added wiki concept pages for agentic coding, SDLC/spec-driven development, subprocess calling, plan mode, agent specifications, agent pool/orchestrator, harness engineering, MCP, and loop/hooks.
- Added [LLM Wiki Schema](wiki/schema/llm-wiki-schema.md), [Raw Item To Wiki Pages Pipeline](wiki/pipelines/raw-item-to-wiki-pages.md), and [LLM Maintenance](wiki/workflows/maintenance.md).
- Added `TASK.md` and `journal.md` for contract-driven maintenance.
- Generated `submissions/llm-wiki-repository-sources.zip` for assignment submission.

## [2026-05-18] setup | Initial markdown-only LLM Wiki

- Created the initial markdown-only wiki structure.
- Seeded the wiki with Karpathy's LLM Wiki pattern as the first source.
- Added concept pages for LLM Wiki, RAG comparison, persistent knowledge artifacts, and markdown-only constraints.
- Added ingest, query, and lint workflows.
- Added reusable templates.
