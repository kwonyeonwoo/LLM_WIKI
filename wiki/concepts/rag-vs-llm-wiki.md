# RAG vs LLM Wiki

## Short Version

RAG는 질문 시점에 원문 조각을 찾아 답을 만든다. LLM Wiki는 자료를 읽을 때 지식을 Markdown 위키로 누적하고, 질문 시점에는 그 위키를 읽어 답한다.

## Comparison

| Dimension | RAG | LLM Wiki |
| --- | --- | --- |
| Main artifact | 원문 조각, 임베딩, 검색 인덱스 | Markdown 위키 |
| When synthesis happens | 질문할 때 | 자료 추가 시점과 질문 시점 모두 |
| Maintenance | 인덱스와 검색 품질 중심 | 페이지, 링크, 출처, 모순 관리 중심 |
| Strength | 많은 문서에서 빠른 검색 | 누적된 이해와 재사용 가능한 정리 |
| Weakness | 매번 재조합이 필요함 | 잘못된 정리가 누적될 수 있음 |
| Best fit | 대량 문서 검색, FAQ, 고객지원 | 연구, 개인 지식관리, 장기 프로젝트 |

## Practical Judgment

LLM Wiki가 RAG를 완전히 대체한다고 보면 과장이다. 자료가 크고 권한, 최신성, 정확한 검색 랭킹이 중요하면 RAG나 DB가 여전히 필요하다. 다만 개인 연구 규모에서는 Markdown 위키가 더 단순하고, 생각의 축적을 보기 쉽다.

## Source

- [Source Note: Karpathy LLM Wiki](../../sources/karpathy-llm-wiki.md)
