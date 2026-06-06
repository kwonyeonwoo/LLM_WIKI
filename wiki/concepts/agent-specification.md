# Agent Specification

## Definition

An agent specification is a structured description of an agent's role, context, inputs, outputs, tools, constraints, and handoff responsibilities.

## Minimal Fields

| Field | Purpose |
| --- | --- |
| `id` | Stable identifier for the agent or role |
| `role` | One-line responsibility |
| `system_prompt` | Behavioral instruction |
| `inputs` | Required inputs and expected format |
| `outputs` | Files or records the agent must produce |
| `constraints` | Permissions, max attempts, timeout, sandbox |
| `handoff` | What the next stage receives |

## LLM Wiki Agent Roles

- Intake agent: identifies source metadata and quality.
- Extractor agent: finds claims, concepts, entities, and open questions.
- Page builder agent: writes or updates wiki pages.
- Reviewer agent: checks links, sources, contradictions, and schema compliance.
- Maintainer agent: updates index, log, and stale sections.

## Source Notes

- [ACB-05](../../sources/agentic-coding-basics/05-agent-specifications.md)
- [ACB-06](../../sources/agentic-coding-basics/06-agent-pool-and-orchestrator.md)
