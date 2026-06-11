---
title: 의사결정 라운드 기록 (Agent Decision Log)
status: active
date: 2026-06-06
updated: 2026-06-11
tags: [decision-log, mcp-wiki, architecture, agent-rounds]
description: markdown-only LLM Wiki를 MCP 기반 wiki tool로 전환하기까지 사용자와 agent가 거친 의사결정 라운드를 스택, 저장 백엔드, tool 표면, 도메인 전환, 무결성 책임 순으로 기록한 결정 로그.
type: decision-log
---

# 의사결정 라운드 기록 (Agent Decision Log)

Status: active (Round 0~7, append 중)
형식: 라운드별 [질문 → 옵션 → tradeoff → 결정 → 근거]
관련 문서: [지식 도메인](01-knowledge-domain.md) · [PRD](03-prd.md) · [README](README.md)

이 문서는 markdown-only LLM Wiki를 **MCP 기반 wiki tool**로 전환하기로 결정하기까지, 사용자와 agent가 거친 의사결정 라운드를 기록한다. 덮어쓰지 않고 append하며, 결정이 번복되면 새 라운드로 남긴다.

---

## Round 0 — 문제 정의

**상황.** 기존 저장소는 markdown 파일만으로 동작하는 LLM Wiki다. ingest/query/lint를 사람이 LLM에게 자연어로 지시하고, LLM이 파일을 직접 편집한다.

**한계.**
- 동작이 LLM의 자율 편집에 의존 → 절차 일관성이 매 세션 흔들림
- 링크 무결성·색인 갱신이 수동 → 누락 발생
- 다른 MCP 클라이언트(Claude Desktop 등)에서 표준 인터페이스로 호출 불가

**결정.** 위키 운영을 **구조화된 MCP tool**로 노출한다. LLM이 자유 편집하는 대신, 정해진 tool(`create_page`, `search`, `link_check` 등)을 호출하게 한다.

근거: tool 경계가 절차를 강제 → 일관성↑, 검증 가능성↑.

---

## Round 1 — 구현 스택

**질문.** MCP 서버를 무엇으로 구현하나?

| 옵션 | 장점 | 단점 |
|---|---|---|
| A. Python + 공식 MCP SDK | SDK 성숙, CV 생태계(numpy 등) 친화 | 배포 시 런타임 의존 |
| B. TypeScript + MCP SDK | Claude Desktop 예제 풍부, 단일 바이너리화 쉬움 | CV 도메인 라이브러리 약함 |
| C. 기존 markdown 유지, tool 없음 | 추가 작업 0 | Round 0 문제 미해결 |

**결정. A — Python + 공식 MCP SDK (`mcp` 패키지).**

근거: 도메인이 CV/Physical AI라 추후 임베딩 검색·이미지 메타 처리 확장 시 Python 생태계가 유리. C는 문제를 해결 못 해 탈락.

---

## Round 2 — 저장 백엔드

**질문.** 위키 데이터를 어디에 저장하나?

| 옵션 | 장점 | 단점 |
|---|---|---|
| A. 기존 markdown 파일 그대로 | 투명·git 친화·기존 자산 재사용 | 쿼리 성능 한계 |
| B. SQLite + markdown 본문 | 메타데이터 쿼리 빠름 | 이중 관리, git diff 약화 |
| C. 벡터 DB | 의미 검색 강력 | 무거움, markdown-only 철학 위배 |

**결정. A를 1차로 채택. 검색 인덱스는 파일에서 파생되는 캐시로만 둔다.**

근거: 기존 [markdown-only-constraint](../wiki/concepts/markdown-only-constraint.md) 철학 유지. source of truth는 항상 markdown 파일. 인덱스(B/C 요소)는 재생성 가능한 부산물로 한정 → 데이터 정합성 단일화.

---

## Round 3 — Tool 표면(surface) 범위

**질문.** 어떤 tool을 노출하나? 너무 많으면 LLM이 오용, 너무 적으면 무력.

검토한 후보: `create_page`, `update_page`, `read_page`, `search_wiki`, `list_pages`, `link_check`, `ingest_source`, `update_index`, `delete_page`.

**결정. MVP는 6개로 제한.**
- `search_wiki`, `read_page`, `list_pages` (read)
- `create_page`, `update_page` (write)
- `link_check` (maintenance)

보류: `ingest_source`(복합 동작 → write tool 조합으로 우선 대체), `delete_page`(위험, 수동 git로), `update_index`(create/update에 자동 포함).

근거: 단순성 우선. 최소 tool로 핵심 루프(검색→읽기→쓰기→점검) 완성. 검증 후 확장.

---

## Round 4 — 지식 도메인 전환

**질문.** 기존 "Agentic Coding Basics" 콘텐츠를 유지하나, 새 도메인으로 가나?

**결정. 컴퓨터비전 / 피지컬 AI로 전환.** 상세는 [01-knowledge-domain.md](01-knowledge-domain.md).

근거: 사용자 요구. 기존 운영 메커니즘(AGENTS.md)은 도메인 독립적이므로 그대로 재사용, 콘텐츠 축만 교체.

**번복 기록(2026-06-11).** 최초엔 ACB 페이지를 archive로 보존하려 했으나, 사용자 지시("지식도메인 내용으로 채워줘 + 검증출처만")에 따라 ACB 도메인 콘텐츠 20개를 `git rm`으로 삭제하고 CV/Physical AI 콘텐츠로 교체. 운영 메커니즘 메타 페이지(llm-wiki, rag-vs-llm-wiki, markdown-only-constraint 등)는 보존. → "보존"이 아니라 "교체(삭제)"가 실제 결정.

