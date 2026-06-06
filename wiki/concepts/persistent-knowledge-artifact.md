# Persistent Knowledge Artifact

## Definition

Persistent knowledge artifact는 채팅 중 나온 유용한 지식을 재사용 가능한 파일로 남긴 결과물이다. LLM Wiki에서 이 artifact는 Markdown 페이지다.

## Why Chat Alone Is Weak

채팅은 빠르지만 누적성이 약하다. 좋은 비교표나 요약이 있어도 다음 세션에서 다시 설명해야 하거나, 이전 대화의 맥락을 잃는다. 파일로 남기면 지식은 검색, 수정, 링크, 버전관리의 대상이 된다.

## Examples

- 어떤 논문 묶음의 핵심 주장 비교
- 특정 개념의 정의와 반론
- 프로젝트 의사결정 기록
- 책의 인물 관계와 테마
- 반복적으로 묻는 질문에 대한 정리 답변

## Rule Of Thumb

다시 물어볼 가능성이 있는 답변은 위키에 저장할 가치가 있다. 단, 출처가 약하거나 일회성 판단이면 `Open Questions`나 `Notes`로 낮은 확신을 표시한다.

## Related

- [LLM Wiki](llm-wiki.md)
- [Query Workflow](../workflows/query.md)
