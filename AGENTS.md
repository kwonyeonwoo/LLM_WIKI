# LLM Wiki Agent Instructions

이 저장소는 markdown-only LLM Wiki다. 목적은 원문 자료를 매번 새로 검색하거나 요약하는 대신, LLM이 읽은 내용을 지속적으로 갱신되는 Markdown 위키로 축적하는 것이다.

## 역할

- 사용자는 자료 선택, 질문, 방향 설정을 담당한다.
- LLM은 원문을 읽고, 관련 위키 페이지를 생성하거나 갱신하고, 링크와 색인과 로그를 유지한다.
- 원문과 위키를 섞지 않는다. 출처는 `sources/`, 통합된 지식은 `wiki/`에 둔다.

## 기본 구조

- `README.md`: 이 위키의 사용법.
- `index.md`: 전체 페이지 색인. 질문에 답하기 전 먼저 읽는다.
- `log.md`: 변경 이력. ingest, query, lint 작업 후 append-only로 남긴다.
- `TASK.md`: 현재 작업의 완료 조건과 가드레일.
- `journal.md`: 세션별 작업 기록. append-only로 유지한다.
- `sources/`: 원문 또는 원문에서 추출한 Markdown 노트.
- `inbox/`: 아직 처리하지 않은 Markdown 자료.
- `wiki/`: LLM이 유지하는 지식 페이지.
- `wiki/schema/`: 이 저장소의 운영 스키마.
- `wiki/pipelines/`: raw item을 wiki page로 바꾸는 파이프라인.
- `templates/`: 새 페이지를 만들 때 쓰는 Markdown 양식.

## 운영 원칙

1. 모든 파일은 Markdown으로 유지한다.
2. 새 자료를 처리할 때는 `sources/`에 출처 노트를 만들고, 관련 `wiki/` 페이지를 갱신한다.
3. 사실 주장에는 가능한 한 출처 링크나 source note 링크를 붙인다.
4. 모순되는 정보가 있으면 덮어쓰지 말고 `Conflicts / Open Questions` 섹션에 남긴다.
5. 새로운 개념이 반복해서 등장하면 별도 페이지를 만든다.
6. 페이지 이름은 소문자 kebab-case를 사용한다. 예: `rag-vs-llm-wiki.md`.
7. 내부 링크는 상대 경로 Markdown 링크를 사용한다.
8. 작업이 끝나면 `index.md`, `log.md`, `journal.md`를 갱신한다.
9. 현재 작업의 완료 조건은 `TASK.md`를 기준으로 판단한다.

## 작업 방식

### Ingest

새 자료가 들어오면:

1. [Raw Item To Wiki Pages Pipeline](wiki/pipelines/raw-item-to-wiki-pages.md)을 따른다.
2. 자료를 읽고 `sources/`에 출처 노트를 만든다.
3. 핵심 개념, 인물, 시스템, 주장, 반론을 추출한다.
4. 이미 있는 관련 페이지를 갱신한다.
5. 필요한 새 페이지를 만든다.
6. `index.md`에 새 페이지나 변경된 페이지를 반영한다.
7. `log.md`와 `journal.md`에 처리 기록을 추가한다.

### Query

질문에 답할 때:

1. `index.md`를 먼저 읽는다.
2. 관련 `wiki/` 페이지와 `sources/` 노트를 읽는다.
3. 출처를 명시해 답한다.
4. 답변이 재사용 가치가 있으면 `wiki/`에 새 분석 페이지로 저장할지 제안하거나 저장한다.

### Lint

정기적으로 다음을 점검한다:

- 끊긴 내부 링크
- 색인에 없는 페이지
- 출처 없는 강한 주장
- 서로 충돌하는 내용
- 오래된 설명
- 너무 길어진 페이지
- 반복되는 개념인데 독립 페이지가 없는 항목

### Maintenance

세션 시작 시:

1. `AGENTS.md`, `index.md`, `TASK.md`, `journal.md`를 읽는다.
2. 이번 요청이 ingest, query, lint, packaging 중 무엇인지 분류한다.
3. 필요한 source note와 wiki page를 먼저 찾는다.

세션 종료 전:

1. `index.md`에 새 파일이 반영됐는지 확인한다.
2. `log.md`와 `journal.md`를 append한다.
3. 남은 일이 있으면 `TASK.md`에 남긴다.
4. `link_check`로 끊긴 링크·색인 누락이 0인지 점검한다.

## 문체

- 간결하고 검증 가능하게 쓴다.
- 칭찬이나 과장보다 한계와 근거를 우선한다.
- 요약은 짧게, 연결과 반론은 명확하게 쓴다.
