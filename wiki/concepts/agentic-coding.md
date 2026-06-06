# Agentic Coding

## Definition

Agentic coding is a structured way to use AI coding agents as participants in a software development workflow. It is not just asking an LLM to write code; it assigns roles, decomposes work, tracks handoffs, verifies outputs, and preserves state through files or sessions.

## Relation To Vibe Coding

Vibe coding uses natural-language goals and constraints to quickly generate working artifacts. Its weakness is that it can skip requirements, verification, and system boundaries. Agentic coding tries to repair that weakness by adding SDLC artifacts, agent roles, handoff files, and validation loops.

## Core Elements

- Clear user request or system request.
- Requirements and constraints before implementation.
- Planner, reviewer, coder, tester, or other role-specific agents.
- Markdown handoff documents.
- Explicit acceptance criteria.
- Verification commands or review criteria.
- Logs or journals that preserve what happened.

## Failure Modes

- Treating "code generated" as "system solved".
- Giving agents excessive permissions before requirements are clear.
- Allowing an agent to revise its own done criteria.
- Hiding important state in chat instead of writing handoff artifacts.

## Source Notes

- [ACB-01](../../sources/agentic-coding-basics/01-vibe-coding-and-agent-coding.md)
- [ACB-02](../../sources/agentic-coding-basics/02-sdlc-pipeline-in-vibe-coding.md)
- [ACB-03](../../sources/agentic-coding-basics/03-agents-subprocess-calling.md)
