# Source Note: Multi-modal Sensor Fusion (Autonomous Driving)

## Metadata

- Author: Huang et al.
- Title: Multi-modal Sensor Fusion for Auto Driving Perception: A Survey
- Type: peer-reviewed survey
- Published: 2022 (v3 갱신)
- Accessed: 2026-06-06
- URL:
  - Survey: https://arxiv.org/abs/2202.02703

## Summary

Sensor fusion = 카메라·LiDAR·radar 등 상호보완적 센서 신호를 결합해 강건한 인지(검출·분할·예측)를 구성. 자율주행·로봇 인지의 핵심.

## Key Claims

- 융합 단계 분류: data-level(early), feature-level(mid), decision-level(late).
- Early fusion: raw 데이터 직접 결합 → 정렬·동기화 문제에 취약.
- Mid-level fusion: modality별 backbone의 중간 feature 결합 → attention 등 유연. 두 주류 트렌드 = 통합 BEV 표현, token-level cross-modal alignment.
- 적용: object detection, semantic segmentation, behavior prediction, planning.

## Useful Details

- 센서 상보성: 카메라=조밀한 색/텍스처, LiDAR=정확한 3D 기하/깊이, radar=속도·악천후 강건.
- 난제: 시공간 정렬(mis-alignment), domain shift, 해석가능성 부족.

## Limits And Risks

- survey 범위 = 자율주행 중심. 일반 로봇 manipulation 융합은 부분적.
- BEV·attention 트렌드는 빠르게 변함 → 최신성 점검 필요.

## Related Wiki Pages

- [Sensor Fusion](../../wiki/concepts/physical-ai/sensor-fusion.md)
