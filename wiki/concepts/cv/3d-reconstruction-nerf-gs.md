# 3D Reconstruction: NeRF & Gaussian Splatting

Domain: cv · Maturity: emerging

## Definition

다수의 2D 이미지로부터 3D 장면을 복원해 **novel-view synthesis**(새 시점 영상 생성)를 수행하는 기법. 두 주류 = NeRF(암시적 신경 표현)와 3D Gaussian Splatting(명시적 표현).

## Key Points

- **NeRF**: 장면을 좌표→(색, 밀도) 매핑 MLP로 표현, volumetric ray-marching으로 시점 합성. positional encoding으로 고주파 디테일 복원. 품질 높으나 학습·렌더가 매우 느림(샘플링 비용).
- **3D Gaussian Splatting(3DGS)**: 장면을 학습 가능한 anisotropic 3D Gaussian point cloud로 표현. 미분가능 splatting + tile-based rasterizer로 **1080p 실시간 렌더 + SOTA 품질**, 경쟁력 있는 학습 시간.
- **핵심 대비**: NeRF=암시적·느림·고품질, 3DGS=명시적·실시간·편집 용이. 3DGS가 NeRF 최상위 품질에 필적하며 실시간성이 강점.
- **Physical AI 연결**: 3D scene 복원 → 로봇 grasping·manipulation, 시뮬레이션 자산 생성에 활용.

## Evidence

- [Source: NeRF / 3D Gaussian Splatting](../../../sources/cv-physical-ai/nerf-gaussian-splatting.md)
- NeRF — https://arxiv.org/abs/2003.08934
- 3DGS — https://arxiv.org/abs/2308.04079

## Conflicts / Open Questions

- 둘 다 정적 장면·다시점 캡처 가정 기본 → 동적/반사/투명 표면 난제.
- 3DGS 메모리·저장 비용 큼. NeRF 변형(Instant-NGP 등) 다수라 "NeRF 느림" 일반화는 주의.

## Related

- [Vision Foundation Models](vision-foundation-models.md)
- [Sensor Fusion](../physical-ai/sensor-fusion.md)
- [Index](../../../index.md)
