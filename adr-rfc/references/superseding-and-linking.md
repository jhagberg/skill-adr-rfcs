# Superseding and Cross-Linking

How to handle document succession and maintain navigable links between related
ADRs and RFCs.

## Superseding an ADR

When a new decision replaces a previous one:

### In the new ADR
- Write the ADR normally. In the "More Information" section, note:
  `Supersedes [ADR-NNNN](NNNN-old-title.md).`
- Explain in the Context section why the previous decision is being revisited.

### In the old ADR
- Update the frontmatter status:
  ```yaml
  status: "superseded by ADR-NNNN"
  ```
- Add a note at the top of the body or in "More Information":
  `Superseded by [ADR-NNNN](NNNN-new-title.md).`
- Do not delete or substantially edit the old ADR's content — it's a historical
  record. The original reasoning remains valuable.

### In the index
- Update the old ADR's status column in `docs/decisions/README.md`.
- Add the new ADR as a new row.

## Superseding an RFC

Same pattern:
- New RFC: normal lifecycle (`draft` → `discussion`); link back to the old RFC
  in its Motivation or Prior art section.
- Old RFC: set `status: superseded` and add a link forward in the body.

## Cross-linking ADRs and RFCs

### RFC → ADR (graduation)
When an RFC's outcome produces ADRs:
- RFC frontmatter: `related-adrs: [NNNN, MMMM]`
- RFC Outcome section: list the ADR numbers with links and a summary of what
  each captures.
- Each ADR's "More Information" section: link back to the RFC.

### ADR → ADR (related decisions)
When decisions are related but neither supersedes the other:
- Use the "More Information" section: `Related: [ADR-NNNN](NNNN-title.md) (covers the auth strategy this depends on).`
- Keep it lightweight — don't create a web of cross-references for loosely
  related decisions. Link only when understanding one decision requires
  context from another.

### ADR → RFC (context)
When an ADR was informed by an RFC that wasn't directly its parent:
- Note it in "More Information": `See also [RFC-NNNN](../rfcs/NNNN-title.md) for broader context on the migration strategy.`

## Deprecation

When a decision is no longer relevant (the technology was decommissioned, the
feature was removed):
- Update frontmatter: `status: "deprecated"`
- Add a brief note in "More Information" explaining why.
- Update the index table.
- Do not delete the ADR.

## Maintaining link integrity

- Use relative paths for links between documents in the same repo.
- When renaming a file, update all documents that link to it.
- The index table in `README.md` is the authoritative list — if a link breaks,
  the index should still be navigable.
