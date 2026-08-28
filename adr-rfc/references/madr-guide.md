# MADR Guide

Markdown Architectural Decision Records (MADR) version 4.0.0 (released 17 September 2024).
This guide covers the format, status lifecycle, naming conventions, and
directory structure.

## Directory structure

Canonical directory: `docs/decisions/` (changed from `docs/adr/` in MADR 3.0+).
Each ADR is a separate Markdown file. An index file (`README.md`) lists all ADRs.

## Naming convention

Filename: `NNNN-kebab-case-title.md`

- `NNNN` is a 4-digit zero-padded sequence number.
- `0000` is reserved by convention for "Use MADR" (the meta-ADR explaining why
  the project uses this format). `assets/0000-use-markdown-architectural-decision-records.md`
  is upstream's own copy — offer it when bootstrapping `docs/decisions/`. Start
  actual project decisions at `0001`.
- To find the next number: list the directory, sort numerically, take max + 1.
  Show the proposed number to the user before creating the file.

## Template variants

MADR 4.0 ships four template variants:

| Variant | Sections | Annotations |
|---------|----------|-------------|
| Full (annotated) | All sections | Yes — inline guidance |
| Minimal (annotated) | Mandatory only | Yes |
| Full (bare) | All sections | No |
| Minimal (bare) | Mandatory only | No |

This skill bundles the two annotated forms in `assets/`, copied from the
upstream 4.0.0 tag (<https://github.com/adr/madr/tree/4.0.0/template>). The
only deviations are three upstream typo fixes in the full template (closing
brace in the `status` placeholder, "Not that" → "Note that", a duplicated
"this decision"). Sections preceded by
`<!-- This is an optional element. Feel free to remove. -->` — and the entire
frontmatter block — are optional per MADR. Use the full template by default;
offer minimal when the user explicitly wants brevity.

## Full template section order

1. **YAML frontmatter** — `status`, `date`, `decision-makers`, `consulted`, `informed` *(optional per MADR; this skill expects them when using the full template)*
2. **Title** — as an H1, descriptive of the decision
3. **Context and Problem Statement** — 2–5 sentences describing the problem
4. **Decision Drivers** *(optional)* — bullet list of forces influencing the decision
5. **Considered Options** — bullet list of alternatives
6. **Decision Outcome** — which option was chosen, with justification
7. **Consequences** *(optional, but nearly always included)* — nested under Decision Outcome; Good and Bad bullets
8. **Confirmation** *(optional but common)* — how compliance will be verified
9. **Pros and Cons of the Options** *(optional)* — detailed analysis per option
10. **More Information** *(optional)* — links, meeting notes, related ADRs/RFCs

## Minimal template section order

1. **Title**
2. **Context and Problem Statement**
3. **Considered Options**
4. **Decision Outcome**
5. **Consequences** *(optional)* — nested under Decision Outcome

No frontmatter, no other sections.

## Status lifecycle

MADR uses an open status vocabulary in YAML frontmatter:

```
proposed → accepted
         → rejected
         → deprecated
         → superseded by ADR-0123
```

Additional commonly used statuses:
- `draft` — author is still writing (not part of MADR's canonical list, but widely adopted)

The status field uses this format:
```yaml
status: "accepted"
```

For supersession:
```yaml
status: "superseded by ADR-0042"
```

## MADR 3.0 → 4.0 changes worth knowing

- "Validation" renamed to "Confirmation" and nested under Decision Outcome
- "Deciders" renamed to "Decision Maker(s)" (`decision-makers:` in YAML)
- Placeholders moved to one-liners
- Quotes around the chosen option name reinstated
- Example identifier is `ADR-0123` (not `ADR-NNNN`)

## When to use MADR vs other ADR formats

MADR's strengths over Nygard's original lightweight format:
- Structured frontmatter for machine-readable metadata
- Explicit "Considered Options" with pros/cons promotes rigorous thinking
- "Confirmation" section adds accountability
- Semantic versioning of the format itself

MADR is appropriate for most teams. It adds useful structure without excessive
ceremony. The minimal template is nearly as lightweight as Nygard's format while
retaining the MADR section vocabulary.