---

## Round 5 — 인덱스/링크 무결성 책임 주체

**질문.** index.md 갱신과 링크 검사를 누가 하나?

| 옵션 | 설명 |
|---|---|
| A. LLM이 매번 수동 | 기존 방식, 누락 위험 |
| B. tool이 자동 강제 | create/update 시 index 자동 반영, link_check tool 제공 |

**결정. B.** `create_page`/`update_page`가 index 엔트리를 자동 갱신하고, `link_check`로 끊긴 링크를 탐지한다.

근거: Round 0의 "수동 누락" 문제 직접 해결. 절차를 코드로 강제.

---

## Round 6 — 시각화 / 서빙 방식 (2026-06-11)

**질문.** wiki page를 어떻게 시각화·서빙하나? MCP tool은 데이터/로직 계층이고, 사람이 보는 표현 계층이 별도로 필요.

| 옵션 | 장점 | 단점 |
|---|---|---|
| A. 정적 사이트 (빌드 시 markdown→HTML+JSON) | 의존성 0, GitHub Pages 배포, 빌드가 파서 로직 실증 | 실시간 편집 인터랙션 약함 |
| B. 동적 웹앱 (서버 렌더 + 편집 UI) | 편집·검색 인터랙션 강함 | 런타임 서버 필요, 복잡 |

**결정. A 먼저 구현, 필요 시 B 이어서.**

근거: MCP 서버 = 데이터/로직, 웹앱 = 표현. 둘이 같은 markdown(source of truth) 공유. 정적 사이트는 stdlib만으로 그래프(노드=페이지, 엣지=Related)·페이지·검색 제공 → markdown-only 철학과 일치, 배포 단순. 산출: `serve/build_site.py` + `template.html` → `site/data.json`+`index.html`. 클라이언트는 CDN d3+marked.

---

## Round 7 — 에이전트 역할 분리 (2026-06-11)

**질문.** 위키를 다루는 에이전트를 단일로 둘지, 권한별로 나눌지?

**결정. 두 역할로 분리** — Wiki Guide(read-only 챗봇), Wiki Keeper(편집·ingest). 상세 [04-agent-spec.md](04-agent-spec.md).

근거: 최소 권한 원칙. 질의응답은 write tool이 필요 없음 → read-only allowlist로 사고 차단. 현재 서버는 단일 프로세스 6 tool 제공, 역할 강제는 클라이언트 정책 또는 추후 `--read-only` 플래그.

---

## Round 8 — 사용자 접근 표면: 열람 / 학습 / 활용 (2026-06-11)

**질문.** 사용자가 위키 자료를 열람·학습·활용하려면 어떤 방식으로 구현하나? 세 모드를 한 UI에 다 넣나, 표면을 나누나?

**핵심 관찰.** 세 모드는 요구가 다름:
- 열람(browse) = "뭐가 있나" 훑기·관계 보기 → 시각화가 답.
- 학습(learn) = 개념 설명·읽는 순서·꼬리질문 → 대화형.
- 활용(apply) = 작업 중 지식 인용·새 지식 저장 → 대화형 + 쓰기.

학습·활용의 대화 엔진(Claude)과 지식 접근(MCP tool)은 **이미 존재**. 그래프 UI에 채팅·추론을 새로 박는 건 중복 투자.

| 옵션 | 설명 | 평가 |
|---|---|---|
| A. 단일 커스텀 웹앱에 열람+편집+채팅 전부 | 통합 UX | 과설계. 대화 엔진 재구현 = 낭비 |
| B. 표면 2분할 — 정적 사이트(열람) + Claude+MCP(학습·활용) | 기존 자산 재사용, 코드 최소 | 채택 |

**결정. B — 표면 2분할.** 우선순위:
1. **P1** Wiki Guide(MCP read-only) Claude Desktop 연결 — 설정만, 코드 0. 학습·활용 즉시 가능.
2. **P2** 정적 사이트 학습 보강 — maturity 필터, Evidence/출처 패널, 검색→그래프 하이라이트.
3. **P3** 브라우저 편집(Stack B) — 보류. 편집은 Keeper로 충분.
4. **병행** 콘텐츠 보강 — 현재 meta:11 vs 실지식:7 쏠림. 표면보다 읽을거리 확보가 선결.

근거: 최소 추가 코드로 세 모드 모두 커버. 대화형(학습·활용)은 Claude+MCP에 위임, 시각화(열람)만 정적 사이트가 담당. 상세 단계 계획 [06-access-plan.md](06-access-plan.md).

---

## 현재까지 합의 요약

- 스택: Python + 공식 MCP SDK
- 저장: markdown 파일 = source of truth, 인덱스는 파생 캐시
- Tool MVP 6종: search/read/list + create/update + link_check
- 도메인: CV / Physical AI (intersection 우선), ACB 콘텐츠는 삭제·교체
- index·링크 무결성: tool이 자동 강제
- 시각화: 정적 사이트(Stack A) 구현, 동적 웹앱(Stack B) 보류
- 에이전트: Wiki Guide(read) / Wiki Keeper(write) 2역할 분리
- 접근 표면: 2분할 — 정적 사이트(열람) + Claude+MCP(학습·활용). P1 Guide 연결 우선 ([Round 8](#round-8--사용자-접근-표면-열람--학습--활용-2026-06-11))

## Open Questions (다음 라운드 후보)

- 의미 검색(임베딩)을 언제 도입하나? → 페이지 50개 초과 시 재검토.
- `ingest_source`를 단일 tool로 승격할지 → MVP 운영 데이터 보고 결정.
- 다중 사용자/동시 편집 시 파일 락 전략 미정.
