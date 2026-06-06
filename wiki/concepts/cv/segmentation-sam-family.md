# Segmentation: SAM Family

Domain: cv · Maturity: established

## Definition

Segmentation은 이미지를 픽셀 단위로 영역 분할하는 과제다. SAM(Segment Anything Model) 계열은 **promptable segmentation** foundation model로, point/box/mask 같은 prompt를 받아 객체 마스크를 zero-shot으로 생성한다.

## Key Points

- **SAM 구조**: image encoder + prompt encoder(point/box/mask) + lightweight mask decoder. prompt 기반 interactive segmentation.
- **SA-1B 데이터**: 1,100만 이미지, 10억(1B)+ 마스크. data engine(모델-사람 루프)으로 구축. 미학습 객체도 zero-shot 분할.
- **SAM 2**: streaming memory transformer로 이미지+비디오 통합. per-session memory module이 객체를 프레임 전반 추적(일시 가림 포함).
- **성능(SAM 2 vs SAM)**: 비디오 상호작용 3배 절감 + 정확도↑, 이미지 6배 빠르고 더 정확.
- **분할 종류 맥락**: semantic / instance / panoptic. SAM은 class-agnostic 마스크(의미 레이블 미제공).

## Evidence

- [Source: Segment Anything (SAM / SAM 2)](../../../sources/cv-physical-ai/segment-anything.md)
- SAM — https://arxiv.org/abs/2304.02643
- SAM 2 — https://arxiv.org/abs/2408.00714

## Conflicts / Open Questions

- SAM은 "무엇"인지 클래스를 주지 않음 → semantic label은 별도 모델 결합 필요.
- 가는 구조·모호 경계에서 실패 가능. 로봇 실시간 적용 시 지연 평가 미정.

## Related

- [Vision Foundation Models](vision-foundation-models.md)
- [Object Detection Overview](object-detection-overview.md)
- [VLA Models](../intersection/vla-models.md)
- [Index](../../../index.md)
