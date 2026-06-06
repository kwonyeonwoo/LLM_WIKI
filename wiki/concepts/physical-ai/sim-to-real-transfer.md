# Sim-to-Real Transfer

Domain: physical-ai · Maturity: established

## Definition

Sim-to-real transfer는 시뮬레이터에서 학습한 정책을 **실로봇으로 옮기는** 문제다. 시뮬레이션은 무한 데이터·안전을 제공하지만, 시뮬과 현실의 차이(sim/real gap)가 전이 시 성능을 떨어뜨린다.

## Key Points

- **주요 방법**: domain randomization, domain adaptation, imitation learning, meta-learning, knowledge distillation.
- **Domain randomization**: 시뮬레이터 파라미터(색·텍스처·동역학)를 무작위화해 현실을 학습 분포의 한 사례로 포함 → 강건한 정책. 로봇·자율주행에서 효과 입증.
- **gap 원인**: 동역학 불일치, 센서 노이즈, 시각적 외형 차이.
- **최신 흐름**: foundation model을 활용한 sim-to-real 진보. 그러나 robustness·scalability·평가가 여전히 핵심 난제.
- **시뮬레이터 맥락**: Isaac Sim, MuJoCo 등에서 대규모 병렬 학습 후 전이.

## Evidence

- [Source: Sim-to-Real Transfer](../../../sources/cv-physical-ai/sim-to-real.md)
- Survey 2020 — https://arxiv.org/abs/2009.13303
- Domain Randomization (Tobin et al. 2017) — https://arxiv.org/abs/1703.06907

## Conflicts / Open Questions

- randomization 과하면 학습 난이도↑·보수적 정책 → 적정 범위 튜닝 미해결.
- 실로봇 시도 비용·안전 → 표준 평가 벤치마크 부족.

## Related

- [VLA Models](../intersection/vla-models.md)
- [Sensor Fusion](sensor-fusion.md)
- [Index](../../../index.md)
