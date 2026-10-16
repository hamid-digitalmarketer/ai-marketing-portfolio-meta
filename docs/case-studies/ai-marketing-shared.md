# Case Study: ai-marketing-shared

**Status:** Done · v0.1.0 · commit `1dd8024` · MIT

## Problem

A 17-repository portfolio only works if every repository speaks the same language. Without a shared foundation, each repo would reinvent schemas, tool wrappers, tracing, cost accounting, evaluation, and provider plumbing — producing inconsistent, unmaintainable, and un-evaluable systems. The problem: define the shared contract **once**, implement it **well**, and make every other repo depend on it.

## Approach

Build a small, typed, testable Python package (`ai_marketing_shared`) that encodes the portfolio's core principles directly in code:

- **Structured outputs** — Pydantic v2 schemas for `Recommendation`, `Evidence`, `AgentRun`, `ToolCall`, `ApprovalItem`, so every agent output is validated at the boundary.
- **Tool-using agents** — a `Tool` base class with explicit permission levels (`read`, `write`, `external`) and a uniform MCP adapter interface, so agents call defined functions and never hallucinate numbers.
- **Observability** — tracing utilities that record inputs, tool calls, outputs, cost, and latency for every agent run.
- **Cost controls** — cost accounting utilities plus a rule-based fallback engine and a zero-API-key demo mode with precomputed fixtures.
- **Evaluation** — an eval harness with dataset loaders and metric reporters, so every repo can report accuracy, precision/recall, calibration, tool-use success, cost, latency, and reliability.
- **Modularity** — a provider abstraction (OpenAI, Anthropic, local, mock) so providers are swappable via interfaces.

## Architecture

```
ai_marketing_shared/
+-- schemas.py     # Pydantic v2 schemas (Recommendation, Evidence, AgentRun, ToolCall, ApprovalItem)
+-- tools.py       # Tool base class + permission levels
+-- mcp.py         # MCP adapter interface
+-- tracing.py     # tracing/logging utilities
+-- cost.py        # cost accounting utilities
+-- fallback.py    # rule-based fallback engine
+-- eval.py        # eval harness (dataset loaders + metric reporters)
+-- providers.py   # provider abstraction (OpenAI, Anthropic, local, mock)
+-- demo.py        # rule-based demo mode, zero API keys, fixtures
```

The package is installed via `pyproject.toml` and imported by every other repository.

## Evaluation

- Unit test suite covering schemas, tools, MCP adapter, tracing, cost, fallback, eval harness, and providers.
- Coverage target **>90%** on core modules; suite verified locally with tests passing.
- Ruff and mypy clean; CI configured to lint, type-check, test, and eval.
- Demo mode runs with **zero API keys** (mock provider is the default).

## Results

- v0.1.0 released with the complete shared foundation: schemas, tooling, tracing, cost, fallback, eval harness, provider abstraction, demo mode.
- Every subsequent portfolio repository imports this package — the shared contract is now a dependency, not a convention.
- Committed locally as `1dd8024`; remote to be created and pushed.

## Lessons

- **Contracts before features.** Defining schemas and interfaces first made the package small and the API surface stable; downstream repos can build against a settled contract.
- **Default to mock.** Making the mock provider the default forces zero-API-key runnability to be the baseline, not an afterthought.
- **Coverage is a proxy, not a goal.** The >90% target helped, but the real win was testing each module's *behavior* (permission enforcement, fallback correctness, cost accounting) rather than just line counts.
- **Keep the hub separate from the implementation.** The shared code lives here; the standards and roadmap that describe it live in `ai-marketing-portfolio-meta`. No duplication, no drift.
