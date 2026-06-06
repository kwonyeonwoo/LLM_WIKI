# LLM Wiki

## Definition

LLM Wiki는 LLM이 원문 자료를 읽고 지속적으로 갱신하는 Markdown 지식베이스다. 사용자는 자료와 질문을 제공하고, LLM은 요약, 링크, 개념 페이지, 모순 기록, 색인을 관리한다.

## Core Idea

일반적인 문서 기반 질문응답은 질문할 때마다 관련 조각을 검색하고 즉석에서 답을 만든다. LLM Wiki는 그 작업의 일부를 미리 축적한다. 새 자료가 들어올 때 LLM이 기존 위키에 내용을 통합하기 때문에, 다음 질문은 원문 조각만이 아니라 이미 정리된 지식 구조를 활용한다.

## Components

- Raw source layer: 원문 또는 원문 기반 노트.
- Wiki layer: 개념, 인물, 사건, 비교, 요약을 담은 Markdown 페이지.
- Schema layer: LLM에게 위키 관리 방식을 알려주는 규칙 파일.

이 저장소에서는 `sources/`, `wiki/`, `AGENTS.md`가 각각 이 역할을 맡는다.

## Why It Matters

LLM Wiki의 장점은 답변을 일회성 채팅 결과로 버리지 않는다는 점이다. 좋은 요약, 비교, 반론, 미해결 질문을 파일로 남기면 다음 작업의 출발점이 좋아진다.

## Failure Modes

- 잘못된 요약이 여러 페이지에 퍼질 수 있다.
- 출처 없는 문장이 점점 사실처럼 굳어질 수 있다.
- 링크가 깨지거나 중복 페이지가 생길 수 있다.
- 오래된 내용과 최신 내용이 섞일 수 있다.

## Source

- [Source Note: Karpathy LLM Wiki](../../sources/karpathy-llm-wiki.md)
