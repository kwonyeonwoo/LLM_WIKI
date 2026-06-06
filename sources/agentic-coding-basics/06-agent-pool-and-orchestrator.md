# Source Note: Agent Pool And Orchestrator

## Metadata

- ID: ACB-06
- Original file: `6. Agent pool and Orchestrator.pdf`
- Pages extracted: 6
- Imported: 2026-06-01

## Summary

This lecture generalizes a fixed pipeline into an agent pool and orchestrator model. Each agent has state, inputs, outputs, and time. Fixed workflow pipelines can be hard to reuse, so agents can be registered in a pool and selected dynamically by an orchestrator.

The lecture proposes agent definitions containing ID, role, system prompt, input schema, output schema, tools, constraints, max attempts, timeout, and sandbox level. The orchestrator reads the pool and chooses agents based on the goal.

## Key Claims

- Agents should expose explicit state such as idle, running, completed, or failed.
- A reusable agent pool reduces the burden on a single fixed workflow.
- Context files such as `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` constrain agent behavior.
- Orchestrators should record round history and outputs so the workflow can be inspected.

## Wiki Extraction

- [Agent Pool And Orchestrator](../../wiki/concepts/agent-pool-and-orchestrator.md)
- [Agent Specification](../../wiki/concepts/agent-specification.md)
