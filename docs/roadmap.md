# Roadmap

Build order and status for the AI marketing engineering portfolio. One coherent architecture, shipped repo by repo. Ship each repository fully before starting the next — no half-finished repos.

## Build order and status

| Order | Repository | Phase | Status | Notes |
|-------|-----------|-------|--------|-------|
| 1 | ai-marketing-shared | A · Shared Foundation | **Done** · v0.1.0 | Committed locally (`1dd8024`). Schemas, tools, MCP adapter, tracing, cost, fallback, eval harness, providers, demo mode; unit suite verified locally with >90% coverage target. Remote to be created and pushed. |
| 2 | ai-marketing-portfolio-meta | A · Shared Foundation | **In progress** | This repository — hub, standards, roadmap, architecture, case studies, diagrams, Astro site. |
| 3 | ai-marketing-growth-os | B · Flagship | Planned | Flagship agentic marketing intelligence platform; proves the shared pattern end-to-end. |
| 4 | ai-agent-testing-lab | G · Testing & Reliability | Planned | Built early (after flagship) so every later repo is evaluated from day one. |
| 5 | ai-marketing-mix-copilot | C · Strategic | Planned | Bayesian MMM + incrementality + budget scenarios. |
| 6 | ai-content-ops-brand-voice | D · Core Modules | Planned | Content planning → drafting → review → publish → measure. |
| 7 | ai-customer-journey-orchestrator | D · Core Modules | Planned | Real-time next-best-action with holdout testing. |
| 8 | ai-cro-experimentation | D · Core Modules | Planned | Hypothesis → experiment → analysis → learning. |
| 9 | ai-marketing-data-quality | D · Core Modules | Planned | Pipeline monitoring: schema drift, freshness, tracking, attribution. |
| 10 | ai-marketing-knowledge-graph | E · Intelligence | Planned | Unified marketing knowledge graph + natural-language querying. |
| 11 | ai-competitive-intelligence | E · Intelligence | Planned | Always-on competitive and market sensing. |
| 12 | ai-customer-feedback-intelligence | E · Intelligence | Planned | Voice-of-customer intelligence. |
| 13 | ai-brand-safety-compliance | F · Governance | Planned | Governed review of ads, landing pages, creatives, influencer content. |
| 14 | ai-local-geo-marketing | F · Governance | Planned | Multi-location local marketing optimization. |
| 15 | ai-lead-scoring-alignment | F · Governance | Planned | Explainable lead scoring and closed-loop revenue attribution. |
| 16 | ai-affiliate-partnership-intelligence | F · Governance | Planned | Partner discovery, vetting, and optimization. |
| 17 | ai-marketing-digital-twin | F · Governance | Planned | Simulation sandbox before real-world execution. |
| 18 | Portfolio polish | H · Polish | Planned | Master README, personal site, case studies, demo videos/GIFs. |

## Dependencies

```
ai-marketing-shared            <- everything imports this (schemas, tooling, eval)
ai-agent-testing-lab           <- evaluates every other repo in CI
ai-marketing-portfolio-meta    <- documents standards, tracks roadmap, hosts case studies
```

- Repos 3–17 depend on `ai-marketing-shared` for schemas, tool base classes, MCP adapter, tracing, cost accounting, fallback engine, eval harness, and provider abstraction.
- `ai-agent-testing-lab` is sequenced after the flagship so every subsequent repo is evaluated from day one.
- The hub (`ai-marketing-portfolio-meta`) is maintained continuously: standards, roadmap status, and one case study per shipped repo.

## Milestones

- [x] **Phase A — Shared foundation** (ai-marketing-shared done; ai-marketing-portfolio-meta in progress)
- [ ] **Phase B — Flagship** (ai-marketing-growth-os proves the pattern end-to-end)
- [ ] **Testing lab wired into CI** (ai-agent-testing-lab evaluates all subsequent repos)
- [ ] **Phases C–F — Strategic, core, intelligence, governance modules**
- [ ] **Phase G — Testing & reliability** (ai-agent-testing-lab)
- [ ] **Phase H — Portfolio polish** (master README, personal site, demos, case studies)
