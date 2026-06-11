# VLA Models (Vision-Language-Action)

Domain: intersection (cv × physical-ai) · Maturity: emerging

## Definition

VLA(Vision-Language-Action) 모델은 vision foundation model + LLM/VLM 위에 **action head**를 얹어, 이미지와 언어 지시를 받아 로봇 행동을 직접 출력하는 end-to-end 정책이다. 컴퓨터비전과 피지컬 AI가 만나는 핵심 영역.

## Key Points

- **RT-2**: 인터넷 규모 VLM을 end-to-end 정책으로 통합. 로봇 행동을 텍스트 토큰으로 표현, 웹 데이터 + 로봇 시연 co-training. 연속 행동값을 차원당 256 bin으로 양자화.
- **OpenVLA**: 7B 파라미터 오픈소스 VLA. Open X-Embodiment(OXE)의 ~97만 실제 로봇 에피소드로 학습.
- **Open X-Embodiment**: 21개 기관·22개 embodiment 로봇 데이터 통합 → generalist 정책 학습 기반.
- **π0**: PaliGemma VLM에 action expert를 붙여 flow matching으로 연속 행동 생성 → 정밀·유연한 manipulation.
- **행동 표현 두 갈래**: (1) 토큰 양자화(RT-2, OpenVLA), (2) 연속 생성(diffusion/flow matching, π0).
- **CV 의존**: vision foundation model(CLIP 류) 사전학습 지식이 미본 객체·지시 일반화에 기여.
- **최신(2024~) 3축**: (1) open-world 일반화(π0.5), (2) 비디오·웹지식 결합(GR-2), (3) 추론 효율화 — VLA가 커지며 실시간 제어 병목 해소가 핵심 과제([Efficient VLA survey](https://arxiv.org/abs/2510.24795)).

## Evidence

- [Source: VLA Models](../../../sources/cv-physical-ai/vla-models.md)
- RT-2 — https://arxiv.org/abs/2307.15818
- OpenVLA — https://arxiv.org/abs/2406.09246
- π0 — https://arxiv.org/abs/2410.24164
- Efficient VLA Models (survey) — https://arxiv.org/abs/2510.24795

## Conflicts / Open Questions

- 대형 VLM 추론 지연 → 실시간 제어 제약. 실로봇 안전성·실패모드 평가 미성숙.
- embodiment 데이터 편향, sim/real gap 잔존.

## Related

- [Vision Foundation Models](../cv/vision-foundation-models.md)
- [Sim-to-Real Transfer](../physical-ai/sim-to-real-transfer.md)
- [Segmentation: SAM Family](../cv/segmentation-sam-family.md)
- [Index](../../../index.md)
