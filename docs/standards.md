---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: a60f8e46820ea466ef0868a20e79d739_ece38202c90811f196f9525400248c00
    ReservedCode1: tHzqLOw91+uUukEIhZio1FIXq3IBHDRhWTa9L6Qiy63rNRZeO7LzROvjcHE0WrpLjE8+6hQyg+RPa56WwguFmNy297O9HDZuQ/sqMiYKDZPq/XwXmx3okO6SjB9MY841TbPHH0D400LtDmaqxntYDa8Anh/4EYoL9lQFXm0mO7Y92eosryC/h0Iofgs=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: a60f8e46820ea466ef0868a20e79d739_ece38202c90811f196f9525400248c00
    ReservedCode2: tHzqLOw91+uUukEIhZio1FIXq3IBHDRhWTa9L6Qiy63rNRZeO7LzROvjcHE0WrpLjE8+6hQyg+RPa56WwguFmNy297O9HDZuQ/sqMiYKDZPq/XwXmx3okO6SjB9MY841TbPHH0D400LtDmaqxntYDa8Anh/4EYoL9lQFXm0mO7Y92eosryC/h0Iofgs=
---

# Shared Standards

This document defines the shared standards for the entire AI marketing engineering portfolio. They are defined once, in [ai-marketing-shared](../../ai-marketing-shared), and reused by every repository. Consistency is a first-class requirement: same repo structure, same naming, same license (MIT), same CI, same commit style.

## 1. Shared schemas (Pydantic v2)

All agent outputs conform to these schemas, defined in `ai_marketing_shared/schemas.py`.

### Recommendation

| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Stable unique identifier |
| `agent` | str | Agent that produced the recommendation |
| `issue` | str | Problem being addressed |
| `evidence[]` | Evidence[] | Supporting evidence, each item cited |
| `priority` | enum | e.g. critical / high / medium / low |
| `confidence` | float | 0..1 confidence in the recommendation |
| `expected_impact` | str | Anticipated business impact |
| `effort` | enum | e.g. low / medium / high |
| `proposed_action` | str | Concrete action to take |
| `next_steps[]` | str[] | Follow-up steps |
| `requires_approval` | bool | Whether human approval is mandatory |
| `status` | enum | e.g. pending / approved / rejected / executed / measured |

### Evidence

| Field | Type | Description |
|-------|------|-------------|
| `source` | str | Where the data came from |
| `metric` | str | Metric name |
| `value` | float | Metric value |
| `timestamp` | datetime | When the metric was observed |
| `confidence_interval` | tuple | Optional uncertainty bounds |
| `url` | str | Optional citation link |

### AgentRun

| Field | Type | Description |
|-------|------|-------------|
| `run_id` | str | Unique run identifier |
| `agent` | str | Agent name |
| `started_at` | datetime | Run start |
| `finished_at` | datetime | Run end |
| `input_summary` | str | Summarized input |
| `tool_calls[]` | ToolCall[] | All tool calls made |
| `recommendations[]` | Recommendation[] | Outputs |
| `token_cost` | float | Token usage accounting |
| `api_cost_estimate` | float | Estimated API cost |
| `latency_ms` | int | Wall-clock latency |
| `status` | enum | e.g. running / succeeded / failed |
| `error` | str | Error detail, if any |

### ToolCall

| Field | Type | Description |
|-------|------|-------------|
| `tool_name` | str | Tool invoked |
| `arguments` | dict | Arguments passed |
| `result_summary` | str | Summarized result |
| `latency_ms` | int | Tool latency |
| `token_cost` | float | Tokens consumed |
| `success` | bool | Call outcome |
| `error` | str | Error detail, if any |

### ApprovalItem

| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Approval identifier |
| `recommendation_id` | str | Linked recommendation |
| `status` | enum | pending / approved / rejected / executed / measured |
| `approver` | str | Human approver |
| `decided_at` | datetime | Decision timestamp |
| `outcome` | str | What happened after approval |

## 2. Shared tooling

All implemented in `ai-marketing-shared`:

