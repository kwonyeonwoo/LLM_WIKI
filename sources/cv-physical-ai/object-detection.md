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
  - RT-DETR (DETRs Beat YOLOs on Real-time Object Detection, CVPR 2024): https://arxiv.org/abs/2304.08069
  - YOLOv10 (Real-Time End-to-End Object Detection): https://arxiv.org/abs/2405.14458
  - YOLO 10년 리뷰: https://arxiv.org/abs/2406.19407

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

## Recent Developments (2023–2025)

- **RT-DETR** (arXiv:2304.08069, CVPR 2024): 최초의 실시간 end-to-end DETR. NMS 제거하고도 YOLO보다 빠르고 정확 → "실시간 검출 = YOLO" 의존을 깸. one-stage와 transformer 검출의 경계가 흐려지는 변곡점.
- **YOLOv10** (arXiv:2405.14458): consistent dual assignments로 **NMS-free end-to-end 학습**. YOLOv10-S가 RT-DETR-R18 대비 유사 AP에서 1.8× 빠르고 파라미터·FLOPs 2.8× 작음. → YOLO 계열도 NMS를 버리는 방향.
- **YOLOv11**: 아키텍처 계층·neck 연결 개선으로 연속 진화.
- **수렴 흐름**: one-stage(YOLO)와 set-prediction(DETR)이 모두 **NMS-free end-to-end**로 수렴 중. 옛 "two-stage가 더 정확 / one-stage가 더 빠름" 이분법이 약화.

## Limits And Risks

- 기반 survey는 2019~2021 시점 → 위 Recent Developments로 보강했으나 추가 후속(RT-DETRv2/v4 등) 검증 필요.
- arxiv abs는 동료심사 전 버전 가능 → 출판본과 수치 차이 가능.

## Related Wiki Pages

- [Object Detection Overview](../../wiki/concepts/cv/object-detection-overview.md)
