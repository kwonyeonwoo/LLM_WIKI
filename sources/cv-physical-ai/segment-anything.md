# Source Note: Segment Anything (SAM / SAM 2)

## Metadata

- Author: Kirillov et al. (SAM); Ravi et al. (SAM 2) — Meta AI
- Title: Segment Anything / SAM 2: Segment Anything in Images and Videos
- Type: 학회 논문 + 공식 릴리스
- Published: SAM 2023-04; SAM 2 2024-07-29
- Accessed: 2026-06-06
- URL:
  - SAM: https://arxiv.org/abs/2304.02643
  - SAM 2: https://arxiv.org/abs/2408.00714
  - Meta 공식: https://ai.meta.com/research/sam2/

## Summary

SAM = promptable segmentation foundation model. point/box/mask prompt를 받아 객체 마스크를 zero-shot으로 분할. SAM 2는 이를 비디오로 확장하고 속도 개선.

## Key Claims

- SAM 구조: image encoder + prompt encoder(point/box/mask) + lightweight mask decoder.
- 학습 데이터 SA-1B: 1,100만 이미지에 10억(1B)+ 마스크. 미학습 객체도 zero-shot 분할.
- SAM 2: streaming memory를 가진 transformer로 실시간 비디오 분할. per-session memory module로 객체를 프레임 전반 추적(일시 가림에도).
- SAM 2 성능: 비디오에서 상호작용 3배 적게 쓰고 정확도↑, 이미지에서 원본 SAM 대비 6배 빠르고 더 정확.

## Useful Details

- prompt 기반 interactive segmentation → annotation tool, downstream 마스크 생성에 활용.
- data engine: 모델-사람 상호작용 루프로 데이터셋을 키움.

## Limits And Risks

- SAM은 "무엇"인지 의미 레이블을 주지 않음 (class-agnostic 마스크). semantic label은 별도 모델 필요.
- 작고 가는 구조, 모호한 경계에서 실패 가능.

## Related Wiki Pages

- [Segmentation: SAM Family](../../wiki/concepts/cv/segmentation-sam-family.md)
