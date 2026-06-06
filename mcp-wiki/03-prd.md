---
title: PRD / 사양서 — MCP 기반 Wiki Tool
status: draft
date: 2026-06-06
tags: [prd, spec, mcp-wiki, requirements, milestones]
description: MCP 기반 컴퓨터비전/피지컬 AI wiki tool의 목표, 사용자, 기능 요구사항, MCP tool 사양, 비목표, 성공 기준, 마일스톤을 정의하는 제품 요구사항 명세서.
type: prd
---

# PRD / 사양서: MCP 기반 Wiki Tool

Status: draft
관련 문서: [지식 도메인](01-knowledge-domain.md) · [의사결정 라운드](02-decision-rounds.md) · [README](README.md) · [기존 운영 규칙](../AGENTS.md)

## 1. 목표 (Goal)

markdown-only LLM Wiki의 운영(검색·읽기·생성·갱신·점검)을 **표준 MCP tool**로 노출해, 모든 MCP 클라이언트가 일관된 인터페이스로 컴퓨터비전 / 피지컬 AI 지식베이스를 다루게 한다.

핵심: source of truth는 markdown 파일 유지. LLM 자유 편집을 정의된 tool 호출로 대체해 절차 일관성과 검증 가능성을 확보한다.

## 2. 배경 / 문제

- 기존 위키는 LLM 자율 편집 의존 → 세션마다 절차가 흔들림.
- index 갱신·링크 무결성이 수동 → 누락 발생.
- 외부 MCP 클라이언트에서 표준 호출 불가.

상세 근거: [의사결정 라운드 Round 0](02-decision-rounds.md).

## 3. 사용자 (Users)

| 사용자 | 목적 |
|---|---|
| 위키 운영자(사람) | MCP 클라이언트로 CV/Physical AI 지식 축적·질의 |
| LLM agent | tool 호출로 ingest/query/lint 수행 |
| 외부 클라이언트 | Claude Desktop 등에서 표준 MCP로 위키 접근 |

## 4. 범위 (Scope)

### In scope (MVP)
- 6개 MCP tool로 핵심 루프(검색→읽기→목록→생성→갱신→점검) 완성
- markdown 파일 기반 저장, index 자동 갱신
- CV/Physical AI 도메인 분류 메타데이터

### Out of scope (MVP 제외)
- 의미 검색(임베딩/벡터 DB) — 페이지 50개 초과 후 재검토
- 페이지 삭제 tool — 수동 git
- 다중 사용자 동시 편집/락
- 이미지 바이너리 저장·렌더링

## 5. 기능 요구사항 (Functional Requirements)

- **FR-1** 키워드로 위키 페이지 본문/제목을 검색해 매칭 페이지 목록 반환.
- **FR-2** 경로로 단일 페이지 본문(+frontmatter)을 읽어 반환.
- **FR-3** 도메인/디렉터리별 페이지 목록을 반환.
- **FR-4** 새 페이지를 템플릿 기반으로 생성하고 `index.md`에 자동 등록.
- **FR-5** 기존 페이지 본문을 갱신하고 변경 시 index 엔트리·갱신일을 반영.
- **FR-6** 끊긴 내부 링크, 색인 누락 페이지를 탐지해 리포트 반환.
- **FR-7** 모든 write 동작(FR-4/5)은 `log.md`에 append.

## 6. MCP Tool 사양 (MVP 6종)

| tool | 종류 | 입력 | 출력 | 매핑 FR |
|---|---|---|---|---|
| `search_wiki` | read | `query: str`, `domain?: str` | 매칭 페이지 경로·발췌 목록 | FR-1 |
| `read_page` | read | `path: str` | frontmatter + 본문 | FR-2 |
| `list_pages` | read | `domain?: str`, `dir?: str` | 페이지 메타 목록 | FR-3 |
| `create_page` | write | `path`, `title`, `domain`, `content` | 생성 결과 + index 반영 여부 | FR-4, FR-7 |
| `update_page` | write | `path`, `content` | 갱신 결과 + diff 요약 | FR-5, FR-7 |
| `link_check` | maintenance | (없음) | 끊긴 링크·색인 누락 리포트 | FR-6 |

각 tool은 markdown 파일을 source of truth로 직접 읽고 쓴다. 검색 인덱스는 파일에서 파생되는 재생성 가능 캐시로만 둔다([Round 2](02-decision-rounds.md)).

### tool 동작 불변조건 (Invariants)
- write tool은 `wiki/` 밖 경로를 거부한다 (경로 traversal 방지).
- `create_page`는 기존 경로 덮어쓰기를 거부한다 (덮어쓰려면 `update_page`).
- 페이지명은 소문자 kebab-case 강제 ([AGENTS.md](../AGENTS.md) 규칙 6).
- 모든 내부 링크는 상대 경로 markdown 링크 ([AGENTS.md](../AGENTS.md) 규칙 7).

## 7. 비기능 요구사항

- **결정성**: 같은 입력 → 같은 파일 변경. tool은 부수효과를 log에 남긴다.
- **투명성**: 모든 변경이 git diff로 추적 가능 (markdown only).
- **안전성**: 위험 동작(삭제, 위키 외부 쓰기) 차단. 위험 CLI 권한 모드를 기본값으로 두지 않음 ([TASK.md](../TASK.md) 가드레일).
- **이식성**: stdio transport로 모든 MCP 클라이언트와 호환.

## 8. 성공 기준 (Acceptance Criteria)

- [ ] 6개 tool이 MCP 클라이언트에서 호출되고 스키마가 노출된다.
- [ ] `create_page` 호출 시 파일 생성 + `index.md` 엔트리 + `log.md` append가 한 번에 일어난다.
- [ ] `search_wiki`가 키워드로 관련 CV/Physical AI 페이지를 반환한다.
- [ ] `link_check`가 의도적으로 심은 끊긴 링크를 탐지한다.
- [ ] 시드 페이지([01](01-knowledge-domain.md) §5) 최소 5개가 tool만으로 생성된다.
- [ ] source of truth가 markdown 파일로 유지된다 (DB 의존 없음).

## 9. 마일스톤

| 단계 | 산출물 |
|---|---|
| M1 | MCP 서버 스캐폴드 + read tool 3종 (search/read/list) |
| M2 | write tool 2종 (create/update) + index 자동 갱신 |
| M3 | `link_check` + log append + 안전 불변조건 |
| M4 | 시드 페이지 ingest, end-to-end 검증, README 확정 |

## 10. Conflicts / Open Questions

- `ingest_source`를 단일 tool로 승격할지 — M4 운영 데이터 보고 결정.
- 의미 검색 도입 시점 — 페이지 50개 기준.
- 동시 편집 락 전략 — 단일 사용자 가정으로 MVP 진행, 추후 재검토.
