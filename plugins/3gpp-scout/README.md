# 3GPP Scout

3GPP Scout is a hosted MCP plugin for Claude Code. It searches an index of public 3GPP technical specifications (TS and TR, Rel-15 through Rel-20), meeting contributions (TDocs), meeting decisions and company positions, and returns short excerpts with document number, version, clause and a link to the official source.

## Install

From this repository's marketplace:

```bash
claude plugin marketplace add carrotlabsai/3gpp-scout-mcp
claude plugin install 3gpp-scout@3gpp-scout
```

Or in one command (Claude Code v2.1.292 or later):

```bash
claude plugin install 3gpp-scout --marketplace carrotlabsai/3gpp-scout-mcp
```

Inside a Claude Code session you can also run `/plugin marketplace add carrotlabsai/3gpp-scout-mcp`, then `/plugin install 3gpp-scout@3gpp-scout`.

Sign in with your Scout account when Claude Code opens the browser. Purchases are not available inside the plugin. Coverage varies by release and working group; a proposal is not an agreed outcome.

## What it includes

- Remote MCP server at `https://api.3gppscout.com/mcp/` (Streamable HTTP, OAuth 2.1)
- A skill that tells Claude how to search specs, read clauses, check meeting decisions and confirm follows before saving

## Example prompts

- Read the RRC reconfiguration procedure in TS 38.331 Rel-18, clause 5.3.5.3.
- What did RAN1 #126 agree? Include sources and coverage limits.
- Help me follow changes to TS 38.331. Show the targets before saving.

## Links

- Setup: [https://3gppscout.com/mcp/claude/](https://3gppscout.com/mcp/claude/)
- Privacy: [https://3gppscout.com/privacy/](https://3gppscout.com/privacy/)
- Support: [contact@3gppscout.com](mailto:contact@3gppscout.com)

## Trade mark notice

3GPP Scout is an independent product and is not affiliated with, endorsed or sponsored by 3GPP, ETSI or any 3GPP Organizational Partner. 3GPP™ is a trade mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners. Excerpts are quoted for reference and the official documents govern. Copyright, correction or removal requests: contact@3gppscout.com.
