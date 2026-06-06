# LLM Maintenance

## Purpose

LLM maintenance is the set of rules that keeps the wiki reliable after pages are created. It adapts the Agentic Coding Basics ideas of contract, procedure, journal, hooks, and bounded loops.

## Maintenance Contract

The wiki is maintained when:

- New raw items produce source notes.
- Source notes produce or update wiki pages.
- `index.md` reflects current pages.
- `log.md` records changes.
- `journal.md` records work sessions.
- Unresolved issues are visible in `TASK.md` or page-level open questions.

## Session Start Checklist

1. Read `AGENTS.md`.
2. Read `index.md`.
3. Read the latest entries in `log.md` and `journal.md`.
4. Identify the requested workflow: ingest, query, lint, or maintenance.

## Stop Checklist

1. Confirm changed pages are linked from `index.md`.
2. Confirm source notes exist for source-backed claims.
3. Append `log.md`.
4. Append `journal.md`.
5. If work remains, add it to `TASK.md`.

## Hook Analogs

This markdown-only wiki does not run executable hooks. Instead, it uses written hook analogs.

| Agent Event | Markdown Hook |
| --- | --- |
| User prompt submitted | Check `index.md` before answering |
| Before file update | Identify affected source and wiki pages |
| After file update | Update links and log |
| Permission or uncertainty | Record open question instead of guessing |
| Stop | Run the stop checklist |

## Bounded Loop Rule

Do not repeatedly rewrite the same page without a new source, new user question, or explicit lint finding. If the same issue remains after three attempts, record the blocker in `TASK.md` and stop.

## Related

- [LLM Wiki Schema](../schema/llm-wiki-schema.md)
- [Ingest Workflow](ingest.md)
- [Raw Item To Wiki Pages Pipeline](../pipelines/raw-item-to-wiki-pages.md)
