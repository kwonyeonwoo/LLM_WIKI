# Rules — 추가 컨텍스트

[AGENTS.md](AGENTS.md)의 운영 규칙을 보완하는 관례·가드레일이다. agent와 사용자 모두 이 위키를 다룰 때 따른다.

## 도메인 설정

- 분류는 `mcp-wiki/mcp_wiki/server.py`의 `_DOMAIN_HEADINGS`와 `index.md`의 `## Concepts — ...` 헤딩 **두 곳이 문자열로 일치**해야 `create_page` 자동 등록이 작동한다. 한쪽만 바꾸면 페이지가 `## Uncategorized`로 떨어진다.
- 모든 개념 페이지는 제목 바로 아래 `Domain: <키> · Maturity: <established|emerging|speculative>` 한 줄을 둔다. 뷰어의 노드 색·필터가 이 줄을 파싱한다.

## 콘텐츠 규칙

- **출처 분리**: raw 원문/노트는 `sources/`, 통합 지식은 `wiki/`. 섞지 않는다.
- **검증 출처만**: 사실 주장은 arXiv abs, 공식 릴리스, peer-reviewed 등 검증 가능한 출처에서. 출처 불명 주장 금지.
- **모순은 보존**: 충돌하는 정보는 덮어쓰지 말고 페이지의 `Conflicts / Open Questions`에 남긴다.
- **kebab-case**: 페이지 파일명은 소문자 kebab-case (`my-concept.md`).
- **상대 링크**: 내부 링크는 상대 경로 Markdown 링크. (이 레포는 GitHub에서 렌더되므로 `[[wikilinks]]` 쓰지 않는다.)

## 안전 가드레일

- write tool은 `wiki/` 밖 경로를 거부한다 (경로 traversal 방지).
- `create_page`는 덮어쓰기 금지 → 기존 페이지는 `update_page`.
- 페이지 삭제 권한 없음. 삭제는 사람이 git으로.
- 위험 CLI 권한 모드(bypass 등)를 기본값으로 쓰지 않는다.
- 같은 페이지를 새 근거 없이 반복 재작성하지 않는다. 3회 시도 후 미해결이면 `TASK.md`에 blocker로 남기고 중단.

## 검증 게이트 (작업 종료 전)

1. `link_check` → `broken_links` / `unindexed_pages` 둘 다 0.
2. `index.md`에 새/변경 페이지 반영 확인.
3. `log.md`에 write 동작 기록.
4. (선택) `serve/build_site.py` 재실행 → 뷰어 최신화.

git hook([hooks/pre-commit](hooks/pre-commit))을 설치하면 1번이 커밋 시 자동 강제된다: `git config core.hooksPath hooks`.
