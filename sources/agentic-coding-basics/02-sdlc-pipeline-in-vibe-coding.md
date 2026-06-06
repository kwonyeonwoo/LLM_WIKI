# Source Note: SDLC Pipeline In Vibe Coding

## Metadata

- ID: ACB-02
- Original file: `2. SDLC pipeline in Vibe coding.pdf`
- Pages extracted: 16
- Imported: 2026-06-01

## Summary

This lecture explains why AI-assisted coding needs system analysis and SDLC discipline. It begins with CLI setup for Codex, Gemini, and Claude, then uses a randomized quicksort visualizer as a small example. The first generated result is fast and visually appealing, but the lecture points out missing requirements: richer logs and a way to understand why randomized quicksort tends toward expected `O(n log n)` behavior.

The core lesson is that incremental prompting without structured requirements becomes unplanned development. Small algorithm viewers can survive this style, but larger information systems and embedded systems require stakeholder analysis, non-functional requirements, integration planning, and failure-cost awareness.

## Key Claims

- Spec-first, code-later is a safer pattern for AI-assisted development.
- PRD, SRS, user stories, and acceptance criteria align why, what, and how before implementation.
- Vibe coding is suited to small applications; agentic coding can scale further when the user acts as orchestrator.
- Agentic coding structures can be single-agent, sequential-agent, or parallel-agent depending on task dependency.

## Useful Details

- Sequential agents require the order and dependencies to be designed in advance.
- Parallel agents are strong for independent research tasks.
- The lecture references a simple agentic coding experience tool: `https://github.com/INHA-SELAB/cse3308_easy_agent`.

## Wiki Extraction

- [SDLC And Spec-Driven Development](../../wiki/concepts/sdlc-and-spec-driven-development.md)
- [Agentic Coding](../../wiki/concepts/agentic-coding.md)
