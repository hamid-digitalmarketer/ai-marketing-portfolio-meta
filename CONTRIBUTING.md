# Contributing to ai-marketing-portfolio-meta

Thanks for taking the time to contribute. This is the hub of an AI marketing engineering portfolio; the same contribution standards apply to every repository in the portfolio.

## Ground rules

- All repositories are MIT licensed. Contributions are accepted under the same license.
- Follow the [shared standards](docs/standards.md): same repo structure, same naming, same CI, same commit style.
- Every agent system must ship evidence-backed recommendations, an approval queue, an eval suite, and a zero-API-key demo mode.
- Never hardcode secrets. Use `.env.example` and environment variables.
- Keep commits small, focused, and described with Conventional Commits.

## Commit style (Conventional Commits)

```
feat: add approval queue component
fix: correct confidence interval calculation in eval harness
docs: document cost-controls
test: add prompt-injection resistance cases
chore: bump shared dependency
refactor: extract provider abstraction
```

## Workflow

1. Fork the repository and create a feature branch (`feature/...` or `fix/...`).
2. Make focused commits following Conventional Commits.
3. Ensure the CI passes (link check + hub site build).
4. Open a pull request with a clear description of the change and, where relevant, evidence (test output, eval metrics).

## Reporting issues

Use the issue templates when available. Include:

- What you expected to happen and what actually happened.
- Steps to reproduce.
- Relevant environment details (OS, Python version, Node version).

## Code of conduct

Be respectful and constructive. The goal is to build one coherent, high-quality portfolio — depth over breadth, quality over quantity.
