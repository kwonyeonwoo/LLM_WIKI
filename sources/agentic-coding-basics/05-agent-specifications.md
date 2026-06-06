# Source Note: Agent Specifications

## Metadata

- ID: ACB-05
- Original file: `5. Agent Specifications.pdf`
- Pages extracted: 15
- Imported: 2026-06-01

## Summary

This lecture defines a planner-reviewer style agent pipeline. The plan-mode pipeline starts from an input prompt, then performs analysis, decomposition, planning, TODO generation, review, plan rewrite, and final output production.

Agent specifications are framed as structured definitions containing system prompt, context, inputs, outputs, session ID, project information, and handoff data. The lecture emphasizes that each agent should have a role and explicit input/output expectations.

## Key Claims

- Planner agents analyze goals, constraints, task decomposition, order, dependencies, inputs, outputs, implementation methods, and acceptance criteria.
- Reviewer agents validate TODO completeness, evaluate technical feasibility, check dependency order, identify ambiguity, score outputs, and propose concrete improvements.
- Handoff files such as `Plan.md`, `Review.md`, `Revised_Plan.md`, and `Final_TODO.md` make the pipeline auditable.
- Agent system prompts can be passed directly through CLI features or indirectly through Markdown context files.

## Wiki Extraction

- [Agent Specification](../../wiki/concepts/agent-specification.md)
- [Raw Item To Wiki Pages Pipeline](../../wiki/pipelines/raw-item-to-wiki-pages.md)
