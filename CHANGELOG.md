# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Case study for ai-marketing-shared (full), placeholders for remaining major repositories.
- Hub site (Astro) — `site/` directory.

## [0.1.0] - 2026-10-16

### Added
- Portfolio hub scaffold:
  - `README.md` — narrative, architecture map, 17-repo table, start-here guide, 12 core principles, shared template.
  - `docs/standards.md` — shared standards (schemas, tooling, repo template, CI, design language).
  - `docs/roadmap.md` — build order and status for all 17 repositories.
  - `docs/architecture.md` — hub architecture and design decisions.
  - `docs/case-studies/` — case study index and per-repo case studies.
  - `docs/diagrams/architecture.mmd` + `docs/diagrams/architecture.png` — architecture diagrams.
  - `site/` — minimal Astro site rendering the hub (deployable to Vercel or GitHub Pages).
  - `LICENSE` (MIT), `CONTRIBUTING.md`, `.gitignore`, `.env.example`.
  - `.github/workflows/ci.yml` — light CI (markdown link check + hub site build).
