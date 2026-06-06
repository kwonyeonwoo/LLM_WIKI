# Source Note: Sim-to-Real Transfer

## Metadata

- Author: Zhao et al. (survey 2020); Tobin et al. (domain randomization); survey 2025 (foundation models)
- Title: Sim-to-Real Transfer in Deep RL for Robotics: a Survey 외
- Type: peer-reviewed survey + 학회 논문
- Published: 2017 / 2020 / 2025
- Accessed: 2026-06-06
- URL:
  - Survey 2020: https://arxiv.org/abs/2009.13303
  - Domain Randomization (Tobin et al. 2017): https://arxiv.org/abs/1703.06907
  - Survey 2025 (foundation models): https://arxiv.org/abs/2502.13187

## Summary

Sim-to-real = 시뮬레이터에서 학습한 정책을 실로봇으로 전이. 시뮬레이션은 무한 데이터·안전을 제공하나, sim/real gap이 전이 시 성능을 떨어뜨림.

## Key Claims

- 주요 방법: domain randomization, domain adaptation, imitation learning, meta-learning, knowledge distillation.
- Domain randomization: 시뮬레이터 파라미터(색·텍스처·동역학)를 무작위화해 실세계를 분포의 한 사례로 포함 → 강건한 정책. 로봇·자율주행에서 효과 입증.
- 2025 survey: MDP 프레임 안에서 해법을 분류, foundation model 활용으로 진보하나 robustness·scalability·평가가 여전히 난제.

## Useful Details

- gap 원인: 동역학 불일치, 센서 노이즈, 시각적 외형 차이.
- 평가 난점: 실로봇 시도 비용·안전 → 표준 벤치마크 부족.

## Limits And Risks

- randomization 과하면 학습 어려움·보수적 정책. 적절 범위 튜닝 필요.
- survey마다 분류 체계 상이 → 용어 통일 주의.

## Related Wiki Pages

- [Sim-to-Real Transfer](../../wiki/concepts/physical-ai/sim-to-real-transfer.md)