- **Tool base class** with permission levels: `read`, `write`, `external` — least-privilege by default.
- **MCP adapter interface** — agents talk to external tools through a uniform adapter (`mcp.py`).
- **Tracing and logging utilities** — every agent run is traced with inputs, tool calls, outputs, cost, latency (`tracing.py`).
- **Cost accounting utilities** — token cost and API cost estimation, cost caps and rate limits (`cost.py`).
- **Rule-based fallback engine** — deterministic, zero-API-cost fallback for demo mode (`fallback.py`).
- **Eval harness** with dataset loaders and metric reporters (`eval.py`).
- **Provider abstraction** — OpenAI, Anthropic, local, and mock providers, swappable via interfaces (`providers.py`).
- **Demo mode** — rule-based, zero API keys, precomputed fixtures (`demo.py`).

## 3. Shared repo template

```
<repo-name>/
+-- backend/          # FastAPI app
+-- frontend/         # React or Next.js (if applicable)
+-- agents/           # Agent definitions
+-- tools/            # Tool functions + MCP adapters
+-- data/             # sample_data/ + connectors
+-- evaluation/       # datasets/ + pytest suites
+-- infra/            # docker-compose.yml, Dockerfiles
+-- docs/             # architecture.md, evaluation.md, cost-controls.md
+-- .github/workflows # CI
+-- .env.example
+-- README.md
+-- CONTRIBUTING.md
+-- LICENSE
+-- pyproject.toml
```

## 4. Shared CI (GitHub Actions)

Every repository runs: **lint** (ruff), **type-check** (mypy), **test** (pytest), **eval** (pytest `evaluation/`), **build docker image**.

The hub adds a light link check and site build — see [`.github/workflows/ci.yml`](../.github/workflows/ci.yml).

## 5. Shared design language for frontends

- Same color system, typography, spacing, and component library.
- Same **approval queue** component.
- Same **trace viewer** component.
- Same **recommendation card** component.

## 6. Engineering standards

- Python 3.11+, type hints everywhere, ruff + mypy clean.
- Pydantic v2 for all schemas.
- pytest with >80% coverage on core modules (shared library targets >90%).
- FastAPI with OpenAPI docs.
- React/Next.js with TypeScript and accessible components.
- Docker multi-stage builds.
- GitHub Actions: lint, type-check, test, eval, build.
- No secrets in code; `.env.example` in every repo.
- Semantic versioning and changelogs.
- MIT license in every repo.

## 7. Evaluation standards

Every repo ships:

- `evaluation/datasets/` with labeled examples.
- `evaluation/run.py` or a pytest suite.
- Metrics reported in CI: accuracy, precision/recall, calibration, tool-use success, cost, latency, reliability.
- A `docs/evaluation.md` summarizing methodology and current results.
- A baseline (rule-based) and an AI-based comparison where applicable.

## 8. Cost and safety standards

Every repo ships:

- Rule-based demo mode (zero API cost).
- Precomputed fixtures for demos.
- Cost caps and rate limits.
- `docs/cost-controls.md`.
- Human approval for all write actions.
- Input validation and sanitization.
- Prompt-injection resistance tests.
- Audit logging.

## 9. Documentation standards

Every repo ships:

- `README.md`: problem, approach, architecture diagram, setup, demo, evaluation summary, roadmap.
- `docs/architecture.md`: design decisions and tradeoffs.
- `docs/evaluation.md`: methodology and results.
- `docs/cost-controls.md`: how to run without cost.
- `CONTRIBUTING.md`, `LICENSE`, `CHANGELOG.md`.

## 10. Definition of done (per repo)

1. `docker compose up` works on a fresh machine with sample data.
2. Rule-based demo mode works with zero API keys.
3. All agents produce structured, evidence-backed outputs.
4. Approval queue works end-to-end.
5. Evaluation suite passes in CI and reports metrics.
6. Tests pass with >80% coverage on core modules.
7. Documentation is complete and accurate.
8. A demo GIF or video exists.
9. A release is tagged and the master README links to it.
10. A case study exists in portfolio-meta.
*（内容由AI生成，仅供参考）*
