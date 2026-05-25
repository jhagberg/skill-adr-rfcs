# RFC Guide

Requests for Comments (RFCs) are exploratory documents for decisions that are
genuinely open, affect multiple stakeholders, and benefit from structured async
discussion before commitment.

## When to use an RFC

Use an RFC when:
- The decision impacts people outside the immediate team
- Multiple genuine options exist and none is obviously right
- The design space is large enough to warrant structured exploration
- You want to invite written feedback before committing

If the decision is already made or the scope is a single self-contained choice,
use an ADR instead.

## Directory and naming

- Directory: `docs/rfcs/`
- Filename: `NNNN-kebab-case-title.md` (4-digit, zero-padded)
- Number space is independent from ADRs

## Lifecycle

```
draft → discussion → accepted → [superseded]
                   → rejected
                   → withdrawn
```

### Status definitions

- **draft** — The author is still writing. Not yet ready for review.
- **discussion** — Open for review and feedback. Typically corresponds to an
  open pull request. This is the main collaboration phase.
- **accepted** — Consensus reached. The Outcome section is filled in with the
  decisions made, ADR links, and next steps.
- **rejected** — Closed without acceptance. Keep the file — the analysis has
  long-term value for anyone who revisits the question later.
- **withdrawn** — The author pulled it before a decision was reached.
- **superseded** — Replaced by a later RFC. Link forward to the replacement.

## The RFC → ADR graduation flow

When an RFC reaches `accepted`:

1. Create one or more ADRs in `docs/decisions/` capturing the committed decisions.
   Each ADR's "More Information" section links back to the RFC.
2. Update the RFC:
   - Set `status: accepted` and update the `updated` date.
   - Fill in the `Outcome` section: summarize the consensus, list the resulting
     ADR numbers, link to implementation issues.
   - Add ADR references to the `related-adrs` frontmatter field.

Not every section of the RFC maps 1:1 to an ADR. The RFC's exploration
(Motivation, Rationale, Prior art) provides context; the ADR captures only the
committed decision and its direct consequences.

## Design influences

This RFC format is inspired by:
- **Rust RFC process** — PR-based, numbered, with Final Comment Period
- **Oxide RFD** ("Request for Discussion") — lighter than Rust RFCs, broader
  scope (technical and non-technical)
- **Squarespace** — heavyweight with named approvers and Architecture Review meetings
- Practitioner consensus (Gergely Orosz, Candost Dagdeviren) that RFC = exploration,
  ADR = commitment

The template in this skill borrows Rust's section vocabulary (Summary,
Motivation, Drawbacks, Rationale and alternatives, Prior art, Unresolved
questions, Future possibilities) but uses a lighter process — no formal Final
Comment Period, no reference-level specification section (replaced by a
combined "Detailed design"), and a simpler status lifecycle.

## Tips for effective RFCs

- **Start with Motivation, not the solution.** The problem statement should
  convince readers the RFC is worth their time.
- **Be honest in Drawbacks.** Readers trust proposals that acknowledge costs.
- **Prior art is not optional.** Showing you've looked beyond your own team
  builds confidence in the recommendation.
- **Keep Unresolved questions visible.** Hidden unknowns erode trust; listed
  unknowns invite help.
- **Name your audience.** The frontmatter `authors` field identifies who is
  responsible; `consulted` and `informed` (borrowed from RACI) clarify who
  should weigh in and who just needs to know.
