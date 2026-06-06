# LLM Wiki Schema

## Purpose

This schema defines the operating structure of the repository. It is the markdown-only equivalent of a database schema and agent configuration.

## Top-Level Files

| File | Role |
| --- | --- |
| `README.md` | User-facing entry point |
| `AGENTS.md` | Maintainer behavior and operating rules |
| `index.md` | Navigation index and page registry |
| `log.md` | Append-only wiki change log |
| `TASK.md` | Current contract and done conditions |
| `journal.md` | Append-only work journal |

## Directories

| Directory | Role |
| --- | --- |
| `inbox/` | Unprocessed user-provided raw items |
| `sources/` | Source notes and source packs |
| `wiki/concepts/` | Stable concept pages |
| `wiki/workflows/` | Repeatable procedures |
| `wiki/pipelines/` | Multi-stage transformation pipelines |
| `wiki/schema/` | Repository operating schema |
| `wiki/analyses/` | Syntheses and query results |
| `templates/` | Markdown templates |
| `submissions/` | Generated submission archives and manifests |

## Page Naming

- Use lowercase kebab-case.
- Prefer descriptive names over abbreviations.
- Keep original source IDs in source notes, not concept page filenames.

## Source Note Required Fields

- ID
- Original title or filename
- Source type
- Import date
- Summary
- Key claims
- Wiki extraction links
- Limits, risks, or open questions

## Concept Page Required Fields

- Definition
- Why it matters or relation to the wiki
- Rules, examples, or comparison
- Failure modes when relevant
- Source notes
- Related links when useful

## Maintenance Invariants

- Every source note must be reachable from `index.md`.
- Every concept page must be reachable from `index.md`.
- Every ingest or structural change must be recorded in `log.md`.
- `journal.md` is append-only.
- Strong claims should link to source notes.
- Markdown-only means no required code, database, hidden index, or executable runtime.
