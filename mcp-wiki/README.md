---
title: MCP 기반 Wiki Tool — 프로젝트 README
status: active
date: 2026-06-06
updated: 2026-06-11
tags: [readme, mcp-wiki, computer-vision, physical-ai, usage]
description: 컴퓨터비전/피지컬 AI 지식을 다루는 MCP 기반 wiki tool의 개요, 제공 MCP tool 목록과 사용법, 클라이언트 설정 및 프로젝트 실행 방법을 설명하는 README.
type: readme
---

# MCP 기반 Wiki Tool (Computer Vision / Physical AI)

markdown-only LLM Wiki를 **MCP(Model Context Protocol) 서버**로 노출한 프로젝트다. 컴퓨터비전 / 피지컬 AI 지식을 표준 tool 호출로 검색·읽기·생성·갱신·점검한다.

> 상태: MCP 서버 6 tool + 정적 사이트(Stack A) 구현됨. 편집 인터랙션이 강한 동적 웹앱(Stack B)은 필요 시 이어서 진행.

구성:
- `mcp_wiki/` — MCP 서버 (6 tool, stdio)
- `serve/` — 정적 사이트 빌더 (그래프·페이지·검색)
- `skills/wiki-keeper/` — 재사용 가능한 Claude 스킬

관련 설계 문서:
- [지식 도메인 정의](01-knowledge-domain.md) — 무엇을 담는가 (CV / Physical AI)
- [의사결정 라운드](02-decision-rounds.md) — 왜 MCP tool로 가는가
- [PRD / 사양서](03-prd.md) — 무엇을 만드는가
- [에이전트 사양](04-agent-spec.md) — 누가 운영하는가 (권한·역할)
- [하네스 & 스킬](05-harness-and-skills.md) — 재사용 실행 구조
- [접근 계획](06-access-plan.md) — 어떻게 열람·학습·활용하는가 (표면 2분할)
- [상위 위키 운영 규칙](../AGENTS.md)

## 1. 이 프로젝트가 푸는 문제

기존 위키는 LLM 자유 편집에 의존해 절차가 흔들리고, index 갱신·링크 무결성이 수동이라 누락이 잦았다. 이 프로젝트는 위키 운영을 **정의된 MCP tool**로 강제해 일관성·검증 가능성을 확보한다. source of truth는 여전히 markdown 파일이다.

### 1.1 MCP 서버 — agent와 tool을 잇는 연결 계층

MCP 서버(`mcp_wiki/server.py`)는 **LLM agent와 markdown 파일 사이의 연결 계층**이다. agent는 파일을 직접 만지지 않는다. 표준 MCP tool을 호출하고, 서버가 그 호출을 받아 markdown을 읽고 쓴 뒤 결과를 돌려준다.

```
사용자 자연어
   │
LLM agent (Claude)           ← 무엇을 할지 결정
   │  tool 호출 (MCP)
MCP 클라이언트 (Claude Desktop 등)
   │  stdio transport
MCP 서버 (mcp_wiki, 6 tool)  ← 절차·불변조건 강제
   │  읽기/쓰기
markdown 파일 (source of truth) + index.md / log.md 자동 반영
```

이 연결 계층이 필요한 이유:

