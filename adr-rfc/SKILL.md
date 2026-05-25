---
name: adr-rfc
description: "Writes and reviews Architecture Decision Records (ADRs, MADR 4.0 format in docs/decisions/) and exploratory RFCs (in docs/rfcs/). Use when the user asks to write an ADR, draft an RFC, record a decision, propose a design, review a proposal, or asks is this decision worth recording, RFC or ADR, what did we decide about X. Also use proactively to offer ADR/RFC capture after an architectural decision has stabilized. Handles numbering, status transitions, supersession, README/index updates, and the RFC-to-ADR graduation flow. Do NOT use for routine code comments, commit messages, PR descriptions, blog posts, release notes, or trivial style choices."
---

# ADR + RFC Skill

Create, review, and manage Architecture Decision Records (MADR 4.0) and
Requests for Comments. ADRs record committed decisions; RFCs explore open
questions that may graduate into one or more ADRs.

## RFC or ADR?

Before creating a document, determine which type fits:

1. **Decision already made?** → ADR. Status starts as `accepted` (or `proposed` if pending ratification).
2. **Decision open, multiple genuine options, impacts people outside the immediate group?** → RFC. Its outcome later spawns ADRs.
3. **Architecturally significant but a single self-contained choice?** → ADR. RFCs are for broader explorations.
4. **Trivial** (variable name, log format, single-file refactor)? → No document. Suggest a code comment or PR description.

Default to ADR when in doubt. RFCs cost weeks of attention; ADRs cost an hour.

For a deeper decision guide with examples, read `references/rfc-vs-adr.md`.

## Workflows

### Write an ADR

1. Check whether `docs/decisions/` exists. If not, ask permission to create it with a `README.md` (use `assets/decisions-README.md` as the template).
2. List existing ADRs to find the next sequence number. Filenames follow `NNNN-kebab-case-title.md` (4-digit, zero-padded). `0000` is reserved for "Use MADR"; start at `0001`.
3. If context is thin, ask the user:
   - What problem are you solving?
   - What options are on the table?
   - Which are you choosing and why?
   - What changes for the codebase as a result?
4. Read `assets/madr-template-full.md` (or `madr-template-minimal.md` if the user wants brevity) and draft the ADR.
5. Show the draft. Wait for approval — never auto-create files.
6. On approval, write `docs/decisions/NNNN-kebab-case-title.md` and update `docs/decisions/README.md` with a new row in the index table.

### Draft an RFC

1. Confirm RFC is the right tool — apply the decision tree above.
2. Check whether `docs/rfcs/` exists. If not, ask permission to create it with a `README.md` (use `assets/rfcs-README.md` as the template). RFC numbering is independent from ADRs.
3. Read `assets/rfc-template.md` and draft the RFC. Frontmatter status: `draft`.
4. Show the draft, get approval, write the file.
5. Update `docs/rfcs/README.md` with a new row in the index table.
6. Suggest opening a PR for the discussion phase.

For RFC lifecycle details, read `references/rfc-guide.md`.

### Review a document

1. Read the file.
2. Apply the relevant checklist from `references/review-checklist.md`.
3. Output a structured review: what's strong, what's missing, specific suggestions with line references.

### Search decisions ("what did we decide about X?")

1. Search `docs/decisions/` (and `docs/rfcs/` if it exists) for matches.
2. Return: title, file path, status, date, decision-makers (if present), Decision Outcome, and a Consequences summary. Flag any superseded or deprecated results.
3. If no match, offer to record one.

### Graduate an RFC to ADR(s)

When an RFC reaches `accepted` status:
1. Create one or more ADRs capturing the committed decisions.
2. Update the RFC's `related-adrs` frontmatter and `Outcome` section with links.
3. Each ADR's "More Information" section links back to the RFC.

For supersession and cross-linking mechanics, read `references/superseding-and-linking.md`.

## Status vocabularies

**ADR (MADR 4.0):** The vocabulary is open; recommended values are `proposed`, `rejected`, `accepted`, `deprecated`, `superseded by ADR-0123`. Also accept `draft` for in-flight authoring. Teams may add other values as needed.

**RFC:** `draft`, `discussion`, `accepted`, `rejected`, `withdrawn`, `superseded`.

For full lifecycle details, read `references/madr-guide.md` and `references/rfc-guide.md`.

## Key principles

- **Never auto-create files.** Draft, show the user, get explicit approval.
- **Keep it short.** Context should be 2–5 sentences. The whole ADR should be readable in 2 minutes.
- **Always list rejected alternatives** with reasons. "We just picked it" is not valid rationale.
- **Always update the index** (`docs/decisions/README.md` or `docs/rfcs/README.md`) when creating or changing status.
- **When superseding, link both directions.** The new document's body links back; the old document's status updates to point forward.
- **When backfilling past decisions,** note both the original decision date and the recording date.
- **Pure Markdown only.** Do not introduce external ADR tooling (`adr-tools`, `log4brains`, `madr-tools`) unless the project already uses it. Do not write scripts to auto-number files.
- **Use `docs/decisions/`**, not `docs/adr/`. This is the canonical MADR 3.0+ directory. If you find an existing `docs/adr/` directory, note it to the user and ask whether to migrate or continue using the legacy path.
- **In non-interactive/autonomous mode,** treat a direct request like "write the ADR file now" as implicit approval — do not block waiting for confirmation that cannot arrive.

For anti-patterns and the full review checklists, read `references/review-checklist.md`.
