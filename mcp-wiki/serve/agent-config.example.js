// Agent provider preset for the in-site chatbot (Wiki Guide).
//
// 이 파일은 템플릿이다. clone 후 `agent-config.js`로 복사해 본인 값으로 채워라:
//     cp agent-config.example.js agent-config.js
// build_site.py가 agent-config.js를 site/로 복사한다(없으면 이 공란 example을 복사).
//
// 중요: API 키는 여기 두지 마라. 키는 사이트의 ⚙ 설정에서 입력 → 브라우저 localStorage에만 저장된다.
//       (브라우저 직접 호출이라 키가 클라이언트에 노출됨 — 개인/로컬 용도 전제.)
//
// provider: "" | "anthropic" | "openai"   (openai는 OpenAI 호환 엔드포인트 포함: Ollama, groq 등)
// model:    provider의 모델 id            (예: "claude-sonnet-4-6", "gpt-4o-mini")
// endpoint: 선택. OpenAI 호환 base URL 등  (비우면 기본 엔드포인트)

window.AGENT_CONFIG = {
  provider: "",
  model: "",
  endpoint: ""
};
