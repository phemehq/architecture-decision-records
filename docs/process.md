# ADR Process

This page describes how PhemeHQ creates, reviews, and maintains Architecture
Decision Records.

## What Is an ADR?

An Architecture Decision Record captures a single architectural decision: the
context that forced the decision, the options considered, the choice made, and
the consequences accepted.

ADRs follow the [MADR (Markdown Architectural Decision Records)](https://adr.github.io/madr/)
standard — the most widely adopted ADR format, used by projects including
Kubernetes, Azure, and CNCF ecosystem tooling.

## When to Write an ADR

Write an ADR when the decision:

- Affects more than one component, team, or repository.
- Is hard or expensive to reverse.
- Involves a genuine choice between competing options.
- Will be questioned by future engineers without documentation.

You do **not** need an ADR for:

- Implementation details within a single component.
- Decisions that follow already-accepted ADRs.
- Purely cosmetic or stylistic choices.

## Decision Lifecycle

| Status | Meaning |
|--------|---------|
| **Proposed** | Draft under discussion. Not yet in effect. Open a pull request. |
| **Accepted** | Approved and in effect. The decision governs current work. |
| **Deprecated** | No longer recommended but still in use. Migrate when practical. |
| **Superseded** | Replaced by a newer ADR (referenced in the status field). |
| **Rejected** | Considered but not adopted. Kept for historical record. |

## How to Write One

1. **Assign a number** — take the next available `ADR-NNNN` in sequence.

2. **Create the file** — `docs/decisions/ADR-NNNN.md` in this repository.

3. **Use the MADR structure** (mandatory sections in bold):

   - **Context and Problem Statement** — what forced this decision?
   - Decision Drivers — forces, constraints, quality attributes at stake.
   - **Considered Options** — every realistic alternative, including "do nothing".
   - **Decision Outcome** — the chosen option and why.
   - Consequences — what becomes easier, what becomes harder.
   - Confirmation — how will we know the decision is holding?
   - Pros and Cons of the Options — detailed trade-off analysis per option.
   - More Information — links, references, follow-up decisions.

4. **Open a pull request** — set status to `Proposed`. At least one other
   engineer must review and approve before the status moves to `Accepted`.

5. **Update the index** — add a row to the table in `docs/index.md`.

## Revisiting Decisions

If you believe an accepted decision should change:

1. Write a new ADR that proposes the alternative.
2. Reference the original ADR in the Context section.
3. If accepted, update the original ADR's status to
   `Superseded by ADR-NNNN` and set the new ADR to `Accepted`.

Never silently edit an accepted ADR to change its outcome — the history of
*why* we changed our mind is as important as the decision itself.

## Tooling

This site is built with [Sphinx](https://www.sphinx-doc.org) using the
`sphinx_rtd_theme`. To build and preview locally:

```bash
# First time only
make install

# Build HTML
make build

# Preview at http://localhost:8000
make run
```

The site is automatically deployed to GitHub Pages on every push to `main`
via `.github/workflows/docs.yml`.
