# Architecture

This document explains how the portfolio is architected: the layers, the dependency rules, the data flow, and the design decisions and tradeoffs.

## Purpose

`ai-marketing-portfolio-meta` is the hub of a 17-repository portfolio. It does not implement agents or tools; it documents the standards, tracks the roadmap, hosts architecture diagrams and case studies, and renders a deployable hub site. The actual shared implementation lives in [ai-marketing-shared](../../ai-marketing-shared).

## Layers

```
+-------------------------------------------------------------+
|  HUB LAYER       ai-marketing-portfolio-meta                |
|  narrative · standards · roadmap · architecture · case      |
|  studies · diagrams · Astro hub site                        |
+-------------------------------------------------------------+
|  FOUNDATION      ai-marketing-shared (v0.1.0)               |
|  schemas · tools · mcp · tracing · cost · fallback · eval · |
|  providers · demo                                            |
+-------------------------------------------------------------+
|  FLAGSHIP        ai-marketing-growth-os                     |
|  agentic marketing intelligence platform                    |
+-------------------------------------------------------------+
|  STRATEGIC       ai-marketing-mix-copilot                   |
|  Bayesian MMM + incrementality + scenarios                  |
+-------------------------------------------------------------+
|  CORE MODULES    content-ops · journey-orchestrator · cro · |
|  data-quality                                               |
+-------------------------------------------------------------+
|  INTELLIGENCE    knowledge-graph · competitive-intel ·      |
|  feedback-intel                                             |
+-------------------------------------------------------------+
|  GOVERNANCE      brand-safety · local-geo · lead-scoring ·  |
|  affiliate · digital-twin                                   |
+-------------------------------------------------------------+
|  RELIABILITY     ai-agent-testing-lab                       |
|  evaluates every other repo in CI                           |
+-------------------------------------------------------------+
```

## Dependency rules

1. **Everything imports `ai-marketing-shared`.** Shared schemas (Recommendation, Evidence, AgentRun, ToolCall, ApprovalItem), the Tool base class with permission levels, the MCP adapter, tracing/logging, cost accounting, the rule-based fallback engine, the eval harness, and the provider abstraction are defined once and reused everywhere.
2. **Everything is evaluated by `ai-agent-testing-lab`.** Every repo's CI calls the lab and reports metrics.
3. **Everything is documented in this hub.** The standards live in `docs/standards.md`, the build order in `docs/roadmap.md`, and each shipped repo gets a case study in `docs/case-studies/`.
4. **No repo invents its own conventions.** Same structure, same naming, same MIT license, same CI, same Conventional Commits.

## Data and control flow (typical repo)

```
data sources -> connectors -> agents (tool-using, structured output)
   -> orchestration (dedupe, prioritize) -> unified action plan
   -> approval queue (pending/approved/rejected/executed/measured)
   -> measured outcome -> eval suite -> CI metrics
```

Every agent run is traced: inputs, tool calls, outputs, cost, latency (`AgentRun` / `ToolCall` schemas). No consequential action — publish, budget change, campaign edit, send message — happens without human approval.

## Hub site

The `site/` directory is a minimal Astro site that renders this hub and links to all repositories. It is static, deployable to Vercel or GitHub Pages, and does not require any API keys. Repository links are built from the `GITHUB_OWNER` environment variable (see `.env.example`), so the same site can be repointed when remotes are created.

## Design decisions and tradeoffs

- **Hub-as-docs, not hub-as-code.** The hub deliberately stays documentation-only so the shared implementation has a single home (`ai-marketing-shared`) and no duplicate logic creeps in.
- **Shared package before anything else.** Schemas and tooling are the contract every repo builds against; building them first prevents divergent conventions across 17 repos.
- **One case study per major repo.** Depth over breadth: a single well-evaluated system is worth more than twenty shallow demos, and the case studies show evaluation and results, not just screenshots.
- **Mermaid source plus PNG.** Mermaid is editable in-repo; the PNG gives a render that works anywhere without a Mermaid renderer.
- **Astro over a heavier framework for the hub.** Static-first, zero JavaScript by default, trivially deployable — the hub is content, not an application.
- **Light CI for the hub.** A link checker plus a site build keep the hub honest without pretending it is an application repo; full lint/test/eval CI belongs to the system repositories.
