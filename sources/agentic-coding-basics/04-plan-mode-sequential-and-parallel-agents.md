# Source Note: Plan Mode, Sequential And Parallel Agents

## Metadata

- ID: ACB-04
- Original file: `4. Plan_mode Sequential and Parallel agents.pdf`
- Pages extracted: 6
- Imported: 2026-06-01

## Summary

This lecture focuses on planning as a separate mode from implementation. Plan Mode is described as a read-only phase where the agent analyzes, searches, and writes planning artifacts but does not modify production files. The user reviews the plan before implementation begins.

The lecture also introduces handoff Markdown files as pipeline outputs. A pipeline can produce a plan, a review of the plan, a revised plan, and a TODO checklist. The handoff files make agent work inspectable and reusable.

## Key Claims

- Planning and implementation should be separated when requirements are still uncertain.
- Sequential agents depend on explicit handoff documents.
- Parallel agents can help when independent research or reviews are needed.
- Pipeline artifacts should be reusable Markdown files, not hidden chat state.

## Wiki Extraction

- [Plan Mode](../../wiki/concepts/plan-mode.md)
- [Raw Item To Wiki Pages Pipeline](../../wiki/pipelines/raw-item-to-wiki-pages.md)
