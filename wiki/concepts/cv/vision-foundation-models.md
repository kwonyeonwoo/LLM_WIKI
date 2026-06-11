# Vision Foundation Models

Domain: cv · Maturity: established

## Definition

대규모 데이터로 사전학습해 다양한 downstream 과제에 전이되는 vision backbone 계열. 언어정렬형(CLIP)과 자기지도형(DINOv2, MAE)으로 갈리며, Vision Transformer(ViT)가 공통 아키텍처 기반.

## Key Points

- **ViT**: 이미지를 패치 시퀀스로 보고 transformer 적용. CNN 없이 대규모 학습 시 SOTA. 후속 foundation model의 backbone.
- **CLIP**: 4억(400M) 이미지-캡션 쌍을 contrastive 학습으로 공유 임베딩 정렬 → zero-shot 분류. vision-language·VLM·VLA의 기반.
- **DINOv2**: 자기지도 학습으로 1.42억(142M) 큐레이션 이미지 학습 → 라벨 없이 전이성 높은 dense feature. 분할·깊이 등 dense 예측에 강함.
- **MAE(Masked Autoencoder)**: 입력 패치 75% 마스킹 후 복원 → ViT용 효율적 자기지도 사전학습.
- **두 갈래 정리**: 언어정렬(CLIP)=의미·검색·멀티모달, 자기지도(DINOv2/MAE)=dense 시각 feature.

## Evidence

- [Source: Vision Foundation Models](../../../sources/cv-physical-ai/vision-foundation-models.md)
- CLIP — https://arxiv.org/abs/2103.00020
- DINOv2 — https://arxiv.org/abs/2304.07193
- ViT — https://arxiv.org/abs/2010.11929

## Conflicts / Open Questions

- 학습 데이터 편향·라이선스 이슈. zero-shot은 분포 밖 도메인에서 저하.
- "foundation model" 정의가 느슨 → 범위 과장 주의.

## Related

- [Object Detection Overview](object-detection-overview.md)
- [Segmentation: SAM Family](segmentation-sam-family.md)
- [VLA Models](../intersection/vla-models.md)
- [Index](../../../index.md)
