# Markdown-Only LLM Wiki

이 폴더는 Andrej Karpathy가 제안한 LLM Wiki 패턴을 Markdown 파일만으로 구현한 개인 지식베이스다.

현재 버전은 과제 제출용 초기 저장소다. Karpathy의 LLM Wiki 아이디어를 조사한 뒤, `Agentic_Coding_Basics.zip` 강의자료를 raw source로 삼아 source note, wiki page, schema, maintenance workflow, raw-to-wiki pipeline을 구성했다.

핵심 아이디어는 단순하다. 자료를 질문할 때마다 다시 검색하고 요약하는 대신, LLM이 자료를 읽은 뒤 지속적으로 갱신되는 위키 페이지로 정리한다. 이렇게 하면 요약, 링크, 비교, 반론, 미해결 질문이 채팅창에 사라지지 않고 파일로 축적된다.

## 빠른 사용법

1. 새 자료를 `inbox/`에 Markdown으로 넣는다.
2. LLM에게 "`inbox/파일명.md`를 ingest 해줘"라고 요청한다.
3. LLM은 `sources/`에 출처 노트를 만들고 `wiki/` 페이지를 갱신한다.
4. 질문할 때는 "`index.md`를 먼저 보고 이 위키 기준으로 답해줘"라고 요청한다.
5. 가끔 "lint 해줘"라고 요청해 끊긴 링크, 오래된 주장, 누락된 출처를 점검한다.

## 폴더 구조

- [AGENTS.md](AGENTS.md): LLM이 이 위키를 관리하는 규칙.
- [index.md](index.md): 전체 색인.
- [log.md](log.md): 작업 기록.
- [TASK.md](TASK.md): 현재 과제의 완료 조건.
- [journal.md](journal.md): append-only 작업 저널.
- [inbox/](inbox/README.md): 아직 처리하지 않은 자료.
- [sources/](sources/README.md): 원문 또는 원문 기반 출처 노트.
- [wiki/](wiki/overview.md): 축적된 지식 페이지.
- [templates/](templates/page.md): 새 문서를 만들 때 쓰는 양식.

## 현재 시작점

이 위키는 Karpathy의 LLM Wiki gist를 첫 자료로 삼아 시작한다.

- [Source: Karpathy LLM Wiki](sources/karpathy-llm-wiki.md)
- [Source Pack: Agentic Coding Basics](sources/agentic-coding-basics/README.md)
- [Concept: LLM Wiki](wiki/concepts/llm-wiki.md)
- [Concept: RAG vs LLM Wiki](wiki/concepts/rag-vs-llm-wiki.md)
- [Concept: Agentic Coding](wiki/concepts/agentic-coding.md)
- [Schema: LLM Wiki Schema](wiki/schema/llm-wiki-schema.md)
- [Pipeline: Raw Item To Wiki Pages](wiki/pipelines/raw-item-to-wiki-pages.md)
- [Workflow: Ingest](wiki/workflows/ingest.md)
- [Workflow: Query](wiki/workflows/query.md)
- [Workflow: Lint](wiki/workflows/lint.md)
- [Workflow: LLM Maintenance](wiki/workflows/maintenance.md)

## 과제 제출물

제출용 압축파일은 `submissions/` 아래에 생성한다. 압축 대상은 Markdown source files이며 `.git/`, `.work/`, 원본 PDF 임시 추출물은 제외한다.

## 중요한 한계

Markdown-only 구조는 가볍고 투명하지만 자동 정합성 보장은 약하다. 링크 무결성, 최신성, 중복, 출처 누락은 LLM과 사용자가 주기적으로 점검해야 한다. 기업용 지식관리나 권한 관리가 필요한 환경에서는 별도의 검색, DB, 승인 흐름이 필요할 수 있다.
