# Sensor Fusion

Domain: physical-ai · Maturity: established

## Definition

Sensor fusion은 카메라·LiDAR·radar 등 **상호보완적 센서 신호를 결합**해 강건한 인지(검출·분할·예측)를 구성하는 기법이다. 자율주행·로봇 인지의 핵심.

## Key Points

- **센서 상보성**: 카메라=조밀한 색/텍스처, LiDAR=정확한 3D 기하/깊이, radar=속도·악천후 강건.
- **융합 단계 분류**:
  - **Data-level (early)**: raw 데이터 직접 결합 → 정렬·동기화 문제에 취약.
  - **Feature-level (mid)**: modality별 backbone 중간 feature 결합 → attention 등 유연. 현재 주류.
  - **Decision-level (late)**: 각 모달 결과를 후단에서 결합.
- **두 주류 트렌드**: 통합 BEV(Bird's-Eye-View) 표현, token-level cross-modal alignment.
- **적용**: object detection, semantic segmentation, behavior prediction, planning.

## Evidence

- [Source: Multi-modal Sensor Fusion](../../../sources/cv-physical-ai/sensor-fusion.md)
- Multi-modal Sensor Fusion for Auto Driving Perception: A Survey — https://arxiv.org/abs/2202.02703

## Conflicts / Open Questions

- 난제: 시공간 정렬(mis-alignment), domain shift, 해석가능성 부족.
- survey가 자율주행 중심 → 로봇 manipulation 융합은 부분적 반영.

## Related

- [Object Detection Overview](../cv/object-detection-overview.md)
- [Sim-to-Real Transfer](sim-to-real-transfer.md)
- [3D Reconstruction: NeRF & Gaussian Splatting](../cv/3d-reconstruction-nerf-gs.md)
- [Index](../../../index.md)