- **절차 강제** — agent가 위키를 자유 편집하면 세션마다 절차가 흔들린다. tool 경계가 "검색→읽기→쓰기→점검" 루프를 강제해 일관성을 만든다.
- **검증 가능** — 모든 변경이 tool을 경유하므로 `index.md` 등록·`log.md` append가 자동으로 따라온다. agent의 자기보고가 아니라 결정적 동작.
- **이식성** — stdio transport + tool 스키마 노출이라 Claude Desktop이든 다른 MCP 클라이언트든 같은 인터페이스로 위키에 연결된다. agent를 바꿔도 tool 계약은 그대로.
- **안전 경계** — `wiki/` 밖 쓰기·덮어쓰기·비-kebab 이름을 서버가 거부([§2.1](#21-왜-이-tool들이-필요한가-tool-근거), [PRD §6](03-prd.md)). agent 실수가 파일을 깨지 못한다.

누가 이 tool들을 호출하는가(편집자/챗봇 역할·권한)는 [에이전트 사양](04-agent-spec.md) 참고.

## 2. 제공하는 MCP Tool

MVP 6종. 핵심 루프 = 검색 → 읽기 → 목록 → 생성 → 갱신 → 점검.

| tool | 종류 | 기능 |
|---|---|---|
| `search_wiki` | read | 키워드로 페이지 본문/제목 검색, 발췌 반환 |
| `read_page` | read | 경로로 단일 페이지(frontmatter+본문) 읽기 |
| `list_pages` | read | 도메인/디렉터리별 페이지 목록 |
| `create_page` | write | 새 페이지 생성 + `index.md` 자동 등록 + `log.md` append |
| `update_page` | write | 기존 페이지 갱신 + index/갱신일 반영 |
| `link_check` | maintenance | 끊긴 내부 링크·색인 누락 탐지 리포트 |

전체 입출력 스키마: [PRD §6](03-prd.md).

### 2.1 왜 이 tool들이 필요한가 (tool 근거)

각 tool은 "agent가 위키를 자유 편집할 때 생기던 문제"를 하나씩 제거한다. tool이 곧 **강제되는 절차**다.

- **`search_wiki`** — agent가 답하기 전에 위키에 이미 있는 지식을 찾게 한다. 없으면 매번 처음부터 재생성/환각 → 중복 페이지·모순 발생. 검색이 "먼저 위키를 봐라"를 강제한다.
- **`read_page`** — 전체 파일을 컨텍스트에 쏟지 않고 필요한 한 페이지만 정확히 읽게 한다. 토큰 절약 + 인용 정확도. 경로 기반이라 agent가 추측한 파일을 여는 실수를 차단.
- **`list_pages`** — 도메인/디렉터리 단위로 "무엇이 있는지" 파악. 새 페이지를 만들기 전 중복 여부를 확인하는 진입점. 그래프/사이트 빌드의 메타 소스이기도 함.
- **`create_page`** — 단순 파일쓰기가 아니라 **생성 + index.md 자동 등록 + log.md append**를 한 번에 원자적으로 묶는다. 수동 편집 시 가장 흔한 누락(색인 미반영)을 구조적으로 제거. kebab-case·`wiki/` 스코프·덮어쓰기 금지를 불변조건으로 강제.
- **`update_page`** — 기존 페이지 갱신을 log에 자동 기록(라인 delta 포함)해 변경 추적성을 보장. create와 분리해 "실수로 덮어쓰기"를 막음.
- **`link_check`** — markdown-only 구조의 최대 약점인 링크 무결성·색인 누락을 기계적으로 점검. agent의 자기보고가 아니라 결정적 스캔 결과를 돌려줘 검증 가능.

핵심: read tool = "위키를 근거로 말하게" 강제, write tool = "쓰면 색인·로그가 따라오게" 강제, maintenance tool = "사람·agent 자기보고 대신 결정적 점검". 이 세 묶음이 [§1의 문제](#1-이-프로젝트가-푸는-문제)를 직접 해소한다.

## 3. Tool 사용법

자연어 요청 → LLM이 적절한 tool 선택 호출. 예시 흐름:

**(a) 질의**
```
사용자: "SAM 계열 segmentation 페이지 찾아줘"
→ search_wiki(query="SAM segmentation", domain="cv")
→ read_page(path="wiki/concepts/cv/segmentation-sam-family.md")
```

**(b) 새 지식 추가**
```
사용자: "VLA 모델 개념 페이지 만들어줘"
→ create_page(
     path="wiki/concepts/intersection/vla-models.md",
     title="VLA Models",
     domain="intersection",
     content="...개념 요약..."
   )
→ index.md 자동 갱신 + log.md append
```

**(c) 무결성 점검**
```
사용자: "위키 링크 점검해줘"
→ link_check()
→ 끊긴 링크·색인 누락 리포트 반환
```

tool 호출 시 강제되는 불변조건: 경로는 `wiki/` 내부, 이름은 kebab-case, 내부 링크는 상대 경로 markdown ([PRD §6](03-prd.md)).

## 4. 프로젝트 실행 방법

> 스택: Python + 공식 MCP SDK ([Round 1](02-decision-rounds.md)).

### 4.1 설치
```bash
# 저장소 루트에서
cd mcp-wiki
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .                  # mcp SDK 포함 (pyproject.toml)
```

### 4.2 서버 단독 실행 (개발/디버그)
```bash
python -m mcp_wiki.server         # stdio transport로 대기
```

### 4.3 MCP 클라이언트 등록 (Claude Desktop 예)

설정 파일(`%APPDATA%/Claude/claude_desktop_config.json`)의 `mcpServers`에 등록:
```json
{
  "mcpServers": {
    "cv-physical-ai-wiki": {
      "command": "C:\\Users\\yeony\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
      "args": ["-m", "mcp_wiki.server"],
      "env": {
        "WIKI_ROOT": "C:\\Users\\yeony\\Documents\\LLM wiki"
      }
    }
  }
}
```
- `command`: 패키지(`pip install -e .`)가 설치된 python의 **절대 경로**. PATH의 `python`이 해당 인터프리터로 확실히 잡히면 `"python"`도 가능하나, GUI 클라이언트는 PATH가 달라질 수 있어 절대 경로 권장.
- `WIKI_ROOT`: 위키 markdown 파일들의 루트. tool은 이 경로 기준으로 읽고 쓴다.
- 등록 후 **Claude Desktop을 재시작**해야 서버가 로드된다.

### 4.4 검증
- 클라이언트에서 6개 tool이 노출되는지 확인.
- `list_pages()` 호출 → 기존 페이지 목록 반환되면 연결 성공.
- 상세 인수 기준: [PRD §8 성공 기준](03-prd.md).

### 4.5 정적 사이트 서빙 (Stack A — 시각화)

MCP 서버와 독립적으로, 같은 markdown을 그래프·페이지·검색으로 본다.

```bash
cd mcp-wiki
python serve/build_site.py                     # site/data.json + site/index.html 생성
python -m http.server -d site 8000             # http://localhost:8000
```
- **그래프 뷰**: 노드=페이지, 엣지=Related 링크, 색=도메인(cv/physical-ai/intersection/meta), 크기=연결 수.
- **페이지 뷰**: markdown 렌더 + 도메인/maturity 배지 + backlink(역참조) 패널.
- **검색·필터**: 키워드 검색, 도메인 체크박스 필터.
- 의존성 0(빌드는 stdlib). 클라이언트는 CDN의 d3 + marked 사용. 정적이라 GitHub Pages 배포 가능.
- 파일 변경 후 `build_site.py` 재실행 또는 커밋 훅/CI로 재빌드.

### 4.6 사이트 챗봇 (브라우저 내 Wiki Guide)

사이트의 **챗봇** 탭은 [Wiki Guide](04-agent-spec.md)(읽기 전용)를 브라우저에서 쓴다. 백엔드 없이 동작:

1. 질문 입력 → 로드된 위키 페이지에서 키워드로 관련 페이지 top-4 검색(client-side).
2. 그 페이지들을 context로 묶어 system 프롬프트(위키 근거로만 답, 없으면 "위키에 없음")와 함께 LLM API에 전송.
3. 답 + 근거 페이지 링크 표시(클릭 시 페이지 뷰로 이동).

**에이전트(provider)는 교체 가능.** 어댑터: `anthropic`(Claude), `openai`(OpenAI 및 호환 엔드포인트 — Ollama·groq 등 `endpoint`로). 추가 provider는 `serve/template.html`의 `callProvider`에 분기 추가.

**설정 위치:**
- `serve/agent-config.js` — provider/model/endpoint 프리셋. **로컬 전용, gitignore**(레포에 안 올라감). 없으면 빌드가 공란 `agent-config.example.js`를 복사.
- 레포는 `agent-config.example.js`를 **공란으로** 배포 → clone 후 본인이 설정:
  ```bash
  cd mcp-wiki/serve && cp agent-config.example.js agent-config.js   # provider/model 채움
  ```
- **API 키**: 파일에 두지 않는다. 사이트 ⚙ 설정에서 입력 → 브라우저 `localStorage`에만 저장.

> ⚠ 보안: 정적 사이트라 브라우저가 LLM API를 **직접 호출**한다 → API 키가 클라이언트에 노출된다. 개인/로컬 용도 전제. 공개 배포(예: GitHub Pages)에 키 넣지 마라. 다중 사용자·키 은닉이 필요하면 별도 백엔드 프록시를 둬야 한다([06 접근 계획 Stack B](06-access-plan.md)).

## 5. 저장 구조

source of truth = markdown 파일. 검색 인덱스는 파일에서 파생되는 재생성 가능 캐시 ([Round 2](02-decision-rounds.md)).

```
LLM wiki/              ← WIKI_ROOT
├─ wiki/               ← tool이 읽고 쓰는 지식 페이지
│  └─ concepts/{cv,physical-ai,intersection}/
├─ index.md            ← create tool이 자동 등록
├─ log.md              ← write 동작 append
└─ mcp-wiki/           ← 이 폴더
   ├─ mcp_wiki/        ← MCP 서버 (server.py, 6 tool)
   ├─ serve/           ← 정적 사이트 빌더 (build_site.py, template.html)
   ├─ site/            ← 빌드 산출물 (data.json, index.html)
   ├─ skills/          ← 재사용 Claude 스킬 (wiki-keeper)
   └─ pyproject.toml
```

## 6. 한계

- MVP는 키워드 검색만. 의미 검색(임베딩) 미포함 ([PRD §4](03-prd.md)).
- 페이지 삭제·동시 편집 미지원. 삭제는 수동 git.
- markdown-only 철학상 자동 정합성 보장은 `link_check` 수준까지 ([markdown-only-constraint](../wiki/concepts/markdown-only-constraint.md)).
