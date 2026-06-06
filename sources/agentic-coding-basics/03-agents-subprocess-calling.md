# Source Note: Agents Subprocess Calling

## Metadata

- ID: ACB-03
- Original file: `3. Agents subprocess calling.pdf`
- Pages extracted: 15
- Imported: 2026-06-01

## Summary

This lecture moves from single-tool AI coding to agent systems. It emphasizes that AI can produce code, but a reliable system needs structured decomposition, permissions, session control, and subprocess-based CLI invocation.

The lecture compares terminal invocation and Python subprocess invocation. Claude and Codex can receive prompts via stdin in the shown examples, while Gemini is shown with prompt text in command arguments. It also covers `subprocess.run()` parameters such as input, output capture, encoding, and timeout.

## Key Claims

- Agentic coding requires explicit control over permissions and execution boundaries.
- High-permission modes such as YOLO or bypass modes reduce friction but can remove meaningful user control.
- CLI agents return different JSON shapes, so an orchestrator should normalize outputs.
- Session persistence matters when an agent must continue prior work.
- Local file access is not automatically solved by subprocess invocation; the workflow must explicitly provide paths, context, or sandbox access.

## Wiki Extraction

- [Agent Subprocess Calling](../../wiki/concepts/agent-subprocess-calling.md)
- [Agentic Coding](../../wiki/concepts/agentic-coding.md)

## Risk Notes

The lecture intentionally shows dangerous permission flags as reminders. This wiki treats them as risk examples, not recommended defaults.
