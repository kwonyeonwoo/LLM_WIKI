# Overview

이 위키는 LLM Wiki 패턴을 구현한 markdown-only 지식베이스 **템플릿**이다. 검증된 출처에서 수집한 개념을 페이지로 축적한다. 운영 메커니즘은 Karpathy의 LLM Wiki gist 패턴을 따른다.

## What This Wiki Is

채팅창에서 사라지는 요약을 파일로 축적하기 위한 구조다. LLM이 자료를 읽고, 개념 페이지를 갱신하고, 질문 결과를 다시 저장하면서 지식이 누적된다.

## What This Wiki Is Not

- 벡터 DB가 아니다.
- 자동 검색 엔진이 아니다.
- 완성된 제품이 아니다.
- 출처 검증 없이 믿어도 되는 진실 저장소가 아니다.

## Current Scope

_(여기에 너의 위키가 현재 답할 수 있는 질문들을 적는다. 자료를 ingest 할수록 늘어난다.)_

템플릿은 예시로 cv / physical-ai / intersection 도메인 분류와 예시 페이지 1개([Example Concept](concepts/cv/example-concept.md))를 둔다. 도메인 바꾸는 법은 [루트 README](../README.md#너의-도메인으로-바꾸기) 참고.

위키 운영:
- LLM Wiki란 무엇이고 RAG와 무엇이 다른가? → [RAG vs LLM Wiki](concepts/rag-vs-llm-wiki.md)
- Markdown만으로 운영하면 어떤 장단점이 있는가? → [Markdown-Only Constraint](concepts/markdown-only-constraint.md)
- 새 자료를 어떻게 ingest / 점검하는가? → [Ingest](workflows/ingest.md) · [Lint](workflows/lint.md)

## Maintenance Rule

새 자료를 추가할 때마다 다음 파일을 함께 갱신한다 (write tool은 index·log를 자동 갱신).

- [index.md](../index.md)
- [log.md](../log.md)
- 관련 `wiki/concepts/` 페이지
- 관련 `sources/` 출처 노트
