---
title: 지식 도메인 정의 — 컴퓨터비전 / 피지컬 AI
status: draft
date: 2026-06-06
tags: [computer-vision, physical-ai, knowledge-domain, mcp-wiki, scope]
description: MCP 기반 wiki tool이 다룰 지식 도메인을 컴퓨터비전과 피지컬 AI 두 축, 그리고 둘의 교집합(embodied perception)으로 정의하고 포함/제외 범위와 페이지 분류 체계를 명시하는 설계 문서.
domain: cv, physical-ai
type: design-doc
---

# 지식 도메인 정의: 컴퓨터비전 / 피지컬 AI

Status: draft
Owner: 사용자 + LLM agent
관련 문서: [PRD](03-prd.md) · [의사결정 라운드](02-decision-rounds.md) · [README](README.md)

이 문서는 MCP 기반 wiki tool이 다룰 지식 도메인의 경계를 정의한다. 위키가 "무엇을 담고, 무엇을 담지 않는가"를 먼저 고정해야 ingest 기준, 페이지 분류, 링크 구조가 흔들리지 않는다.

## 1. 도메인 한 줄 정의

이 위키는 **컴퓨터비전(Computer Vision)** 과 **피지컬 AI(Physical AI)** 두 축, 그리고 둘이 만나는 교집합(로봇 인지, embodied perception)을 다루는 기술 지식베이스다.

기존 저장소가 "Agentic Coding Basics"를 다뤘다면, 이 위키는 도메인을 CV/Physical AI로 전환한다. 위키 운영 메커니즘(source → wiki 분리, ingest/query/lint)은 [기존 AGENTS.md](../AGENTS.md) 규칙을 그대로 계승한다.

## 2. 두 축의 정의

### 2.1 컴퓨터비전 (Computer Vision)

이미지/비디오에서 의미를 추출하는 알고리즘과 모델 계열.

핵심 하위 영역:
- **인식(Recognition)**: classification, detection, segmentation, pose estimation
- **기하(Geometry)**: camera model, calibration, multi-view geometry, SfM, SLAM, depth estimation
- **생성/표현(Generation & Representation)**: diffusion, NeRF, 3D Gaussian Splatting, representation learning
- **비디오/시계열**: tracking, action recognition, optical flow
- **기반 모델**: ViT, CLIP, SAM, DINO 계열 vision foundation model

### 2.2 피지컬 AI (Physical AI)

물리 세계에서 동작하는 에이전트(로봇, 자율 시스템)의 인지–판단–제어 스택.

핵심 하위 영역:
- **로봇 학습**: imitation learning, reinforcement learning, VLA(Vision-Language-Action) 모델
- **인지(Perception)**: 센서 융합(LiDAR/카메라/IMU), 3D scene understanding, occupancy
- **제어/플래닝**: motion planning, MPC, sim-to-real transfer
- **시뮬레이션**: Isaac Sim, MuJoCo, 도메인 랜덤화, world model
- **하드웨어 맥락**: manipulator, mobile robot, humanoid, edge 추론 제약

### 2.3 교집합 (위키의 핵심 가치 영역)

CV와 Physical AI가 겹치는 지점이 이 위키가 가장 깊게 파야 할 곳:

- embodied perception (행동을 위한 인지)
- 로봇용 실시간 detection/segmentation
- depth/3D 복원 → manipulation grasping
- VLA 모델 (vision foundation model + action head)
- sim-to-real에서의 vision domain gap

## 3. 페이지 분류 체계

기존 `wiki/concepts|workflows|pipelines|analyses|schema` 구조 위에, 도메인 분류 태그를 페이지 front-matter에 추가한다.

```
domain: cv | physical-ai | intersection
maturity: established | emerging | speculative
```

권장 디렉터리 매핑(구현 단계에서 확정):

```
wiki/concepts/cv/...
wiki/concepts/physical-ai/...
wiki/concepts/intersection/...
```

## 4. 포함 / 제외 기준 (Scope Boundary)

### 포함 (In scope)
- CV/Physical AI의 모델, 알고리즘, 시스템 아키텍처
- 핵심 논문·기법의 개념 요약과 비교
- 두 도메인을 잇는 실전 파이프라인
- 벤치마크, 데이터셋, 평가 지표

### 제외 (Out of scope)
- CV/Physical AI와 무관한 일반 ML/NLP 이론 (참조 링크만 허용)
- 제품 마케팅·뉴스성 내용 (출처 노트로만, wiki 본문 승격 금지)
- 코드 전체 덤프 (개념 설명에 필요한 스니펫만)

### 경계 사례 처리
- LLM 일반론 → 제외. 단 VLA/멀티모달처럼 Physical AI에 직접 쓰이면 intersection으로 포함.
- 순수 그래픽스(렌더링) → 제외. 단 NeRF/Gaussian Splatting처럼 인지·복원에 쓰이면 CV로 포함.

## 5. 시드 페이지 (구현 후 첫 ingest 대상)

| 페이지 | domain | 우선순위 |
|---|---|---|
| object-detection-overview | cv | high |
| segmentation-sam-family | cv | high |
| 3d-reconstruction-nerf-gs | cv | mid |
| vla-models | intersection | high |
| sim-to-real-transfer | physical-ai | mid |
| sensor-fusion | physical-ai | mid |
| vision-foundation-models | cv | high |

## 6. Conflicts / Open Questions

- CV와 Physical AI 비중을 50:50으로 둘지, intersection 중심으로 둘지 — 초기엔 intersection 우선, ingest 누적 후 재조정.
- 논문 단위 페이지 vs 개념 단위 페이지 — 기본은 개념 단위, 영향 큰 논문(SAM, CLIP 등)만 단독 페이지.
- maturity=speculative 항목(world model 등)의 검증 기준 미정.
