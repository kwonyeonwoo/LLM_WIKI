# Ingest Workflow

새 자료를 위키에 통합하는 절차다.

## Input

- `inbox/`의 Markdown 파일
- 사용자가 직접 제공한 텍스트
- 원문 URL과 사용자가 붙인 요약

## Steps

1. 자료의 제목, 작성자, 날짜, URL, 접근일을 확인한다.
2. `sources/`에 출처 노트를 만든다.
3. 핵심 주장, 개념, 인물, 시스템, 반론, 숫자를 추출한다.
4. `index.md`에서 관련 페이지를 찾는다.
5. 기존 페이지를 갱신하거나 새 페이지를 만든다.
6. 모순이나 불확실성은 별도 섹션에 남긴다.
7. 모든 새 페이지를 `index.md`에 추가한다.
8. `log.md`에 ingest 기록을 남긴다.

## Output Checklist

- [ ] Source note exists in `sources/`.
- [ ] Relevant concept pages are updated.
- [ ] New pages are linked from `index.md`.
- [ ] Source links are present on strong factual claims.
- [ ] Contradictions or uncertainties are marked.
- [ ] `log.md` has a new entry.

## Page Placement

- 개념: `wiki/concepts/`
- 워크플로: `wiki/workflows/`
- 분석 결과: `wiki/analyses/`
- 인물 또는 조직: `wiki/entities/`
- 프로젝트 의사결정: `wiki/decisions/`

필요한 폴더가 없으면 Markdown 파일과 함께 새로 만든다.
