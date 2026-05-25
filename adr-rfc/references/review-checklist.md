# Review Checklists

Use these when reviewing an existing ADR or RFC. Output a structured review:
what's strong, what's missing, and specific suggestions with line references.

## ADR review checklist

- [ ] **Title** is specific and names both the problem and the solution
- [ ] **Context** is 2–5 sentences, not an essay
- [ ] **At least 2 alternatives** are considered, each with explicit rejection reasons
- [ ] **Decision** is one paragraph, present tense ("We use X")
- [ ] **Consequences** include both positive and negative impacts
- [ ] **Confirmation** describes how compliance will be verified
- [ ] **Supersession** — if this supersedes another ADR, the prior ADR's status
      is updated to `superseded by ADR-NNNN` with a link in its body
- [ ] **Index updated** — `docs/decisions/README.md` has a row for this ADR
- [ ] **Frontmatter complete** (full template only) — `decision-makers` is
      populated (not empty), `consulted` and `informed` are present (can be
      empty if genuinely N/A). Skip this check for minimal-template ADRs.
- [ ] **Date** in frontmatter matches when the decision was made (not when the
      file was created, if backfilling)
- [ ] **No jargon without context** — a new team member can understand the
      decision without external documents

## RFC review checklist

- [ ] **Motivation** includes concrete use cases, not just abstractions
- [ ] **Guide-level explanation** is understandable by someone unfamiliar with
      the internals
- [ ] **Alternatives section** is honest about trade-offs, not a straw-man
      dismissal of everything except the preferred option
- [ ] **Drawbacks** are acknowledged openly — proposals that hide costs lose
      reviewer trust
- [ ] **Prior art** shows the author looked beyond their own team and codebase
- [ ] **Unresolved questions** are listed explicitly, not hidden in vague language
- [ ] **Stakeholders** are identified — authors, consulted parties, and informed
      parties are named in frontmatter
- [ ] **Outcome path** is clear — it's obvious what would become an ADR vs what
      would be implementation detail
- [ ] **Scope** is appropriate — the RFC isn't trying to solve everything at once

## Common issues to flag

### In ADRs
- Context section that's really a solution description (the problem got lost)
- "Considered Options" with only one entry — that's not a decision, it's a mandate
- Consequences that are all positive — every decision has trade-offs
- Missing confirmation section for decisions that need enforcement (e.g., "use
  library X" should specify a lint rule or review gate)

### In RFCs
- Motivation that jumps to the solution without establishing the problem
- Alternatives dismissed with a single sentence each while the preferred option
  gets pages of detail
- "Prior art" that only lists things the author already uses
- Unresolved questions that are actually resolved but the author hasn't updated
  the document
- Scope creep — the RFC tries to decide everything instead of focusing on the
  key architectural question
