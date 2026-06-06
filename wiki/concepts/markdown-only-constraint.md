# Markdown-Only Constraint

## Definition

Markdown-only constraint는 이 위키가 데이터베이스, 스크립트, 플러그인, 임베딩 인덱스 없이 `.md` 파일만으로 운영된다는 제약이다.

## Advantages

- 구조가 투명하다.
- 어떤 에디터에서도 읽을 수 있다.
- Git으로 변경 이력을 추적하기 쉽다.
- LLM이 직접 읽고 수정하기 쉽다.
- 도구가 망가져도 파일은 남는다.

## Costs

- 링크 무결성을 자동 보장하지 않는다.
- 대규모 검색은 약하다.
- 중복 페이지를 막기 어렵다.
- 권한 관리와 승인 흐름이 없다.
- 오래된 내용을 자동으로 폐기하지 않는다.

## Operating Implication

이 제약에서는 `index.md`와 `log.md`가 사실상 수동 데이터베이스 역할을 한다. 위키가 커질수록 이 두 파일의 품질이 전체 시스템의 품질을 좌우한다.

## When To Break The Constraint

다음 문제가 반복되면 Markdown-only를 유지할지 다시 판단한다.

- 관련 페이지를 찾는 시간이 길어진다.
- 중복 개념 페이지가 자주 생긴다.
- 출처 추적이 불안정하다.
- 수백 개 이상의 페이지에서 링크 점검이 부담된다.

## Related

- [Lint Workflow](../workflows/lint.md)
