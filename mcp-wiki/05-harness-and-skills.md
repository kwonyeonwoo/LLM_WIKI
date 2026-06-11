---
title: 하네스 & 스킬 — 재사용 가능한 실행 구조
status: active
date: 2026-06-06
updated: 2026-06-11
tags: [harness, skill, mcp-wiki, reusable, serving]
description: MCP wiki tool 구현과 LLM wiki 페이지 서빙을 재사용 가능하게 묶는 하네스(계약·절차·도구·저널·서빙 계층)와 Claude 스킬(wiki-keeper) 카탈로그를 정리한 문서.
type: harness-spec
---

# 하네스 & 스킬: 재사용 가능한 실행 구조

Status: active (하네스 5계층 + wiki-keeper 스킬 구현됨)
관련 문서: [에이전트 사양](04-agent-spec.md) · [README](README.md) · [PRD](03-prd.md) · [운영 규칙](../AGENTS.md)

**하네스(harness)** = 에이전트가 매번 즉흥적으로 일하지 않도록 감싸는 재사용 실행 구조. **스킬(skill)** = 그 하네스를 한 번에 호출하는 진입점. 도메인이 바뀌어도(CV/Physical AI → 다른 주제) 그대로 재사용된다 — 도메인은 데이터(markdown)일 뿐, 실행 구조는 불변.

## 1. 하네스 계층

| 계층 | 구현물 | 역할 |
|---|---|---|
| **Contract (계약)** | [AGENTS.md](../AGENTS.md), [TASK.md](../TASK.md), [04-agent-spec.md](04-agent-spec.md) | 무엇을 하고/하지 말지, 권한·완료조건 |
| **Procedure (절차)** | [ingest](../wiki/workflows/ingest.md) · [query](../wiki/workflows/query.md) · [lint](../wiki/workflows/lint.md) · [pipeline](../wiki/pipelines/raw-item-to-wiki-pages.md) | 단계화된 작업 흐름 |
| **Tools (도구)** | `mcp_wiki/server.py` (6 tool) | 절차를 강제하는 결정적 동작 |
| **Journal (저널)** | [log.md](../log.md), [journal.md](../journal.md) | 변경·세션 흔적 (append-only) |
| **Serving (서빙)** | `serve/build_site.py` + `template.html` | markdown → 그래프·페이지·검색 시각화 |

핵심: 계약·절차는 **사람이 읽는 규칙**, tool·서빙은 **기계가 강제하는 실행**. 둘이 같은 markdown(source of truth)을 공유.

## 2. 재사용성의 근거

- **도메인 독립**: tool·빌더는 `WIKI_ROOT` 환경변수만 바꾸면 다른 위키에 그대로 붙는다. CV/Physical AI 특화 코드 없음.
- **포맷 계약**: 페이지는 `# Title` + `Domain: x · Maturity: y` + `## Related` 규약만 지키면 그래프·필터·검색이 자동 동작. 파서가 이 규약에 의존.
- **무상태 빌드**: `build_site.py`는 stdlib만 쓰고 파일에서 전부 파생 → 어디서나 재실행 가능, 캐시는 버려도 됨.
- **transport 표준**: MCP stdio라 Claude Desktop·기타 클라이언트에 공통 연결.

## 3. 스킬 카탈로그

### `wiki-keeper` (구현됨: `skills/wiki-keeper/SKILL.md`)
하나의 스킬로 Keeper 워크플로우 전체를 진입. 내부에서 MCP tool + 서빙 빌더를 순서대로 호출.

호출 시 수행:
1. **ingest**: 출처 검증 → source note 작성 → `create_page`/`update_page`.
2. **maintain**: `link_check` → 끊긴 링크·색인 누락 0 만들기.
3. **serve**: `build_site.py` 실행 → 사이트 갱신.
4. **journal**: `log.md`/`journal.md` 반영 확인.

설치(재사용): `skills/wiki-keeper/`를 프로젝트 `.claude/skills/`에 복사하거나 심볼릭 링크. 그러면 `/wiki-keeper`로 호출 가능.

### `wiki-guide` (구현됨: `skills/wiki-guide/SKILL.md`)
read-only Q&A 진입. 위키 MCP read tool(search/read/list)로 관련 페이지를 찾아 근거 기반으로 답하고 출처를 단다. **API 키 불필요**(현재 Claude 구독/세션 사용). 권한 분리 — 쓰기 금지([04 §1](04-agent-spec.md)). 사이트 챗봇의 로컬 브리지(`serve/guide_bridge.py`)와 같은 Guide의 두 표면.

### 향후 스킬 후보
- `wiki-ingest` — 대량 출처 일괄 ingest 전용.

## 4. 실행 요약 (재사용 체크리스트)

```bash
# 1. tool 서버 (편집·질의 백엔드)
cd mcp-wiki && pip install -e .
WIKI_ROOT=/path/to/repo python -m mcp_wiki.server

# 2. 서빙 (시각화)
python serve/build_site.py && python -m http.server -d site 8000

# 3. 스킬 (Claude에서 운영)
#   skills/wiki-keeper/ → .claude/skills/ 복사 후 /wiki-keeper
```

## 5. Conflicts / Open Questions

- 서빙 빌드를 git pre-commit 훅 또는 CI로 자동화할지(수동 재실행 vs 자동).
- 스킬이 MCP tool을 직접 호출 vs 절차 안내만 — 현재는 절차 안내 + tool 호출 가이드.
- Stack B(동적 웹앱) 전환 시 서빙 계층 교체 범위.
