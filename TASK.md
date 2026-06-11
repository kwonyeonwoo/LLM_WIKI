# TASK

Status: template (너의 첫 과제로 바꿔라)

Goal: (예) 내 자료 N건을 ingest 해 도메인 X의 첫 위키 페이지들을 만든다.

Done when:

- 처리할 자료가 `sources/`에 출처 노트로 정리됨.
- 핵심 개념이 `wiki/concepts/<domain>/`에 페이지로 생성됨.
- `index.md`·`log.md`가 갱신됨.
- `link_check` → broken/unindexed 0.
- `serve/build_site.py`로 빌드해 뷰어에서 확인됨.

Negative guardrails:

- 검증되지 않은 출처로 사실을 단정하지 않는다.
- write는 `wiki/` 밖으로 나가지 않는다. 삭제는 사람이 git으로.
- 위험 CLI 권한 모드를 기본값으로 쓰지 않는다.

Log:

- [YYYY-MM-DD] Task created from template.
