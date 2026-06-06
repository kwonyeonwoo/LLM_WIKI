# Source Note: Object Detection (Surveys + Landmark Papers)

## Metadata

- Author: Zou et al.; Faster R-CNN (Ren et al.); YOLO (Redmon et al.); DETR (Carion et al.)
- Title: Object Detection in 20 Years: A Survey 외
- Type: peer-reviewed survey + 학회 논문
- Published: 2019~2020
- Accessed: 2026-06-06
- URL:
  - Survey "Object Detection in 20 Years": https://arxiv.org/abs/1905.05055
  - Survey "Modern DL based Object Detection Models": https://arxiv.org/abs/2104.11892
  - Faster R-CNN: https://arxiv.org/abs/1506.01497
  - YOLO: https://arxiv.org/abs/1506.02640
  - DETR (End-to-End Object Detection with Transformers): https://arxiv.org/abs/2005.12872

## Summary

Object detection = 이미지 내 객체의 클래스 + 위치(bbox)를 동시에 예측. 딥러닝 이후 two-stage(proposal→classify), one-stage(단일 패스), transformer 기반 set-prediction(DETR) 세 계열로 발전.

## Key Claims

- Two-stage 검출기는 sparse proposal을 먼저 생성 후 분류 → 정확도 높음, 느림 (Faster R-CNN).
- One-stage 검출기는 proposal 단계 없이 모든 위치를 후보로 봄 → 실시간성 우수 (YOLO, SSD, RetinaNet).
- DETR은 검출을 set prediction으로 보고 NMS·anchor 같은 hand-crafted 요소를 제거. Deformable DETR이 학습 효율·수렴 개선.

## Useful Details

- 평가 지표: mAP (mean Average Precision), IoU 임계값 기반. 벤치마크: COCO, PASCAL VOC.
- Two-stage 대표: R-CNN → Fast R-CNN → Faster R-CNN (RPN 도입).
- One-stage 대표: YOLO 계열, RetinaNet(Focal Loss로 class imbalance 완화).
- DETR: bipartite matching loss + transformer encoder-decoder.

## Limits And Risks

- Survey는 2019~2021 시점 → 이후 RT-DETR, YOLO 최신 버전 등 미반영.
- arxiv abs는 동료심사 전 버전 가능 → 출판본과 수치 차이 가능.

## Related Wiki Pages

- [Object Detection Overview](../../wiki/concepts/cv/object-detection-overview.md)
