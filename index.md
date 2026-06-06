# Index

이 파일은 위키의 탐색 진입점이다. 질문에 답하기 전 먼저 읽고, 관련 페이지로 이동한다.

## Core

- [Overview](wiki/overview.md): 이 위키의 현재 범위와 운영 철학.
- [Log](log.md): ingest, query, lint 작업 이력.
- [Task](TASK.md): 현재 과제 완료 조건.
- [Journal](journal.md): append-only 작업 저널.
- [Agent Instructions](AGENTS.md): LLM이 따라야 할 운영 규칙.
- [LLM Wiki Schema](wiki/schema/llm-wiki-schema.md): 저장소 구조와 유지보수 불변조건.

## Sources

- [Sources README](sources/README.md): 출처 노트 관리 방식.
- [Karpathy LLM Wiki](sources/karpathy-llm-wiki.md): Andrej Karpathy의 LLM Wiki gist 요약과 메타데이터.
- [Agentic Coding Basics Source Pack](sources/agentic-coding-basics/README.md): 과제 첨부 PDF 9개를 Markdown source note로 변환한 묶음.
- [ACB-01 Vibe Coding And Agent Coding](sources/agentic-coding-basics/01-vibe-coding-and-agent-coding.md)
- [ACB-02 SDLC Pipeline In Vibe Coding](sources/agentic-coding-basics/02-sdlc-pipeline-in-vibe-coding.md)
- [ACB-03 Agents Subprocess Calling](sources/agentic-coding-basics/03-agents-subprocess-calling.md)
- [ACB-04 Plan Mode Sequential And Parallel Agents](sources/agentic-coding-basics/04-plan-mode-sequential-and-parallel-agents.md)
- [ACB-05 Agent Specifications](sources/agentic-coding-basics/05-agent-specifications.md)
- [ACB-06 Agent Pool And Orchestrator](sources/agentic-coding-basics/06-agent-pool-and-orchestrator.md)
- [ACB-07 Harness And Skills](sources/agentic-coding-basics/07-harness-and-skills.md)
- [ACB-08 Model Context Protocol](sources/agentic-coding-basics/08-model-context-protocol.md)
- [ACB-09 Loop And Hooks](sources/agentic-coding-basics/09-loop-and-hooks.md)

## Concepts

- [LLM Wiki](wiki/concepts/llm-wiki.md): LLM이 유지하는 지속적 Markdown 지식베이스.
- [RAG vs LLM Wiki](wiki/concepts/rag-vs-llm-wiki.md): 검색-시점 합성과 축적형 위키의 차이.
- [Persistent Knowledge Artifact](wiki/concepts/persistent-knowledge-artifact.md): 채팅 결과를 재사용 가능한 파일로 남기는 사고방식.
- [Markdown-Only Constraint](wiki/concepts/markdown-only-constraint.md): DB, 스크립트, 플러그인 없이 운용할 때의 장단점.
- [Agentic Coding](wiki/concepts/agentic-coding.md): 역할, 핸드오프, 검증을 갖춘 AI 코딩 방식.
- [SDLC And Spec-Driven Development](wiki/concepts/sdlc-and-spec-driven-development.md): PRD, SRS, AC 중심의 AI-assisted 개발 구조.
- [Agent Subprocess Calling](wiki/concepts/agent-subprocess-calling.md): CLI agent를 subprocess로 다루는 방식.
- [Plan Mode](wiki/concepts/plan-mode.md): read-only 계획 단계와 handoff 문서.
- [Agent Specification](wiki/concepts/agent-specification.md): agent role, input, output, constraint 구조.
- [Agent Pool And Orchestrator](wiki/concepts/agent-pool-and-orchestrator.md): agent pool과 orchestrator 모델.
- [Harness Engineering](wiki/concepts/harness-engineering.md): contract, procedure, journal, preference 기반 실행 구조.
- [Model Context Protocol](wiki/concepts/model-context-protocol.md): agent-tool 표준 연결 방식과 tradeoff.
- [Loop And Hooks](wiki/concepts/loop-and-hooks.md): agent lifecycle event와 deterministic checks.

## Workflows

- [Ingest Workflow](wiki/workflows/ingest.md): 새 자료를 위키에 통합하는 절차.
- [Query Workflow](wiki/workflows/query.md): 위키 기반으로 질문에 답하는 절차.
- [Lint Workflow](wiki/workflows/lint.md): 위키 상태를 점검하고 정리하는 절차.
- [LLM Maintenance](wiki/workflows/maintenance.md): session start, stop, bounded loop, maintenance hook 규칙.

## Pipelines

- [Raw Item To Wiki Pages](wiki/pipelines/raw-item-to-wiki-pages.md): raw item을 source note와 wiki page로 변환하는 제출 핵심 파이프라인.

## Analyses

- [Agentic Coding Basics Synthesis](wiki/analyses/agentic-coding-basics-synthesis.md): 강의자료를 LLM Wiki 구성요소로 매핑한 종합 분석.

## Templates

- [Page Template](templates/page.md): 일반 위키 페이지 양식.
- [Source Note Template](templates/source-note.md): 출처 노트 양식.
- [Query Result Template](templates/query-result.md): 재사용 가능한 질의 결과 양식.
- [Lint Report Template](templates/lint-report.md): 점검 보고서 양식.

## Open Questions

- 제출 후 실제 수업 기준에 맞춰 원본 PDF 포함 여부가 필요한지 확인해야 한다.
- Markdown-only 절차가 커졌을 때 자동 링크 검사 도구를 추가할지 결정해야 한다.
