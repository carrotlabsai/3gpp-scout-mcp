---
name: 3gpp-scout
description: Hosted 3GPP MCP server for semantic search over Rel-15 through Rel-20 TS/TR (5G NR, LTE, RAN, 5G core). Connect to https://api.3gppscout.com/mcp/. No local index.
---

# 3GPP Scout

3GPP Scout is a **hosted 3GPP MCP server**. Use it when the user needs 3GPP technical specifications: 5G NR (38-series), LTE (36-series), 5G system architecture (TS 23.501), RRC (TS 38.331), NAS, security, charging, or other TS/TR in Rel-15 through Rel-20.

## Connect

Prefer MCP over copying this file into every session:

```
https://api.3gppscout.com/mcp/
```

Streamable HTTP, OAuth 2.1. No Scout API key in MCP config. After connect, read `scout://skill-guide` or [https://api.3gppscout.com/skill.md](https://api.3gppscout.com/skill.md) for tools, filters, and workflows.

Verify with `list_documents` filtered to `doc_number=38.331` and `release=Rel-19`.

## Do not

- Self-host from this repository. There is no server implementation here.
- Claim 3GPP or ETSI endorsement.
- Invent spec text. Search, then cite.

Product page: [https://3gppscout.com/mcp/](https://3gppscout.com/mcp/?src=github)
