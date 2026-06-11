# Log

Append-only 작업 기록이다. 새 ingest, query, lint 작업이 끝나면 최신 항목을 위에 추가한다. `create_page`/`update_page` tool은 여기 자동으로 한 줄 append 한다.

## [YYYY-MM-DD] setup | LLM Wiki template initialized

- 템플릿을 clone 해 빈 위키로 시작.
- 첫 자료를 `inbox/`에 넣고 ingest 하면 여기에 기록이 쌓인다.
