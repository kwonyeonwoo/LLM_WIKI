# Agent Pool And Orchestrator

## Definition

An agent pool is a reusable set of agent definitions. An orchestrator reads the pool, selects appropriate agents, routes inputs, monitors state, and records outputs.

## State Model

- `idle`: available but not running.
- `running`: processing a task.
- `completed`: produced a valid output.
- `failed`: stopped with an error or unmet acceptance criteria.
- `blocked`: needs user input or external state.

## Markdown-Only Adaptation

This repository does not use JSON pool files or executable orchestrator code. Instead, `AGENTS.md`, [LLM Wiki Schema](../schema/llm-wiki-schema.md), [Raw Item To Wiki Pages Pipeline](../pipelines/raw-item-to-wiki-pages.md), and [log.md](../../log.md) act as the pool and orchestration layer.

## Source Notes

- [ACB-06](../../sources/agentic-coding-basics/06-agent-pool-and-orchestrator.md)
