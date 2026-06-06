# Plan Mode

## Definition

Plan Mode is a read-only planning phase. The agent can inspect files, search, reason, and write a plan artifact, but it does not implement or mutate the target system until the plan is reviewed.

## Output Artifacts

- Analysis of the request.
- Decomposition into tasks.
- Implementation plan.
- TODO checklist.
- Review of the plan.
- Revised plan after critique.

## Why It Fits LLM Wiki

LLM Wiki ingestion benefits from a planning phase. Before creating pages, the maintainer should identify source type, target concepts, page placement, and risks. This prevents the wiki from becoming a pile of unrelated summaries.

## Source Notes

- [ACB-04](../../sources/agentic-coding-basics/04-plan-mode-sequential-and-parallel-agents.md)
- [ACB-05](../../sources/agentic-coding-basics/05-agent-specifications.md)
