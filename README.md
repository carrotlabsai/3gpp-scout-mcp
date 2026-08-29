# Hosted 3GPP MCP Server

**3GPP Scout** is a [hosted 3GPP MCP server](https://3gppscout.com/mcp/?src=github). It makes 3GPP technical specifications (TS and TR) searchable from Cursor, Claude, Codex, and other MCP clients: 5G NR, LTE, RAN, and 5G core, Rel-15 through Rel-20.

You do not download the 3GPP FTP archive, parse Word files, or run a local SQLite index. Connect to the remote Model Context Protocol endpoint and search.

**MCP endpoint:** [`https://api.3gppscout.com/mcp/`](https://api.3gppscout.com/mcp/) (Streamable HTTP, OAuth 2.1)

This repository is the **public listing and integration page** for the 3GPP Scout MCP Server. The hosted service is proprietary. There is nothing here to `go run` or `npx`. If you want a 3GPP MCP server without self-hosting, this is that product.

## Why a hosted 3GPP MCP

3GPP specifications are hard for LLMs to use from training data alone. There are thousands of TS/TR documents. A single spec such as TS 38.331 (NR RRC) or TS 23.501 (5G system architecture) can run hundreds of pages. Releases diverge. Tables and figures carry the protocol.

A self-hosted 3GPP MCP typically means: scrape the 3GPP archive, convert `.docx`, build a local database, and keep it current yourself. Scout runs that index as a service. New and revised 3GPP specs are ingested into the live search index as 3GPP publishes them.

The production corpus is **Rel-15 through Rel-20** (8,700+ document versions, 1.3M+ sections). It is not a Rel-15 + Rel-19 subset.

## What you can search

Semantic search over the published TS/TR set, including:

- **5G NR / RAN:** 38-series (RRC, NG-RAN, NR overall description)
- **5G system and core:** 23-series architecture, 24-series NAS, 29-series HTTP/2 service-based interfaces, 33-series security
- **LTE / EPS:** 36-series and related SAE specs
- **Charging, OAM, and the rest of the TS/TR catalog** in those releases, not only radio

Filter by release (`Rel-18`, `Rel-19`, …), document number (`38.331`, `23.501`, `36.300`), series, TS vs TR, or section. Image search covers figures, diagrams, and tables extracted from the specs.

Citations from the hosted chat app link to the specification's folder on the 3GPP FTP archive, not to a sentence-level PDF deep-link.

## Connect an agent (Cursor, Claude, Codex)

Official registry name: [`com.3gppscout/scout`](https://registry.modelcontextprotocol.io/v0.1/servers?search=com.3gppscout/scout)

### Cursor

Merge into `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "3gpp-scout": {
      "url": "https://api.3gppscout.com/mcp/"
    }
  }
}
```

Enable **3gpp-scout** under Cursor Settings > Tools & MCP. The first tool call opens a browser for OAuth. Do not put a Scout API key in the MCP config.

### Claude Code

```bash
claude mcp add --transport http --scope user 3gpp-scout https://api.3gppscout.com/mcp/
```

Then `/mcp` and connect `3gpp-scout`.

### OpenAI Codex

```bash
codex mcp add 3gpp-scout --url https://api.3gppscout.com/mcp/
codex mcp login 3gpp-scout
```

### Verify

Call `list_documents` with `doc_number=38.331` and `release=Rel-19`. You should see indexed versions of TS 38.331. Do not list the entire corpus as a health check.

Setup prompt for agents: [api.3gppscout.com/agent-setup/prompt.md](https://api.3gppscout.com/agent-setup/prompt.md)

## MCP tools

| Tool | Use |
|---|---|
| `search_text` | Semantic search over specification text (primary) |
| `search_images` | Figures, diagrams, and tables |
| `search_combined` | Text and images in one request |
| `list_documents` / `get_document` | Browse indexed TS/TR metadata |
| `get_sections` / `list_sections` | Pull section body or TOC |
| `get_image` | Fetch an extracted figure |

Full agent skill (parameters, filters, workflows): [api.3gppscout.com/skill.md](https://api.3gppscout.com/skill.md). ClawHub listing: [chriscarrotlabs/3gpp-scout](https://clawhub.ai/chriscarrotlabs/3gpp-scout).

REST with an API key (same corpus): [api.3gppscout.com/docs](https://api.3gppscout.com/docs)

## FAQ

**Is there a hosted 3GPP MCP server?**
Yes. 3GPP Scout at `https://api.3gppscout.com/mcp/`. Product page: [3gppscout.com/mcp](https://3gppscout.com/mcp/?src=github).

**Do I need to self-host an MCP server for 3GPP specs?**
No. Scout is a remote MCP server operated by [Carrot Labs](https://carrotlabs.ai).

**How do I give Cursor or Claude access to 3GPP specifications?**
Add the Streamable HTTP URL above. OAuth on first use. No local 3GPP MCP install.

**Which 3GPP releases?**
Rel-15 through Rel-20, the published TS/TR set. The index stays current as 3GPP publishes.

**Is this an official 3GPP or ETSI product?**
No. 3GPP Scout is independent. It is not affiliated with, endorsed by, or a partner of 3GPP or ETSI.

## Pricing

Explorer includes 150 MCP/API requests per UTC calendar month. Founding Engineer is $8/month for 1,000. Hosted chat at [app.3gppscout.com](https://app.3gppscout.com) uses separate prepaid credits.

Sign up: [dashboard.3gppscout.com](https://dashboard.3gppscout.com)

## This repository

| File | What it is |
|---|---|
| `README.md` | Integration and discovery (this page) |
| `server.json` | Public MCP Registry metadata (remote server only) |
| `SKILL.md` | Short agent skill that points at the hosted server |
| `llms.txt` | Same facts in agent-readable form |

`server.json` is discovery metadata. It does not contain credentials, prompts, or the search implementation. Do not open issues asking for the private monorepo or a self-host package. That is not what this repo is.

## Links

- Product: [3gppscout.com](https://3gppscout.com/?src=github)
- Hosted MCP page: [3gppscout.com/mcp](https://3gppscout.com/mcp/?src=github)
- Chat: [app.3gppscout.com](https://app.3gppscout.com)
- Contact: [contact@3gppscout.com](mailto:contact@3gppscout.com)
- Terms: [3gppscout.com/terms](https://3gppscout.com/terms.html)
- Privacy: [3gppscout.com/privacy](https://3gppscout.com/privacy.html)
