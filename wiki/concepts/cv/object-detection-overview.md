# Object Detection Overview

Domain: cv · Maturity: established

## Definition

Object detection은 이미지/비디오에서 객체의 **클래스**와 **위치(bounding box)**를 동시에 예측하는 컴퓨터비전 과제다. 분류(classification)와 위치추정(localization)의 결합.

## Key Points

- **세 가지 패러다임**:
  - **Two-stage**: sparse proposal 생성 후 분류·정제. 정확도 우위, 상대적으로 느림. 대표: R-CNN → Fast R-CNN → Faster R-CNN(RPN).
  - **One-stage**: proposal 단계 없이 모든 위치를 후보로 단일 패스 예측. 실시간성 우위. 대표: YOLO 계열, SSD, RetinaNet(Focal Loss).
  - **Transformer / set prediction**: DETR이 검출을 집합 예측으로 재정의, NMS·anchor 등 hand-crafted 요소 제거. Deformable DETR이 수렴·효율 개선.
- **평가**: mAP(mean Average Precision), IoU 임계값 기준. 벤치마크 = COCO, PASCAL VOC.
- **트레이드오프**: 정확도 ↔ 지연(latency). 로봇/자율주행은 실시간 one-stage 또는 효율형 DETR 선호.

## Evidence

- [Source: Object Detection (surveys + landmark papers)](../../../sources/cv-physical-ai/object-detection.md)
- Object Detection in 20 Years: A Survey — https://arxiv.org/abs/1905.05055
- DETR — https://arxiv.org/abs/2005.12872

## Conflicts / Open Questions

- Survey 출처가 2019~2021 시점 → RT-DETR, 최신 YOLO 버전 등 후속 발전 미반영.
- "two-stage가 항상 더 정확" 주장은 최신 one-stage/DETR로 경계가 흐려짐 → 재검토 필요.

## Related

- [Vision Foundation Models](vision-foundation-models.md)
- [Segmentation: SAM Family](segmentation-sam-family.md)
- [Sensor Fusion](../physical-ai/sensor-fusion.md)
- [Index](../../../index.md)
