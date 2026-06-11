# Index

이 파일은 위키의 탐색 진입점이다. 질문에 답하기 전 먼저 읽고, 관련 페이지로 이동한다.

현재 지식 도메인: **(여기에 너의 도메인을 적어라)**. 도메인 분류·헤딩은 아래 `## Concepts — ...` 섹션과 `mcp-wiki/mcp_wiki/server.py`의 `_DOMAIN_HEADINGS`를 함께 바꾸면 된다. 기본값은 예시로 cv / physical-ai / intersection을 둔다.

## Core

- [Overview](wiki/overview.md): 이 위키의 현재 범위와 운영 철학.
- [Log](log.md): ingest, query, lint 작업 이력.
- [Task](TASK.md): 현재 과제 완료 조건.
- [Journal](journal.md): append-only 작업 저널.
- [Agent Instructions](AGENTS.md): LLM이 따라야 할 운영 규칙.
- [Rules](rules.md): 추가 컨텍스트·관례 (도메인 설정, 안전, 검증 게이트).
- [LLM Wiki Schema](wiki/schema/llm-wiki-schema.md): 저장소 구조와 유지보수 불변조건.

## Wiki System (meta)

- [LLM Wiki](wiki/concepts/llm-wiki.md): LLM이 유지하는 지속적 Markdown 지식베이스.
- [RAG vs LLM Wiki](wiki/concepts/rag-vs-llm-wiki.md): 검색-시점 합성과 축적형 위키의 차이.
- [Persistent Knowledge Artifact](wiki/concepts/persistent-knowledge-artifact.md): 채팅 결과를 재사용 가능한 파일로 남기는 사고방식.
- [Markdown-Only Constraint](wiki/concepts/markdown-only-constraint.md): DB, 스크립트, 플러그인 없이 운용할 때의 장단점.

## Concepts — Computer Vision

- [Example Concept](wiki/concepts/cv/example-concept.md): 예시 시드. 자기 자료로 첫 페이지를 만들면 지우거나 덮어쓴다.

## Concepts — Physical AI

_(아직 없음 — 첫 페이지를 만들면 여기 자동 등록된다.)_

## Concepts — Intersection (CV × Physical AI)

_(아직 없음)_

## Sources

- [Sources README](sources/README.md): 출처 노트 관리 방식.
- [Karpathy LLM Wiki](sources/karpathy-llm-wiki.md): Andrej Karpathy의 LLM Wiki gist 요약 (위키 시스템 출처).
- [Example Source](sources/example-source.md): 예시 출처 노트.

## Workflows

- [Ingest Workflow](wiki/workflows/ingest.md): 새 자료를 위키에 통합하는 절차.
- [Query Workflow](wiki/workflows/query.md): 위키 기반으로 질문에 답하는 절차.
- [Lint Workflow](wiki/workflows/lint.md): 위키 상태를 점검하고 정리하는 절차.
- [LLM Maintenance](wiki/workflows/maintenance.md): session start, stop, bounded loop, maintenance hook 규칙.

## Pipelines

- [Raw Item To Wiki Pages](wiki/pipelines/raw-item-to-wiki-pages.md): raw item을 source note와 wiki page로 변환하는 핵심 파이프라인.

## MCP Wiki (도구 + 설계 문서)

- [MCP Wiki README](mcp-wiki/README.md): MCP 서버 + 뷰어 사용법.
- [지식 도메인 정의](mcp-wiki/01-knowledge-domain.md)
- [의사결정 라운드](mcp-wiki/02-decision-rounds.md)
- [PRD / 사양서](mcp-wiki/03-prd.md)
- [에이전트 사양](mcp-wiki/04-agent-spec.md)
- [하네스 & 스킬](mcp-wiki/05-harness-and-skills.md)
- [접근 계획](mcp-wiki/06-access-plan.md)

## Templates

- [Page Template](templates/page.md): 일반 위키 페이지 양식.
- [Source Note Template](templates/source-note.md): 출처 노트 양식.
- [Query Result Template](templates/query-result.md): 재사용 가능한 질의 결과 양식.
- [Lint Report Template](templates/lint-report.md): 점검 보고서 양식.

## Open Questions

- (여기에 너의 위키에서 미해결인 질문을 남긴다.)
