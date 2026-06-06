# Model Context Protocol

## Definition

Model Context Protocol is a standardized way for AI agents to connect with external systems and tools through a common protocol.

## LLM Wiki Interpretation

For an LLM Wiki, MCP is useful when the wiki needs durable memory, external search, file access, or append/read tools. But the markdown-only version deliberately avoids MCP as a dependency. Instead, it borrows the MCP idea of narrow, explicit interfaces.

## Tradeoff

More tools do not automatically make an agent better. Too many available tools can increase context size and tool-selection ambiguity. A wiki maintainer should expose only the operations needed for the workflow.

## Source Notes

- [ACB-08](../../sources/agentic-coding-basics/08-model-context-protocol.md)
