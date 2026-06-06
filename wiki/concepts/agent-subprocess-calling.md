# Agent Subprocess Calling

## Definition

Agent subprocess calling is the pattern of invoking CLI agents from another program or orchestrator through isolated process calls. The subprocess boundary helps define inputs, outputs, timeouts, return codes, and permissions.

## Why It Matters

Subprocess calls make agent work inspectable. The orchestrator can capture stdout, stderr, exit codes, execution time, JSON output, and session identifiers. This is more controllable than leaving all work inside a single interactive chat.

## Design Rules

- Pass prompts in a way each CLI supports.
- Normalize each agent's output into a common record.
- Set timeouts.
- Capture errors instead of assuming success.
- Avoid dangerous permission modes unless the user explicitly accepts the risk.
- Make local file paths and sandbox boundaries explicit.

## LLM Wiki Use

This repository does not implement executable subprocess orchestration because the assignment asks for a markdown-only wiki. Instead, it captures the same idea as a document pipeline: each stage produces a Markdown handoff file that another agent or user can inspect.

## Source Notes

- [ACB-03](../../sources/agentic-coding-basics/03-agents-subprocess-calling.md)
