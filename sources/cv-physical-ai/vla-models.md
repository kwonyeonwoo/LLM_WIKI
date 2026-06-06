# Source Note: Vision-Language-Action (VLA) Models

## Metadata

- Author: Brohan et al. (RT-2); Kim et al. (OpenVLA); Black et al. (π0); Open X-Embodiment Collaboration
- Title: RT-2 / OpenVLA / π0 / Open X-Embodiment
- Type: 학회·기술 논문
- Published: RT-2 2023-07; OXE 2023-10; OpenVLA 2024-06; π0 2024-10
- Accessed: 2026-06-06
- URL:
  - RT-2: https://arxiv.org/abs/2307.15818
  - OpenVLA: https://arxiv.org/abs/2406.09246
  - π0: https://arxiv.org/abs/2410.24164
  - Open X-Embodiment: https://arxiv.org/abs/2310.08864

## Summary

VLA = vision foundation model + LLM/VLM 위에 action head를 얹어, 이미지+언어 지시를 받아 로봇 행동을 직접 출력하는 end-to-end 정책. CV와 Physical AI의 교집합.

## Key Claims

- RT-2: 인터넷 규모 VLM을 end-to-end 정책으로 통합, 로봇 행동을 텍스트 토큰으로 표현, 웹 데이터 + 로봇 시연 co-training. 연속 행동값을 차원당 256 bin으로 균등 양자화.
- OpenVLA: 7B 파라미터 오픈소스 VLA, Open X-Embodiment(OXE) 데이터셋의 ~97만(near 1M) 실제 로봇 에피소드로 학습. action discretization 방식 채택.
- OXE: 21개 기관, 22개 embodiment의 로봇 데이터를 통합.
- π0: PaliGemma VLM에 action expert를 붙여 flow matching으로 연속 행동 생성 → 정밀·유연한 manipulation.

## Useful Details

- 행동 표현 두 갈래: (1) 토큰 양자화(RT-2, OpenVLA), (2) 연속 생성(diffusion/flow matching, π0).
- generalist 정책: 다양한 로봇·태스크에 전이. 웹 사전학습 지식이 미본 객체·지시 일반화에 기여.

## Limits And Risks

- 추론 지연·실시간성 제약(대형 VLM). 실로봇 안전성·실패모드 평가 미성숙.
- 데이터 편향(embodiment 분포). sim/real gap 잔존.

## Related Wiki Pages

- [VLA Models](../../wiki/concepts/intersection/vla-models.md)
