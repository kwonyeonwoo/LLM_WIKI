# Index

이 파일은 위키의 탐색 진입점이다. 질문에 답하기 전 먼저 읽고, 관련 페이지로 이동한다.

현재 지식 도메인: **컴퓨터비전 / 피지컬 AI** (정의: [mcp-wiki/01-knowledge-domain.md](mcp-wiki/01-knowledge-domain.md)).

## Core

- [Overview](wiki/overview.md): 이 위키의 현재 범위와 운영 철학.
- [Log](log.md): ingest, query, lint 작업 이력.
- [Task](TASK.md): 현재 과제 완료 조건.
- [Journal](journal.md): append-only 작업 저널.
- [Agent Instructions](AGENTS.md): LLM이 따라야 할 운영 규칙.
- [LLM Wiki Schema](wiki/schema/llm-wiki-schema.md): 저장소 구조와 유지보수 불변조건.

## Wiki System (meta)

- [LLM Wiki](wiki/concepts/llm-wiki.md): LLM이 유지하는 지속적 Markdown 지식베이스.
- [RAG vs LLM Wiki](wiki/concepts/rag-vs-llm-wiki.md): 검색-시점 합성과 축적형 위키의 차이.
- [Persistent Knowledge Artifact](wiki/concepts/persistent-knowledge-artifact.md): 채팅 결과를 재사용 가능한 파일로 남기는 사고방식.
- [Markdown-Only Constraint](wiki/concepts/markdown-only-constraint.md): DB, 스크립트, 플러그인 없이 운용할 때의 장단점.

## Concepts — Computer Vision

- [Object Detection Overview](wiki/concepts/cv/object-detection-overview.md): two-stage / one-stage / DETR 검출 패러다임.
- [Segmentation: SAM Family](wiki/concepts/cv/segmentation-sam-family.md): promptable segmentation foundation model (SAM, SAM 2).
- [3D Reconstruction: NeRF & Gaussian Splatting](wiki/concepts/cv/3d-reconstruction-nerf-gs.md): novel-view synthesis와 3D 복원.
- [Vision Foundation Models](wiki/concepts/cv/vision-foundation-models.md): CLIP, DINOv2, ViT, MAE.

## Concepts — Physical AI

- [Sim-to-Real Transfer](wiki/concepts/physical-ai/sim-to-real-transfer.md): 시뮬레이터 학습 정책의 실로봇 전이.
- [Sensor Fusion](wiki/concepts/physical-ai/sensor-fusion.md): 카메라·LiDAR·radar 융합 인지.

## Concepts — Intersection (CV × Physical AI)

- [VLA Models](wiki/concepts/intersection/vla-models.md): vision-language-action end-to-end 로봇 정책 (RT-2, OpenVLA, π0).

## Sources

- [Sources README](sources/README.md): 출처 노트 관리 방식.
- [Karpathy LLM Wiki](sources/karpathy-llm-wiki.md): Andrej Karpathy의 LLM Wiki gist 요약 (위키 시스템 출처).
- [Object Detection](sources/cv-physical-ai/object-detection.md)
- [Segment Anything (SAM / SAM 2)](sources/cv-physical-ai/segment-anything.md)
- [NeRF / 3D Gaussian Splatting](sources/cv-physical-ai/nerf-gaussian-splatting.md)
- [VLA Models](sources/cv-physical-ai/vla-models.md)
- [Sim-to-Real Transfer](sources/cv-physical-ai/sim-to-real.md)
- [Multi-modal Sensor Fusion](sources/cv-physical-ai/sensor-fusion.md)
- [Vision Foundation Models](sources/cv-physical-ai/vision-foundation-models.md)

## Workflows

- [Ingest Workflow](wiki/workflows/ingest.md): 새 자료를 위키에 통합하는 절차.
- [Query Workflow](wiki/workflows/query.md): 위키 기반으로 질문에 답하는 절차.
- [Lint Workflow](wiki/workflows/lint.md): 위키 상태를 점검하고 정리하는 절차.
- [LLM Maintenance](wiki/workflows/maintenance.md): session start, stop, bounded loop, maintenance hook 규칙.

## Pipelines

- [Raw Item To Wiki Pages](wiki/pipelines/raw-item-to-wiki-pages.md): raw item을 source note와 wiki page로 변환하는 핵심 파이프라인.

## MCP Wiki (설계 문서)

- [지식 도메인 정의](mcp-wiki/01-knowledge-domain.md)
- [의사결정 라운드](mcp-wiki/02-decision-rounds.md)
- [PRD / 사양서](mcp-wiki/03-prd.md)
- [MCP Wiki README](mcp-wiki/README.md)

## Templates

- [Page Template](templates/page.md): 일반 위키 페이지 양식.
- [Source Note Template](templates/source-note.md): 출처 노트 양식.
- [Query Result Template](templates/query-result.md): 재사용 가능한 질의 결과 양식.
- [Lint Report Template](templates/lint-report.md): 점검 보고서 양식.

## Open Questions

- 시드 7개 외 다음 ingest 우선순위(예: occupancy, world model, grasping) 결정 필요.
- CV : Physical AI : intersection 비중 재조정 (현재 4:2:1).
- 출처 arxiv abs 다수 → 출판본 수치와 대조 점검 필요.
