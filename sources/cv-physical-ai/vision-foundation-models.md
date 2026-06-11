# Source Note: Vision Foundation Models (CLIP / DINOv2 / ViT / MAE)

## Metadata

- Author: Radford et al. (CLIP); Oquab et al. (DINOv2); Dosovitskiy et al. (ViT); He et al. (MAE)
- Title: CLIP / DINOv2 / An Image is Worth 16x16 Words (ViT) / Masked Autoencoders
- Type: 학회 논문
- Published: ViT 2020; CLIP 2021; MAE 2021; DINOv2 2023
- Accessed: 2026-06-06
- URL:
  - CLIP: https://arxiv.org/abs/2103.00020
  - DINOv2: https://arxiv.org/abs/2304.07193
  - ViT: https://arxiv.org/abs/2010.11929
  - MAE: https://arxiv.org/abs/2111.06377

## Summary

대규모 데이터로 사전학습해 다양한 downstream에 전이되는 vision backbone 계열. 언어정렬형(CLIP)과 자기지도형(DINOv2, MAE)으로 갈림. ViT가 공통 아키텍처 기반.

## Key Claims

- ViT: 이미지를 패치 시퀀스로 보고 transformer 적용. CNN 없이도 대규모 학습 시 SOTA.
- CLIP: 4억(400M) 이미지-캡션 쌍을 contrastive 학습으로 공유 임베딩 정렬 → zero-shot 분류.
- DINOv2: 자기지도 학습으로 1.42억(142M) 큐레이션 이미지 학습 → 라벨 없이 전이성 높은 feature. 최소 fine-tuning으로 광범위 태스크 대응.
- MAE: 입력 패치 75%를 마스킹 후 복원 학습 → ViT용 효율적 자기지도.

## Useful Details

- CLIP feature는 vision-language(검색·VLM·VLA)의 기반. DINOv2 feature는 dense 예측(분할·깊이)에 강함.
- foundation model = 광범위 데이터 사전학습 후 다수 태스크에 적응하는 모델.

## Limits And Risks

- 학습 데이터 편향·라이선스 이슈. zero-shot은 분포 밖 도메인에서 저하.
- "foundation model" 정의가 느슨 → 범위 과장 주의.

## Related Wiki Pages

- [Vision Foundation Models](../../wiki/concepts/cv/vision-foundation-models.md)
