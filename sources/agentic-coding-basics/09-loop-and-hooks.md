# Source Note: Loop And Hooks

## Metadata

- ID: ACB-09
- Original file: `9. Loop and Hooks.pdf`
- Pages extracted: 5
- Imported: 2026-06-01

## Summary

This lecture describes hooks as scripts or actions that run at specific moments in an agent lifecycle. Events include user prompt submission, before and after tool use, permission requests, stop events, and session start or resume.

The main idea is to use hooks to make parts of agent behavior deterministic: logging tool use, checking knowledge bases before answering, validating completion at stop time, or triggering another agent after a task completes.

## Key Claims

- Hooks can reduce probabilistic failure by enforcing deterministic checks.
- Post-tool hooks are useful for logs.
- User-prompt hooks can check whether a knowledge base already contains relevant information.
- Stop hooks can validate that completion commands exit successfully before the agent reports done.
- Loops and scheduled checks can be expensive if they trigger read/write LLM work too often.

## Wiki Extraction

- [Loop And Hooks](../../wiki/concepts/loop-and-hooks.md)
- [LLM Maintenance](../../wiki/workflows/maintenance.md)
