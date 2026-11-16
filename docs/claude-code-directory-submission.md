# Claude Code / Anthropic directory submission (3GP-514)

Prepared for the owner. Listing text matches the Codex plugin manifests in this repository and the Claude Connectors packet in `carrotlabsai/3gpt` at `specs/claude-directory/SUBMISSION.md` (3GP-500). Trade mark notice matches `business/LEGAL.md` section 5 in the Scout product repo.

Anthropic docs read for this packet (current as of the agent run):

- [Publish and distribute a plugin](https://code.claude.com/docs/en/plugins/publish)
- [Submit your plugin](https://claude.com/docs/plugins/submit)
- [Plugin pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist)
- [Plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)
- [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace)
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) (PRs are not monitored; submit through the portal)

## What Anthropic requires

### Two different catalogs

1. **Your own marketplace (works today, no Anthropic account).** A `.claude-plugin/marketplace.json` in this public GitHub repository. Users run `claude plugin marketplace add carrotlabsai/3gpp-scout-mcp` then `claude plugin install 3gpp-scout@3gpp-scout`. No review.
2. **Anthropic's directory (claude.ai / Cowork / Claude Code via account sync).** Submit a **Plugin bundle** from a paid claude.ai account at [claude.ai/directory/manage](https://claude.ai/directory/manage). Anthropic validates, security-scans and (usually) has a reviewer publish the first version. This is **not** a pull request to `anthropics/claude-plugins-official`. That repository says directory submissions go through the portal only. Getting into Anthropic's separate official Claude Code marketplace (`claude-plugins-official`) needs an Anthropic partner contact; the directory portal does not put you there.

### Directory submission requirements (plugin bundle)

- Paid claude.ai plan (Pro, Max, Ultra on your own account; Team/Enterprise Owner, or a member with Directory permission).
- GitHub account connected to the Claude organization that submits, with push access to `carrotlabsai/3gpp-scout-mcp`.
- Plugin folder with `.claude-plugin/plugin.json` (here: `plugins/3gpp-scout`).
- README of at least 40 words in the plugin folder.
- License: `LICENSE` in the plugin folder or `license` in `plugin.json` (both present).
- Remote MCP entries use `type` of `http`/`sse`/`ws` and an absolute `https://` URL.
- No secrets in files; comply with [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) and Software Directory Terms.
- Local check: `claude plugin validate ./plugins/3gpp-scout --strict` and `claude plugin validate ./plugins/3gpp-scout --profile directory`.
- Portal Validate runs more checks than the CLI. Fix Blocking findings before Submit for review.
- If the plugin references an MCP server you operate, also submit that server as an **MCP connector** (tracked in 3GP-500). Submit both when the connector is not already listed.

### What the portal cannot be done by an agent without the owner's account

Submission needs the owner's (or Carrot Labs') paid Claude login, GitHub connection in that Claude org, and acknowledgements. This agent does **not** submit. Exact owner action is under [Owner action](#owner-action-exact).

## Files in this repository

| Path | Role |
|---|---|
| `plugins/3gpp-scout/.claude-plugin/plugin.json` | Claude Code / directory plugin manifest |
| `plugins/3gpp-scout/.mcp.json` | Remote MCP: `type: http`, `https://api.3gppscout.com/mcp/` |
| `plugins/3gpp-scout/skills/3gpp-scout/SKILL.md` | Scout skill (auto-loaded from `skills/`) |
| `plugins/3gpp-scout/assets/logo.svg` | Listing icon (Scout search mark on `#047857`; no 3GPP/ETSI/LTE/5G logos) |
| `plugins/3gpp-scout/README.md` | Plugin README for the directory listing |
| `plugins/3gpp-scout/LICENSE` | MIT copy for the plugin folder |
| `.claude-plugin/marketplace.json` | Repo marketplace for `/plugin marketplace add carrotlabsai/3gpp-scout-mcp` |

## Listing text (copy into the portal)

The portal Listing details step reads `plugin.json` and the plugin README. Prefer editing those files and re-validating. If a free-text field still needs paste:

**Name / display name:** 3GPP Scout

**Short description** (manifest `description`):

> Search 3GPP specifications, TDocs and meeting decisions with citations.

**Long description** (same claims as Codex `longDescription` / Claude connector description; "inside the plugin" kept for the plugin surface):

> 3GPP Scout helps telecom engineers, standards delegates and consultants search its own index of public 3GPP specifications, meeting contributions (TDocs), decisions and company positions. Find a clause or recorded outcome, then check a short excerpt with its document number, version and source link. Review and confirm targets to follow a topic in your Scout account, with optional email digests. Requires a Scout account and uses its request limits. Coverage varies by release and working group; a proposal is not an agreed outcome. Purchases are not available inside the plugin. 3GPP Scout is an independent product and is not affiliated with, endorsed or sponsored by 3GPP, ETSI or any 3GPP Organizational Partner. 3GPP™ is a trade mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners. Excerpts are quoted for reference and the official documents govern. Copyright, correction or removal requests: contact@3gppscout.com.

**Links**

| Field | Value |
|---|---|
| Documentation | https://3gppscout.com/mcp/claude/ |
| Privacy | https://3gppscout.com/privacy/ |
| Support | https://3gppscout.com/support.html (or contact@3gppscout.com where the form asks for email) |
| Homepage | https://3gppscout.com/mcp/claude/ |
| Repository | https://github.com/carrotlabsai/3gpp-scout-mcp |
| Icon | `plugins/3gpp-scout/assets/logo.svg` (same mark as Codex; 512×512 SVG). If the portal requires PNG, use `specs/claude-directory/icon-512.png` from the 3gpt repo (same artwork). |

**Author / company:** Carrot Labs AI, Inc. · contact@3gppscout.com · https://3gppscout.com

## Example prompts

Same three as the Codex plugin defaults, plus two from the connector packet:

1. Read the RRC reconfiguration procedure in TS 38.331 Rel-18, clause 5.3.5.3.
2. What did RAN1 #126 agree? Include sources and coverage limits.
3. Help me follow changes to TS 38.331. Show the targets before saving.
4. What does TS 24.501 say the UE does when registration is rejected with 5GMM cause #7? Quote the clause.
5. Which companies supported or opposed the RedCap eDRX proposals in RAN2, and what did they say?

## Data handling answers (portal step)

Use the same facts as 3GP-500:

- The plugin connects to Scout's own API at `api.3gppscout.com` (public 3GPP documents indexed by Scout). It is not a proxy for a third-party API you do not operate.
- Personal health data: No.
- Intended for people under 18: No (business / engineering tool).
- Sends data only to the declared MCP server (`https://api.3gppscout.com/mcp/`) for tool calls after the user signs in with OAuth.
- Retention: API and MCP records per https://3gppscout.com/privacy/ (Data Retention / API and MCP Records).
- Scout receives tool name, arguments and the signed-in account. It does not read Claude memory, chat history or local files.

## Compliance acknowledgements

Tick all acknowledgements the portal shows. Contact email for Anthropic: `contact@3gppscout.com` (or `chris@3gppscout.com` if you want reviewer mail in your inbox).

## Owner action (exact)

**Who:** Owner (Chris), on a paid Claude account that can push to `carrotlabsai/3gpp-scout-mcp`.

**Do not:** open a PR against `anthropics/claude-plugins-official`. Anthropic does not monitor those PRs for third-party listings.

**Do:**

1. Merge this repository's PR so `main` has `.claude-plugin/marketplace.json` and `plugins/3gpp-scout/.claude-plugin/plugin.json`.
2. Confirm the Claude connector submission for 3GP-500 is in progress or listed (plugin + connector are separate portal entries).
3. Open [claude.ai/directory/manage](https://claude.ai/directory/manage).
4. Connect GitHub for this Claude organization if the portal asks.
5. Select **Submit new** → **Plugin bundle**.
6. Source step:
   - Repository: `carrotlabsai/3gpp-scout-mcp` (or the full GitHub URL).
   - Plugin path: `plugins/3gpp-scout`
   - Branch or tag: leave empty to follow `main`, or set `main` explicitly.
7. Select **Validate**. Fix any Blocking findings in the repo, push, re-validate.
8. Confirm Listing details match the table above.
9. Complete Data handling with the answers in this file.
10. Compliance: confirm `contact@3gppscout.com`, tick all acknowledgements.
11. Review and submit: keep **GitHub push webhook** if you have admin on the repo; otherwise Scheduled check only is fine. Select **Submit for review**.
12. If offered, set up push updates (needs GitHub admin).
13. When a version passes checks, select **Publish** (Anthropic reviewer typically publishes the first version).
14. Comment on Linear 3GP-514 with the submission date and portal status. Escalations: follow portal guidance; connector escalations used `mcp-review@anthropic.com`.

## Install commands users get today (before directory listing)

```bash
claude plugin marketplace add carrotlabsai/3gpp-scout-mcp
claude plugin install 3gpp-scout@3gpp-scout
```

Then sign in when Claude Code prompts (OAuth; loopback callback already supported by Scout).

MCP-only fallback (no plugin skill):

```bash
claude mcp add --transport http --scope user 3gpp-scout https://api.3gppscout.com/mcp/
```

## Website follow-up

After the plugin installs cleanly from the marketplace (and again when the directory lists it), update https://3gppscout.com/mcp/claude/ with the plugin install commands through a website agent (called out in 3GP-514 Do step 4).
