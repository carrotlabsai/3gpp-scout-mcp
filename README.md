# Hosted 3GPP MCP Server

**3GPP Scout** is a [hosted 3GPP MCP server](https://3gppscout.com/mcp/?src=github). It makes 3GPP technical specifications (TS and TR) searchable from Cursor, Claude, Codex, and other MCP clients: 5G NR, LTE, RAN, and 5G core, Rel-15 through Rel-20.

You do not download the 3GPP FTP archive, parse Word files, or run a local SQLite index. Connect to the remote Model Context Protocol endpoint and search.

**MCP endpoint:** [`https://api.3gppscout.com/mcp/`](https://api.3gppscout.com/mcp/) (Streamable HTTP, OAuth 2.1)

This repository is the **public listing and integration page** for the 3GPP Scout MCP Server. There is nothing here to `go run` or `npx`. If you want a 3GPP MCP server without self-hosting, this is that product. See [License and the hosted service](#license-and-the-hosted-service).

## Why a hosted 3GPP MCP

3GPP specifications are hard for LLMs to use from training data alone. There are thousands of TS/TR documents. A single spec such as TS 38.331 (NR RRC) or TS 23.501 (5G system architecture) can run hundreds of pages. Releases diverge. Tables and figures carry the protocol.

A self-hosted 3GPP MCP typically means: scrape the 3GPP archive, convert `.docx`, build a local database, and keep it current yourself. Scout runs that index as a service. New and revised 3GPP specs are ingested into the live search index as 3GPP publishes them.

The production corpus is **Rel-15 through Rel-20** (8,700+ document versions, 1.3M+ sections). It is not a Rel-15 + Rel-19 subset.

## What you can search

**Specifications.** Semantic search over the published TS/TR set, including:

- **5G NR / RAN:** 38-series (RRC, NG-RAN, NR overall description)
- **5G system and core:** 23-series architecture, 24-series NAS, 29-series HTTP/2 service-based interfaces, 33-series security
- **LTE / EPS:** 36-series and related SAE specs
- **Charging, OAM, and the rest of the TS/TR catalog** in those releases, not only radio

Filter by release (`Rel-18`, `Rel-19`, ...), document number (`38.331`, `23.501`, `36.300`), series, TS vs TR, or section. Image search covers figures, diagrams, and tables extracted from the specs.

**Meeting documents and decisions.** Search and read TDocs (meeting contributions, change requests, liaison statements) with status and quoted proposals, list meetings and what each one agreed, approved, noted or rejected, and summarize which companies argued for or against a proposal. The TDoc catalog currently covers RAN1, RAN2, RAN3, RAN4 and SA2, and grows as meetings are processed. The skill guide below lists the current coverage.

**Supporting sources.** IETF RFC passages that 3GPP specs depend on, with the 3GPP clauses that cite them, and telecom industry news.

Results carry citations: specification number, version, release and section for spec text, and TDoc number and meeting for contributions.

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

### ChatGPT plugin directory

Install 3GPP Scout from the [ChatGPT plugin directory](https://chatgpt.com/plugins/plugin_asdk_app_6acb351336d481918e036c4d9b611e4f). It signs in with your Scout account and works in ChatGPT and Codex.

### Codex and ChatGPT desktop plugin

```bash
codex plugin marketplace add carrotlabsai/3gpp-scout-mcp
codex plugin add 3gpp-scout@3gpp-scout
```

In the ChatGPT desktop app, open Plugins, add the plugin marketplace `carrotlabsai/3gpp-scout-mcp`, choose 3GPP Scout and install. Sign in with your Scout account when asked. The plugin bundles the hosted MCP server and a short skill; it lives in [`plugins/3gpp-scout`](plugins/3gpp-scout).

### OpenAI Codex (MCP only)

```bash
codex mcp add 3gpp-scout --url https://api.3gppscout.com/mcp/
codex mcp login 3gpp-scout
```

### Verify

Call `list_documents_documents_get` with `doc_number=38.331` and `release=Rel-19`. You should see indexed versions of TS 38.331. Do not list the entire corpus as a health check.

Setup prompt for agents: [api.3gppscout.com/agent-setup/prompt.md](https://api.3gppscout.com/agent-setup/prompt.md)

## MCP tools

These are the tools the live server lists today. Names are the exact strings your client sees.

| Group | Tools |
|---|---|
| Specification search | `search_text_search_text_post` (text, by meaning and by exact values such as numbers and parameter names), `search_images_search_images_post` (figures and diagrams), `search_combined_search_combined_post` (text and figures together) |
| Specification reading | `list_documents_documents_get`, `get_document_documents`, `list_sections_sections_toc_get` (table of contents), `get_sections_sections_get`, `get_sections_batch` (up to 10 clauses in one call) |
| IETF RFCs | `search_ietf_rfcs`, `get_rfc_section` |
| TDocs | `search_tdocs`, `get_tdoc`, `get_tdocs_batch` (up to 10), `list_tdocs`, `fetch_tdoc` (fetch and parse one public TDoc on demand) |
| Meetings and decisions | `list_meetings`, `get_meeting`, `list_meeting_decisions` |
| Companies and positions | `resolve_organization`, `get_organization`, `get_company_positions`, `search_positions` |
| News | `search_news` |
| Follow topics (signed-in user) | `find_topics_to_follow`, `list_followed_topics`, `get_followed_topic_updates`, `follow_topic`, `update_followed_topic`, `unfollow_topic` |
| Private preview | `compare_proposal`, `get_proposal_comparison`, `follow_patent` |

Search and read tools are read-only. `follow_topic`, `update_followed_topic`, `unfollow_topic` and `follow_patent` change the signed-in user's Scout account, and `fetch_tdoc` may download a public TDoc into Scout's catalog. Tool names and parameters can change; the skill guide is the current reference.

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

The free Explorer tier includes 150 MCP/API requests per UTC calendar month, no card needed. Founding Engineer is $8/month for 1,000. Hosted chat at [app.3gppscout.com](https://app.3gppscout.com) uses separate prepaid credits.

Sign up: [dashboard.3gppscout.com](https://dashboard.3gppscout.com)

## This repository

| File | What it is |
|---|---|
| `README.md` | Integration and discovery (this page) |
| `LICENSE` | MIT license for the files in this repository |
| `server.json` | Public MCP Registry metadata (remote server only) |
| `glama.json` | Maintainer claim file for the Glama directory |
| `SKILL.md` | Short agent skill that points at the hosted server |
| `llms.txt` | Same facts in agent-readable form |
| `.agents/plugins/marketplace.json` | Codex and ChatGPT desktop plugin marketplace |
| `plugins/3gpp-scout/` | The 3GPP Scout plugin (MCP server wiring and skill) |

`server.json` is discovery metadata. It does not contain credentials, prompts, or the search implementation. Do not open issues asking for the private monorepo or a self-host package. That is not what this repo is.

## License and the hosted service

The 3GPP Scout hosted service, its search index and its data are proprietary to Carrot Labs AI, Inc. The files in this repository (listing metadata, plugin wiring, the skill and the documentation) are licensed under the [MIT License](LICENSE). The server implementation is not included.

## Links

- Product: [3gppscout.com](https://3gppscout.com/?src=github)
- Hosted MCP page: [3gppscout.com/mcp](https://3gppscout.com/mcp/?src=github)
- Chat: [app.3gppscout.com](https://app.3gppscout.com)
- Contact: [contact@3gppscout.com](mailto:contact@3gppscout.com)
- Terms: [3gppscout.com/terms](https://3gppscout.com/terms.html)
- Privacy: [3gppscout.com/privacy](https://3gppscout.com/privacy.html)
