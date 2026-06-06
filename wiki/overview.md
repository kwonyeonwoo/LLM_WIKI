# Overview

이 위키는 LLM Wiki 패턴을 실험하기 위한 markdown-only 지식베이스다. 현재 주제는 LLM 기반 지식관리이며, 첫 출처는 Andrej Karpathy의 LLM Wiki gist다.

## What This Wiki Is

이 위키는 채팅창에서 사라지는 요약을 파일로 축적하기 위한 구조다. LLM이 자료를 읽고, 개념 페이지를 갱신하고, 질문 결과를 다시 저장하면서 지식이 누적된다.

## What This Wiki Is Not

- 벡터 DB가 아니다.
- 자동 검색 엔진이 아니다.
- 완성된 제품이 아니다.
- 출처 검증 없이 믿어도 되는 진실 저장소가 아니다.

## Current Scope

현재는 다음 질문에 답할 수 있도록 구성되어 있다.

- LLM Wiki란 무엇인가?
- RAG와 무엇이 다른가?
- Markdown만으로 운영하면 어떤 장단점이 있는가?
- 새 자료를 어떻게 ingest 하는가?
- 위키를 어떻게 점검하는가?

## Maintenance Rule

새 자료를 추가할 때마다 다음 파일을 함께 갱신한다.

- [index.md](../index.md)
- [log.md](../log.md)
- 관련 `wiki/concepts/` 페이지
- 관련 `sources/` 출처 노트
