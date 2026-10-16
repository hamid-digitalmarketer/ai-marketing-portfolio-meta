---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_f1ddb9e0c90811f196f9525400248c00
    ReservedCode1: KIdKSZmPTdVtcPjNEsj+1QIKYUuEf0t4E9DZYBn5rO3b/NZ+fYiAuPCUsYQZFv7jPVDnxpCbJ71fQGTB6xxyWqiHEWEAg5XdYIfGXWRBiArf7MwngYcZDtO5q9BMI157MkBxV32wqz+3uXlTIiMvoyMjNMu/KuygxsM7xOfDkNceU0BmjpAJNoZhXI4=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_f1ddb9e0c90811f196f9525400248c00
    ReservedCode2: KIdKSZmPTdVtcPjNEsj+1QIKYUuEf0t4E9DZYBn5rO3b/NZ+fYiAuPCUsYQZFv7jPVDnxpCbJ71fQGTB6xxyWqiHEWEAg5XdYIfGXWRBiArf7MwngYcZDtO5q9BMI157MkBxV32wqz+3uXlTIiMvoyMjNMu/KuygxsM7xOfDkNceU0BmjpAJNoZhXI4=
---

# Roadmap

Build order and status for the AI marketing engineering portfolio. One coherent architecture, shipped repo by repo. Ship each repository fully before starting the next — no half-finished repos.

## Build order and status

| Order | Repository | Phase | Status | Notes |
|-------|-----------|-------|--------|-------|
| 1 | ai-marketing-shared | A · Shared Foundation | **Done** · v0.1.0 | Pushed to GitHub (`1dd8024`, [hamid-digitalmarketer/ai-marketing-shared](https://github.com/hamid-digitalmarketer/ai-marketing-shared)). Schemas, tools, MCP adapter, tracing, cost, fallback, eval harness, providers, demo mode; >90% coverage. |
| 2 | ai-marketing-portfolio-meta | A · Shared Foundation | **Done** · v0.1.0 | Pushed to GitHub (`c44497e`, [hamid-digitalmarketer/ai-marketing-portfolio-meta](https://github.com/hamid-digitalmarketer/ai-marketing-portfolio-meta)). Hub, standards, roadmap, architecture, case studies, diagrams, Astro site. |
| 3 | ai-marketing-growth-os | B · Flagship | **Done** · v0.1.0 | Pushed to GitHub (`ba8f3e5`, [hamid-digitalmarketer/ai-marketing-growth-os](https://github.com/hamid-digitalmarketer/ai-marketing-growth-os)). 55 tests, 94.46% coverage; FastAPI backend, 4 agents, approval queue, dashboard, Docker, CI. |
| 4 | ai-agent-testing-lab | G · Testing & Reliability | **Done** · v0.1.0 | Pushed to GitHub (`e919875`, [hamid-digitalmarketer/ai-agent-testing-lab](https://github.com/hamid-digitalmarketer/ai-agent-testing-lab)). 81 tests, 98.66% coverage; harness imports shared + growth-os agents, 7 dataset suites, reporters, CI integration template; self-eval PASS. |
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

- [x] **Phase A — Shared foundation** (ai-marketing-shared + ai-marketing-portfolio-meta done, pushed)
- [x] **Phase B — Flagship** (ai-marketing-growth-os done, pushed)
- [x] **Testing lab built** (ai-agent-testing-lab pushed; wiring into subsequent repo CIs in progress)
- [ ] **Phases C–F — Strategic, core, intelligence, governance modules**
- [ ] **Phase G — Testing & reliability** (ai-agent-testing-lab)
- [ ] **Phase H — Portfolio polish** (master README, personal site, demos, case studies)
*（内容由AI生成，仅供参考）*
