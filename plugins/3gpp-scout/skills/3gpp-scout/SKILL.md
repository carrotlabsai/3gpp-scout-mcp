---
name: 3gpp-scout
description: Answer questions about 3GPP specifications (TS and TR, Rel-15 through Rel-20), TDocs, meetings and company positions with the 3GPP Scout MCP tools. Use for 5G NR, LTE, RAN, 5G core, NAS, security or charging questions that need spec text and citations.
---

# 3GPP Scout

Use the `3gpp-scout` MCP tools from this plugin when the user needs 3GPP specification text, TDocs, meeting decisions or company positions.

## Workflow

Tool names below are the short form. Some servers list them with a route suffix, for example `search_text_search_text_post` or `get_sections_sections_get`; they are the same tools.

1. Search first with `search_text`. Filter by `doc_number` (for example `38.331`), `release` (for example `Rel-19`) or series when the user names them.
2. Read the clause with `get_sections` using the document and section from the search hit before quoting it.
3. For TDocs and meetings, use `search_tdocs`, `get_tdoc`, `list_meetings` and `list_meeting_decisions`.
4. Cite every quote with spec number, version and clause, and link the 3GPP source when the tool returns one.

For the full tool guide, read the `scout://skill-guide` resource.

## Do not

- Invent spec text. Search, then cite.
- Rebuild or export a whole specification. Give short excerpts and point to the 3GPP document.
- Say or imply that 3GPP Scout is endorsed by 3GPP or ETSI. It is an independent product.

## Follow confirmation and limits

`find_topics_to_follow` previews possible targets without saving. Show the targets and delivery settings, then wait for the user to confirm before calling `follow_topic` with `confirmed: true`. `update_followed_topic` overwrites settings. `unfollow_topic` removes a saved follow and cannot be undone; confirm the specific follow first.

Scout covers 3GPP documents; state missing coverage instead of inventing text from other standards. Purchases are unavailable inside this plugin. Relay quota usage and reset information without plan prices, checkout links or upgrade prompts.
