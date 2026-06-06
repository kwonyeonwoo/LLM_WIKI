# Agentic Coding Basics Synthesis For LLM Wiki

## Thesis

Agentic Coding Basics turns the LLM Wiki from a passive note collection into a maintained agent workspace. The key move is to treat wiki maintenance as a pipeline with contracts, handoffs, review, and logs.

## Mapping From Lecture Ideas To Repository Components

| Lecture Idea | Wiki Implementation |
| --- | --- |
| Spec-first development | `TASK.md`, schema, source note templates |
| Plan Mode | Page planning before writing |
| Handoff Markdown | Source notes, concept pages, log entries |
| Agent specifications | Role definitions in pipeline and schema |
| Agent pool and orchestrator | `AGENTS.md` plus role table in pipeline |
| Harness engineering | Contract, procedure, journal, preference files |
| MCP | Narrow read/append interface idea, without adding runtime dependency |
| Hooks | Written checklists at session start, before update, after update, and stop |

## Design Decision

This repository intentionally avoids executable scripts, JSON agent pools, vector databases, and MCP servers. That is a limitation, but it matches the markdown-only requirement. The pipeline is therefore implemented as documented procedures and durable Markdown artifacts.

## Weak Point

The biggest weakness is that checks are procedural, not enforced by code. Broken links, stale claims, and missing source references can still happen. The mitigation is explicit linting and maintenance checklists, not automation.

## Related

- [LLM Wiki Schema](../schema/llm-wiki-schema.md)
- [Raw Item To Wiki Pages Pipeline](../pipelines/raw-item-to-wiki-pages.md)
- [LLM Maintenance](../workflows/maintenance.md)
