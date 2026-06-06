---
name: wiki-keeper
description: CV/Physical AI LLM Wiki를 편집·유지보수·서빙하는 스킬. 새 출처를 ingest해 검증된 개념 페이지를 만들고(create_page/update_page), 링크 무결성을 점검(link_check)하고, 정적 사이트를 빌드한다. 트리거 — "위키에 추가", "ingest", "위키 페이지 만들어", "링크 점검", "사이트 빌드", "/wiki-keeper".
---

# Wiki Keeper

이 스킬은 [Wiki Keeper 에이전트 사양](../../04-agent-spec.md)을 실행하는 진입점이다. MCP 서버(`cv-physical-ai-wiki`)의 tool과 정적 사이트 빌더를 정해진 순서로 사용한다.

## 전제

- MCP 서버 `cv-physical-ai-wiki`가 클라이언트에 연결돼 있어야 한다(6 tool 노출). 설치: [README §4](../../README.md).
- `WIKI_ROOT`는 저장소 루트(`index.md`가 있는 폴더)를 가리킨다.

## 권한 (이 스킬이 지키는 경계)

- 쓰기는 `wiki/` 내부만. 페이지명 kebab-case. `create_page`는 덮어쓰기 금지.
- 페이지 **삭제 금지** — 사람이 git으로 수행.
- 검증된 출처(arXiv, 공식 릴리스, peer-reviewed)에서만 사실 인용.
- 같은 페이지를 새 근거 없이 3회 이상 재작성하지 않는다 → `TASK.md`에 blocker 기록 후 중단.

## 절차

### A. 새 자료 ingest
1. `list_pages` / `search_wiki`로 **기존 페이지 중복 확인**.
2. 출처를 읽고 검증 → `sources/<주제>/`에 source note 작성(메타데이터 + key claims + URL).
3. 개념 페이지를 작성:
   - 신규: `create_page(path="wiki/concepts/<domain>/<slug>.md", title=..., domain=..., content=...)`
   - 기존: `update_page(path=..., content=...)`
   - 페이지는 `# Title` + `Domain: <cv|physical-ai|intersection> · Maturity: <established|emerging|speculative>` + `## Definition / Key Points / Evidence / Conflicts / Related` 구조.
4. 사실 주장에 출처 링크(상대 경로) 부착. 모순은 `Conflicts / Open Questions`에 기록.

### B. 유지보수
5. `link_check` 실행 → `broken_links`, `unindexed_pages`가 비었는지 확인. 남으면 고친다.

### C. 서빙 (시각화 갱신)
6. 터미널에서 사이트 재빌드:
   ```bash
   cd mcp-wiki && python serve/build_site.py
   python -m http.server -d site 8000   # 미리보기
   ```

### D. 마무리
7. `index.md`(create_page가 자동 등록)와 `log.md`(write가 자동 append)가 반영됐는지 확인.
8. 세션 요약을 `journal.md`에 append.

## 성공 기준

- 새/수정 페이지가 템플릿 구조를 지킨다.
- `link_check` 결과 끊긴 링크·색인 누락 0.
- 모든 사실에 검증 출처 링크가 붙어 있다.
- `build_site.py`가 오류 없이 사이트를 갱신한다.

## 비목표

- 페이지 삭제, 도메인 전환, 대량 재작성(사람 승인 필요).
- 의미 검색·임베딩(현재 범위 밖, [PRD §4](../../03-prd.md)).
