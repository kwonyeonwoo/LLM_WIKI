---
title: 에이전트 사양 — Wiki Keeper / Wiki Guide
status: active
date: 2026-06-06
updated: 2026-06-11
tags: [agent-spec, permissions, roles, mcp-wiki, governance]
description: MCP 기반 CV/Physical AI wiki를 편집하거나 질의응답하는 두 에이전트(Wiki Keeper 편집자, Wiki Guide 챗봇)의 역할, 권한, 허용 기능, 가드레일, 에스컬레이션을 정의하는 사양 문서.
type: agent-spec
---

# 에이전트 사양: Wiki Keeper / Wiki Guide

Status: active ([Round 7](02-decision-rounds.md)에서 2역할 분리 확정)
관련 문서: [PRD](03-prd.md) · [README](README.md) · [하네스 & 스킬](05-harness-and-skills.md) · [운영 규칙](../AGENTS.md)

이 위키를 다루는 에이전트는 **두 역할**로 나뉜다. 권한을 분리해 "읽기만 하면 되는 작업"이 쓰기 권한을 갖지 않게 한다(최소 권한 원칙).

| 에이전트 | 역할 | 허용 tool | 쓰기 권한 | 삭제 |
|---|---|---|---|---|
| **Wiki Guide** | 질의응답 챗봇 (read-only) | `search_wiki`, `read_page`, `list_pages` | 없음 | 없음 |
| **Wiki Keeper** | 편집·ingest·유지보수 | 6 tool 전체 (read 3 + `create_page`, `update_page`, `link_check`) | `wiki/` 내부만 | 없음 (사람이 git) |

요약: **Guide = 읽고 답한다, Keeper = 쓰고 점검한다.** 둘 다 페이지 삭제 권한은 없음(사람 승인 사항). 상세는 아래 각 절.

---

## 1. Wiki Guide (챗봇 / read-only)

### 역할
사용자 질문에 **위키 내용을 근거로** 답한다. 위키 밖 지식으로 답할 때는 출처 없음을 명시한다.

### 허용 기능 (tool allowlist)
- `search_wiki` ✅
- `read_page` ✅
- `list_pages` ✅
- `create_page` / `update_page` / `link_check` ❌

### 입력 / 출력
- 입력: 자연어 질문.
- 출력: 답변 + 인용한 페이지 경로(상대 링크). 근거 없으면 "위키에 없음" 명시.

### 가드레일
- 파일을 쓰지 않는다. 어떤 경우에도 write tool 호출 금지.
- 추측을 사실처럼 단정하지 않는다. 위키에 없으면 없다고 한다.
- 재사용 가치 있는 답이면 "Wiki Keeper로 저장할까요?"를 제안만 한다(직접 저장 X).

---

## 2. Wiki Keeper (편집자)

### 역할
새 자료 ingest, 페이지 생성·갱신, 무결성 점검을 수행한다. [Ingest 워크플로우](../wiki/workflows/ingest.md)와 [Raw→Wiki 파이프라인](../wiki/pipelines/raw-item-to-wiki-pages.md)을 따른다.

### 허용 기능 (tool allowlist)
- `search_wiki`, `read_page`, `list_pages` ✅ (쓰기 전 항상 먼저 확인)
- `create_page` ✅ — 신규 페이지
- `update_page` ✅ — 기존 페이지
- `link_check` ✅ — 작업 후 점검

### 입력 / 출력
- 입력: 새 출처(URL/텍스트), 또는 편집 지시.
- 출력: 생성·갱신된 페이지 경로, index/log 반영 결과, link_check 리포트.

### 권한 경계 (불변조건 — tool이 강제)
1. 쓰기는 `wiki/` 내부만. 밖 경로 거부.
2. 페이지명 kebab-case 강제.
3. `create_page`는 덮어쓰기 금지 → 기존 페이지는 `update_page`.
4. 삭제 권한 **없음**. 페이지 삭제는 사람이 git으로 수행([PRD §4 Out of scope](03-prd.md)).
5. `index.md`·`log.md` 갱신은 tool이 자동 수행 → 수동 직접 편집 지양.

### 작업 절차 (필수 순서)
1. `search_wiki` / `list_pages`로 기존 페이지 확인 (중복 방지).
2. 출처는 `sources/`에 source note로 먼저 정리.
3. 개념 페이지를 `create_page`(신규) 또는 `update_page`(기존)로 작성.
4. 사실 주장에는 출처 링크(상대 경로) 부착.
5. 모순은 덮어쓰지 말고 `Conflicts / Open Questions`에 기록.
6. 작업 후 `link_check` 실행 → 끊긴 링크·색인 누락 0 확인.

### 가드레일
- 검증된 출처에서만 사실을 가져온다(arXiv, 공식 릴리스, peer-reviewed). 출처 불명 주장 금지.
- 같은 페이지를 새 근거 없이 반복 재작성하지 않는다. 3회 시도 후 미해결이면 `TASK.md`에 blocker 기록하고 중단([Bounded Loop](../wiki/workflows/maintenance.md)).
- 위험 CLI 권한 모드를 기본값으로 쓰지 않는다([TASK.md](../TASK.md) 가드레일).

---

## 3. 공통 원칙

- **출처 분리**: 원문 = `sources/`, 통합 지식 = `wiki/`. 섞지 않는다.
- **결정성**: 모든 쓰기는 `log.md`에 흔적을 남긴다.
- **최소 권한**: 읽기 작업에 쓰기 에이전트를 쓰지 않는다.
- **사람 승인 지점**: 페이지 삭제, 도메인 전환, 대량 재작성은 사람이 결정.

## 4. 클라이언트 설정과 권한 매핑

MCP 클라이언트가 어떤 tool을 노출하느냐로 역할을 강제한다.
- Wiki Guide 세션: 서버를 read-only 모드로 띄우거나, 클라이언트에서 write tool을 비활성화.
- Wiki Keeper 세션: 6 tool 전체 노출.

(현재 서버는 단일 프로세스로 6 tool 모두 제공. 역할 분리는 클라이언트 정책 또는 추후 `--read-only` 플래그로 강제 — [Open Questions](#5-conflicts--open-questions).)

### Wiki Guide의 또 다른 표면 — 사이트 챗봇

정적 사이트(`serve/`)의 **챗봇** 탭이 Wiki Guide를 브라우저에서 구현한다. **read-only**다 — 파일을 쓸 수단이 없고, 위키를 검색해 context로 넣어 답할 뿐이다. **API 키를 쓰지 않는다**: 로컬 브리지(`serve/guide_bridge.py`)가 `claude -p`(로그인된 구독, 무키)로 답을 만든다. 설정은 [README §4.6](README.md). 즉 Guide는 세 경로로 쓸 수 있다: (1) MCP 클라이언트(Claude Desktop)의 read tool, (2) `/wiki-guide` 스킬, (3) 사이트 챗봇(로컬 브리지). 모두 키 불필요.

## 5. Conflicts / Open Questions

- 서버에 `--read-only` 플래그를 추가해 Wiki Guide를 프로세스 수준에서 강제할지.
- 다중 사용자 시 동시 쓰기 충돌 처리(파일 락) 미정.
- 챗봇이 답변을 자동으로 분석 페이지로 저장하는 자동화 수준의 경계.
