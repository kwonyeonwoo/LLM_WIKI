---
title: 접근 계획 — 열람 / 학습 / 활용
status: active
date: 2026-06-11
updated: 2026-06-11
tags: [access-plan, ux, learning, mcp-wiki, roadmap]
description: 사용자가 위키 자료를 열람·학습·활용하는 세 모드를 표면 2분할(정적 사이트 + Claude+MCP)로 구현하기 위한 단계별 계획. P1 Wiki Guide 연결, P2 사이트 학습 보강, P3 Stack B 보류, 콘텐츠 보강 병행.
type: plan
---

# 접근 계획: 열람 / 학습 / 활용

Status: active (계획 확정, 구현 전)
관련 문서: [의사결정 Round 8](02-decision-rounds.md) · [에이전트 사양](04-agent-spec.md) · [하네스 & 스킬](05-harness-and-skills.md) · [PRD](03-prd.md) · [README](README.md)

이 문서는 사용자가 위키 지식을 **열람·학습·활용**하기 위한 구현 계획이다. [Round 8](02-decision-rounds.md) 결정(표면 2분할)을 단계별 작업으로 전개한다. 구현 진행 시 이 문서를 갱신한다.

## 1. 결정 요약

세 모드는 요구가 달라 한 UI에 묶지 않는다. **표면 2분할**:

| 모드 | 사용자 의도 | 표면 | 상태 |
|---|---|---|---|
| **열람** (browse) | "뭐가 있나" 훑기, 개념 관계 보기 | 정적 그래프 사이트 (`serve/`, `site/`) | 구현됨 |
| **학습** (learn) | 개념 설명, 읽는 순서, 꼬리질문 | Wiki Guide (MCP read tool + Claude) | 미연결 |
| **활용** (apply) | 작업 중 지식 인용, 새 지식 저장 | Wiki Keeper (MCP 6 tool + Claude) | 서버 구현됨, 운영 미정 |

원칙: 대화형(학습·활용)은 Claude+MCP에 위임, 시각화(열람)만 정적 사이트가 담당. 커스텀 웹앱에 채팅·추론 재구현 금지(과설계).

**갱신(2026-06-11).** 학습·활용을 **사이트 내 챗봇**으로도 연다 ([Round 9](02-decision-rounds.md)). 백엔드 없이 브라우저가 LLM API를 직접 호출하는 Wiki Guide(read-only) — provider 교체형(anthropic/openai 등), 레포는 provider 공란 배포. 이로써 MCP 클라이언트 없이도 사이트만으로 질의 가능. 키 은닉이 필요한 공개 배포는 여전히 백엔드 프록시(아래 P3/Stack B) 몫.

## 2. 단계 계획

### P1 — Wiki Guide 연결 (학습·활용 시동, 코드 0)

- **목표**: 설정만으로 학습·활용 즉시 가능하게.
- **작업**: Claude Desktop(또는 MCP 클라이언트) config에 서버 등록 — `command: python -m mcp_wiki.server`, `env.WIKI_ROOT` 지정. read-only 운영은 [04 §4](04-agent-spec.md) 정책(write tool 비노출 또는 추후 `--read-only` 플래그).
- **산출물**: 검증된 클라이언트 config 예시(README §4.3 이미 존재) + Guide 사용 가이드.
- **성공 기준**: 사용자가 자연어 질문 → Claude가 `search_wiki`→`read_page`로 위키 근거 답변 + 출처 링크 제시.
- **의존성**: 없음(서버 구현·검증 완료, [PRD §8](03-prd.md)).

### P2 — 정적 사이트 학습 보강 (열람 → 학습 격상)

읽기 전용 열람을 "학습"으로 끌어올리는 3개 기능. 작은 클라이언트 코드(`serve/template.html`).

| 기능 | 학습 가치 | 현 상태 |
|---|---|---|
| maturity 필터/색 | established↔emerging 신뢰도 기준 탐색 | 배지만 있음, 필터 없음 |
| Evidence/출처 패널 강조 | 각 주장 근거(arXiv 등) 클릭 접근 = 학습 핵심 | 본문에 묻힘 |
| 검색 → 그래프 하이라이트 | 키워드 주변 개념망 시각화 | 사이드바만 필터, 그래프 미반영 |

- **성공 기준**: maturity로 필터되고, 페이지에서 출처가 한눈에 보이며, 검색어가 그래프에 강조됨.
- **의존성**: P1과 독립. `build_site.py` 파서는 그대로, 템플릿만 확장.

### P3 — 브라우저 편집 (Stack B) — 보류

- 비-Claude 사용자용 브라우저 편집 UI. 편집은 Keeper(Claude+MCP)로 충분해 우선순위 낮음.
- 트리거: 외부 협업자가 Claude 없이 직접 편집해야 할 때 재검토.

### 병행 — 콘텐츠 보강 (선결 과제)

- 현재 도메인 분포: meta 11 / cv 4 / physical-ai 2 / intersection 1 (총 18노드, 26엣지).
- 표면 품질과 무관하게 **읽을거리가 적으면 학습 가치 낮음.** intersection·physical-ai 페이지 확충이 P1/P2와 동등하게 중요.
- 작업: Keeper 워크플로우([05 §3](05-harness-and-skills.md))로 검증 출처 기반 시드 추가.

## 3. 우선순위 근거

1. **P1 먼저** — 코드 0, 효과 최대(학습·활용 두 모드 동시 개방).
2. **콘텐츠 병행** — 표면 투자 전 읽을거리 확보가 ROI 높음.
3. **P2 다음** — 열람 표면을 학습 도구로 격상.
4. **P3 마지막** — 필요성 입증 후.

## 4. Conflicts / Open Questions

- Wiki Guide read-only 강제를 클라이언트 정책으로 둘지, 서버 `--read-only` 플래그로 코드화할지 ([04 §5](04-agent-spec.md)).
- 학습 모드에 "읽는 순서/학습 경로"(prerequisite 그래프)를 명시 메타로 넣을지 — 현재 Related 링크는 방향성 없음.
- 사이트 자동 재빌드(git hook/CI) 도입 시점 ([05 §5](05-harness-and-skills.md)).
- 콘텐츠 보강 목표 수치(예: intersection 5+, physical-ai 5+) 미확정.
