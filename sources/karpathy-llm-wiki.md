# Source Note: Karpathy LLM Wiki

## Metadata

- Author: Andrej Karpathy
- Title: LLM Wiki
- Type: GitHub Gist
- Created: 2026-04-04
- Accessed: 2026-05-18
- URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Summary

Karpathy describes LLM Wiki as a pattern for building personal knowledge bases with LLM agents. The document is intentionally abstract: it is not a finished application, but a prompt-like idea file meant to be adapted by an agent such as Codex, Claude Code, OpenCode, or similar tools.

The central claim is that common RAG workflows repeatedly retrieve raw fragments at question time, while an LLM Wiki accumulates knowledge into a persistent Markdown artifact. When a new source is added, the LLM reads it, extracts key information, updates relevant pages, records contradictions, and maintains cross-references. The wiki becomes a compiled layer between the user and the raw sources.

Karpathy proposes three layers:

- Raw sources: immutable source materials.
- Wiki: LLM-generated Markdown pages.
- Schema: an instruction file such as `CLAUDE.md` or `AGENTS.md` that defines conventions and workflows.

He also describes three operations:

- Ingest: add a new source and update the wiki.
- Query: answer questions by reading the wiki and optionally saving useful answers back into it.
- Lint: periodically inspect the wiki for stale claims, missing links, contradictions, orphan pages, and gaps.

## Importance

This source is the seed document for this repository. It defines the operating pattern: keep the system simple, use Markdown as the durable artifact, and let the LLM handle maintenance work that humans usually avoid.

## Limits And Risks

- The gist is a concept, not a production architecture.
- It assumes the LLM can reliably maintain links, summaries, and contradictions, which needs verification.
- It works best at personal or moderate scale. Large organizational knowledge bases may need stronger search, permissions, transaction control, and review workflows.
- If errors enter the wiki, later pages can amplify them unless linting and source checks are routine.

## Related Wiki Pages

- [LLM Wiki](../wiki/concepts/llm-wiki.md)
- [RAG vs LLM Wiki](../wiki/concepts/rag-vs-llm-wiki.md)
- [Persistent Knowledge Artifact](../wiki/concepts/persistent-knowledge-artifact.md)
- [Markdown-Only Constraint](../wiki/concepts/markdown-only-constraint.md)
