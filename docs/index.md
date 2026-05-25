# PhemeHQ Architecture Decision Records

This repository is the single source of truth for **architecture decisions** made
across PhemeHQ projects. Every significant technical choice — a language, a protocol,
a data model, a vendor — is documented here as an Architecture Decision Record (ADR)
before it is implemented.

**Why this exists**: when someone asks *"why did we do it this way?"* or proposes a
change (*"should we switch from Terraform to OpenTofu?"*), the answer is a document,
not an individual's memory. The ADR tells you the context at the time, the options
that were weighed, the reasoning behind the choice, and the trade-offs accepted.
If circumstances change, the ADR is updated or superseded — not silently forgotten.

:::{note}
Decisions here are not immutable edicts. They are the best reasoning we had at
the time. New evidence, new constraints, or new options are good reasons to open
a new ADR and supersede an old one.
:::

```{toctree}
:maxdepth: 1
:caption: How We Work

process
```

```{toctree}
:maxdepth: 1
:caption: Decisions

decisions/index
decisions/ADR-0001
decisions/ADR-0002
```

## Decision Status at a Glance

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [ADR-0001](decisions/ADR-0001.md) | Use Go for the Metric Bridge | Accepted | 2026-05-26 |
| [ADR-0002](decisions/ADR-0002.md) | Use Holt-Winters ETS for Baseline Anomaly Detection | Accepted | 2026-05-26 |
