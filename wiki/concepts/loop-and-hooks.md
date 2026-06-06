# Loop And Hooks

## Definition

Hooks are actions that run at specific lifecycle events of an agent. Loops are repeated agent actions that continue until a condition is met.

## Useful Events

- User prompt submitted.
- Before tool use.
- After tool use.
- Permission requested.
- Session started or resumed.
- Turn stopping.

## LLM Wiki Use

In a markdown-only repository, hooks are represented as written checks rather than executable scripts. For example, before answering a query, the maintainer must check `index.md`; after ingest, the maintainer must update `log.md`; before stopping, the maintainer must verify links and source notes.

## Risk

Automated loops can waste money or repeatedly mutate files. For this repository, loops should be bounded by [TASK.md](../../TASK.md) and recorded in [journal.md](../../journal.md).

## Source Notes

- [ACB-09](../../sources/agentic-coding-basics/09-loop-and-hooks.md)
