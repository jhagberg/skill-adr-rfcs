# RFC vs ADR — Decision Guide

Use this when it's unclear whether a document should be an ADR or an RFC.

## Quick decision tree

```
Is the decision already made?
├── Yes → ADR (status: accepted)
└── No
    ├── Is it genuinely open with multiple viable options?
    │   ├── Yes
    │   │   ├── Does it impact people outside the immediate team?
    │   │   │   ├── Yes → RFC
    │   │   │   └── No → ADR (status: proposed)
    │   │   └── Is the design space large enough to warrant structured exploration?
    │   │       ├── Yes → RFC
    │   │       └── No → ADR (status: proposed)
    │   └── No (one option is clearly right, just needs ratification)
    │       └── ADR (status: proposed)
    └── Is it trivial (variable name, log format, single-file refactor)?
        └── No document. Use a code comment or PR description.
```

## The fundamental distinction

**RFC = exploration.** "Here's a problem space. Here are approaches. Let's
discuss and converge." The output is consensus and one or more committed decisions.

**ADR = commitment.** "We decided X because of Y. Here's what changes." The
output is a record that future readers can reference.

An RFC's outcome becomes one or more ADRs. Not every change needs an RFC —
most decisions go straight to ADR.

## Examples

| Scenario | Document | Why |
|----------|----------|-----|
| "We're switching from REST to GraphQL" — decision already made by tech lead | ADR | Decision is committed. Record the rationale. |
| "Should we use GraphQL, gRPC, or keep REST? Three teams are affected" | RFC | Open question, multiple stakeholders, genuine options |
| "We chose PostgreSQL over MySQL for the new service" | ADR | Single self-contained choice, already decided |
| "How should we handle multi-tenancy across all services?" | RFC | Cross-cutting concern, broad design space |
| "Let's add an index to the users table" | Neither | Trivial operational change |
| "We need to pick a CI provider — GitHub Actions vs GitLab CI" | ADR (proposed) | Two options but self-contained; doesn't need weeks of RFC discussion |
| "Redesigning the authentication architecture across mobile, web, and API" | RFC | Large scope, multiple teams, many interacting decisions |

## When in doubt

Default to ADR. An ADR with status `proposed` gives you the same review
opportunity as an RFC but with less overhead. Escalate to RFC only when the
discussion genuinely warrants a heavier process — cross-team impact, weeks of
design work, or a problem space where the alternatives section would span
multiple pages.

## Linking them together

When an RFC graduates to ADR(s):
- Each ADR's "More Information" section links to the originating RFC
- The RFC's `Outcome` section lists the resulting ADR numbers
- The RFC's `related-adrs` frontmatter field references the ADR numbers
- Each ADR's frontmatter can note the originating RFC if the team wants bidirectional metadata
