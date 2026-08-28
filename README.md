# adr-rfc

A [Claude Code skill](https://code.claude.com/docs/en/skills) that writes,
reviews, and maintains Architecture Decision Records
([MADR 4.0](https://adr.github.io/madr/)) and exploratory RFCs.

## Install

Copy or symlink the `adr-rfc/` directory into your skills folder:

```sh
ln -s "$(pwd)/adr-rfc" ~/.claude/skills/adr-rfc     # personal
ln -s "$(pwd)/adr-rfc" .claude/skills/adr-rfc       # project-scoped
```

## What it does

| Ask | Result |
|-----|--------|
| "Write an ADR for X" | MADR 4.0 record in `docs/decisions/NNNN-kebab-case-title.md`, index row added |
| "Draft an RFC for X" | Rust/Oxide-style RFC in `docs/rfcs/`, independent numbering |
| "Review this ADR/RFC" | Checklist-driven review with line references |
| "What did we decide about X?" | Search across decisions and RFCs, flags superseded results |
| "Accept / deprecate / supersede ADR-0007" | Status change, index update, bidirectional links |
| "This RFC is accepted" | Graduates it into one or more ADRs |

It also tells you when *not* to write one (trivial choices) and which of the
two fits (RFC = exploration, ADR = commitment).

## Layout

```
adr-rfc/
├── SKILL.md        # workflows and principles — loaded when the skill triggers
├── references/     # loaded on demand: MADR guide, RFC guide, checklists, linking
└── assets/         # templates copied into the target repo (MADR 4.0, RFC, indexes)
```

## Evals

`evals/` holds the scenarios (`evals.json`), a deliberately weak ADR fixture
for the review scenario, and a programmatic grader. To rerun after changing
the skill: for each scenario, run its prompt once with the skill installed and
once without, save the output under
`<run-dir>/<scenario>-with_skill/outputs/` and
`<run-dir>/<scenario>-without_skill/outputs/`, then:

```sh
python3 evals/grade_outputs.py <run-dir>
```

Last result (iteration 4): with skill 29/29 assertions, without 9/29. Comment-leak check: 0/5 across five ADR-creation reps.

## Attribution and license

The MADR templates in `adr-rfc/assets/` are copied from
[adr/madr](https://github.com/adr/madr/tree/4.0.0/template) 4.0.0
(`MIT OR CC0-1.0`); deviations are listed in
`adr-rfc/references/madr-guide.md`. Everything else is MIT — see `LICENSE`.
