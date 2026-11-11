---
name: 3gpp-scout
description: Answer questions about 3GPP specifications (TS and TR, Rel-15 through Rel-20), TDocs, meeting decisions and company positions with the 3GPP Scout MCP tools. Use for 5G NR, LTE, RAN, 5G core, NAS, security or charging questions that need spec text and citations.
---

# 3GPP Scout

Use the `3gpp-scout` MCP tools from this plugin when the user needs 3GPP specification text, TDocs, meeting decisions or company positions.

## Workflow

1. Find where the behavior is defined. Use `lookup_reference` for a cause code, timer, information element, message name, or a term or abbreviation a spec defines. Use `search_specs` for everything else. It returns normative specs (requirements, architecture, protocol) unless you set `role`.
2. Read the defining clause with `read_clause` before quoting it. When a long clause comes back truncated, call it again with `term` to read the part around a word, value or cause number.
3. When the release matters, check `clause_history` for which releases changed the clause.
4. For what is changing or still under discussion, use `search_meeting_documents` and `get_meeting_decisions`. Find meeting IDs with `find_meetings`. Agreements reach the specs months later.
5. For one TDoc, use `get_tdoc`. For what companies proposed, supported or opposed on a topic, use `company_positions` with a topic and, if the user names them, companies and a meeting.
6. Cite every quote with spec number, version and clause, or TDoc number, and link the official 3GPP source the tool returns.

Every result has a role. Conformance test specs test a requirement defined elsewhere: cite the clause in `tested_clauses`, not the test. Use `find_conformance_tests` only when the user asks how a requirement is tested.

For the full guide, read the `scout://guide` resource.

## Do not

- Invent spec text. Look it up, read it, then cite it.
- Rebuild or export a whole specification. Give short excerpts and point to the 3GPP document.
- Present a proposal or a feature-lead summary as an agreement. Only `get_meeting_decisions` records what a meeting agreed.
- Say or imply that 3GPP Scout is endorsed by 3GPP or ETSI. It is an independent product.

## Follow confirmation and limits

`find_topics_to_follow` previews possible targets without saving. Show the targets and delivery settings, then wait for the user to confirm before calling `follow_topic` with `confirmed: true`. `update_followed_topic` overwrites settings. `unfollow_topic` removes a saved follow and cannot be undone; confirm the specific follow first.

Scout covers 3GPP documents; state missing coverage instead of inventing text from other standards. Purchases are unavailable inside this plugin. Relay quota usage and reset information without plan prices, checkout links or upgrade prompts.
