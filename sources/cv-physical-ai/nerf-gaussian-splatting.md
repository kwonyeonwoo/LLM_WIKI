# Source Note: NeRF / 3D Gaussian Splatting

## Metadata

- Author: Mildenhall et al. (NeRF); Kerbl, Kopanas, Leimkühler, Drettakis (3DGS, INRIA)
- Title: NeRF: Representing Scenes as Neural Radiance Fields / 3D Gaussian Splatting for Real-Time Radiance Field Rendering
- Type: 학회 논문 (ECCV 2020 / ACM ToG SIGGRAPH 2023)
- Published: NeRF 2020; 3DGS 2023-08
- Accessed: 2026-06-06
- URL:
  - NeRF: https://arxiv.org/abs/2003.08934
  - 3DGS: https://arxiv.org/abs/2308.04079
  - 3DGS 프로젝트: https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/
  - Survey on 3D Gaussian Splatting: https://arxiv.org/abs/2401.03890
  - 3DGS in Robotics (survey): https://arxiv.org/abs/2410.12262

## Summary

둘 다 다수의 2D 이미지로부터 3D 장면을 복원해 novel-view synthesis를 수행. NeRF는 MLP로 연속 표현 + volumetric ray-marching, 3DGS는 명시적 3D Gaussian + tile-based rasterization.

## Key Claims

- NeRF: 장면을 좌표→(색,밀도) 매핑 MLP로 표현, volume rendering으로 새 시점 합성. 품질 높으나 학습·렌더 매우 느림(샘플링 비용).
- 3DGS: 장면을 학습 가능한 anisotropic 3D Gaussian point cloud로 표현. 미분가능 splatting + tile rasterizer로 1080p 실시간 렌더 + SOTA 품질, 경쟁력 있는 학습 시간.
- 3DGS는 NeRF 최상위 품질에 필적하면서 실시간 렌더가 핵심 강점.

## Useful Details

- NeRF 입력: 5D (3D 위치 + 2D 시점방향). positional encoding으로 고주파 디테일 복원.
- 3DGS 표현: 각 Gaussian = 위치, 공분산, 색(SH), 불투명도. explicit → 편집·실시간 유리.

## Recent Developments (2024–2025)

- **동적 장면 확장**: deformable 3D Gaussian — canonical space에서 Gaussian을 학습하고 별도 deformation field로 시공간 변형을 모델링(annealing smoothing으로 시간 일관성↑). 4D Gaussian Splatting 계열이 실시간 동적 장면 렌더로 발전 → "정적 장면 한정" 한계를 직접 공략.
- **로봇 적용 확산**: 3DGS in Robotics survey(arXiv:2410.12262)가 자율주행 도시 장면 복원·scene understanding·manipulation 자산 생성 등 Physical AI 응용을 정리.
- **종합 survey**: arXiv:2401.03890이 explicit 표현·실시간 렌더·editability를 NeRF 대비 강점으로 체계화.

## Limits And Risks

- 원형 NeRF/3DGS는 정적 장면·다시점 캡처 가정. 동적·반사·투명은 위 deformable/4D 변형으로 일부 완화되나 여전히 활성 연구.
- 3DGS는 메모리·저장 큼. NeRF 변형 다수 존재(Instant-NGP 등)로 일반화 시 주의.

## Related Wiki Pages

- [3D Reconstruction: NeRF & Gaussian Splatting](../../wiki/concepts/cv/3d-reconstruction-nerf-gs.md)
