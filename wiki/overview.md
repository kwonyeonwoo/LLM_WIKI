# Overview

이 위키는 LLM Wiki 패턴을 실험하기 위한 markdown-only 지식베이스다. 현재 지식 도메인은 **컴퓨터비전 / 피지컬 AI**이며, 검증된 출처(arXiv, Meta AI, INRIA 등)에서 수집한 개념을 축적한다. 운영 메커니즘은 Karpathy의 LLM Wiki gist 패턴을 따른다.

## What This Wiki Is

이 위키는 채팅창에서 사라지는 요약을 파일로 축적하기 위한 구조다. LLM이 자료를 읽고, 개념 페이지를 갱신하고, 질문 결과를 다시 저장하면서 지식이 누적된다.

## What This Wiki Is Not

- 벡터 DB가 아니다.
- 자동 검색 엔진이 아니다.
- 완성된 제품이 아니다.
- 출처 검증 없이 믿어도 되는 진실 저장소가 아니다.

## Current Scope

현재는 다음 질문에 답할 수 있도록 구성되어 있다.

도메인 (컴퓨터비전 / 피지컬 AI):
- Object detection 패러다임(two-stage / one-stage / DETR)은 무엇인가?
- SAM 계열 promptable segmentation은 어떻게 동작하는가?
- NeRF와 3D Gaussian Splatting의 차이는?
- Vision foundation model(CLIP, DINOv2 등)이란?
- VLA 모델이 CV와 로봇을 어떻게 잇는가?
- Sim-to-real transfer와 sensor fusion의 핵심 방법은?

위키 운영:
- LLM Wiki란 무엇이고 RAG와 무엇이 다른가?
- Markdown만으로 운영하면 어떤 장단점이 있는가?
- 새 자료를 어떻게 ingest / 점검하는가?

## Maintenance Rule

새 자료를 추가할 때마다 다음 파일을 함께 갱신한다.

- [index.md](../index.md)
- [log.md](../log.md)
- 관련 `wiki/concepts/` 페이지
- 관련 `sources/` 출처 노트
