# Source Note: Model Context Protocol

## Metadata

- ID: ACB-08
- Original file: `8. Model Context Protocol.pdf`
- Pages extracted: 6
- Imported: 2026-06-01

## Summary

This lecture introduces MCP as a standardized protocol that lets AI agents connect to external systems through a common interface. It compares MCP to an AI-oriented USB interface: the agent can use tools without needing to understand each service's internal API integration.

The lecture also notes a tradeoff. Tool abundance can create context explosion because the agent must infer which tool is appropriate. The practical exercise involves cloning AgentMEMO, defining an input schema with an agent, implementing FastMCP tools, and verifying tool calls against a local server and SQLite-backed repository.

## Key Claims

- MCP reduces repeated connector analysis and integration cost.
- MCP encapsulates tool behavior so the agent can focus on task-level use.
- Too many exposed tools increase tool-selection burden and context size.
- For memory-like systems, read and append tools are safer than unrestricted execution tools.

## Wiki Extraction

- [Model Context Protocol](../../wiki/concepts/model-context-protocol.md)
- [LLM Maintenance](../../wiki/workflows/maintenance.md)
