# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Hard Rules
- Stay within existing directory boundaries: backend logic in `src/`, `data_provider/`, `api/`, `bot/`; web frontend in `apps/dsa-web/`; desktop in `apps/dsa-desktop/`; deployment and pipelines in `scripts/`, `.github/workflows/`, `docker/`.
- Do not execute `git commit`, `git tag`, `git push` without explicit confirmation.
- Commit messages must be in English, without `Co-Authored-By`.
- Do not hardcode secrets, accounts, paths, model names, ports, or environment-specific logic.
- Reuse existing modules, configuration entry points, scripts, and tests; avoid adding parallel implementations.
- Prioritize stability over "handy optimizations"; refrain from refactoring, abstraction, or infrastructure migration not directly required by the current task.
- When adding new configuration items, must simultaneously update `.env.example` and related documentation.
- For changes affecting user-visible capabilities, CLI/API behavior, deployment methods, notification methods, or report structures, must update related documentation and `docs/CHANGELOG.md`.
- When modifying report format, report rendering effects, or Web UI interface, PR description must include affected report/page screenshots; for before-after differences, prioritize before-after comparisons; if screenshots cannot be taken, explain why and provide alternative visual evidence.
- Issue/PR process screenshots, review screenshots, one-time acceptance screenshots, and temporary visual evidence must not be committed as repository files; place them in PR description, PR comments, GitHub attachments, Actions artifacts, or external accessible evidence links. Long-term product documentation requiring retention of schematic images is exempt, but file names and document semantics must be detached from specific issue/PR numbers.
- `docs/CHANGELOG.md` `[Unreleased]` section uses flat format: each item on its own line, format `- [类型] 描述`, type values: `新功能`/`改进`/`修复`/`文档`/`测试`/`chore`; prohibited to add new `### 类目标头` in `[Unreleased]` to reduce merge conflicts. Maintainer consolidates into titled formal format upon release.
- `README.md` is only for project positioning, core capabilities overview, quick start, main entry points, sponsorship/cooperation homepage-level information; avoid unnecessary updates to prevent continual bloat.
- For finer module behavior, page interactions, special configurations, troubleshooting instructions, field contracts, implementation semantics, and boundary conditions, update corresponding `docs/*.md` or specialized documents instead of writing into `README.md`.
- When changing one of the bilingual documents, assess whether the other needs synchronization; if not synchronized, mention the reason in the delivery explanation.
- Comments, docstrings, and log copy should be clear and accurate; do not enforce English, but should be consistent with the file context.

## Core Commands
- Install dependencies: `pip install -r requirements.txt` (backend) and `npm ci` (frontend)
- Run backend tests: `./scripts/ci_gate.sh` or `python -m pytest -m "not network"`
- Run the stock analysis: `python main.py` (or with `--webui` for the web interface)
- Run the FastAPI server: `uvicorn server:app --reload --host 0.0.0.0 --port 8000`
- Lint and build web frontend: `cd apps/dsa-web && npm run lint && npm run build`
- Lint and build desktop frontend: `cd apps/dsa-desktop && npm run build` (after building web)

## Authority & Important Files
- `AGENTS.md`: The single source of truth for repository AI collaboration rules; `CLAUDE.md` must be a symlink pointing to `AGENTS.md` for Claude ecosystem compatibility.
- `.github/copilot-instructions.md` and `.github/instructions/*.instructions.md`: GitHub Copilot/Coding Agent mirrors or layered supplements; in case of conflict, `AGENTS.md` takes precedence.
- Repository collaboration skills: stored in `.claude/skills/`; analysis artifacts stored in `.claude/reviews/`; the former can be committed, the latter are default local products.
- Root `SKILL.md` and `docs/openclaw-skill-integration.md`: product or external integration explanations, not the repository collaboration rules truth source.
- To verify AI collaboration governance assets, run: `python scripts/check_ai_assets.py`
- Key entry points: `main.py` (analysis task main entry), `server.py` (FastAPI service entry), `apps/dsa-web/` (web frontend), `apps/dsa-desktop/` (Electron desktop), `.github/workflows/` (CI, release, daily tasks)
- Core responsibilities: `src/core/` (main process orchestration), `src/services/` (business service layer), `src/repositories/` (data access layer), `src/reports/` (report generation), `src/schemas/` (schema/data structures), `data_provider/` (multi-source adaptation with fallback), `api/` (FastAPI API), `bot/` (robot access), `scripts/` (local scripts), `.github/scripts/` (GitHub automation scripts), `tests/` (pytest tests), `docs/` (documentation and instructions)

## Stop Conditions
- When encountering correctness or security issues, stop and ask the user.
- When encountering blocking-type CI failures, stop and ask the user.
- When PR description substantively contradicts actual changes, stop and ask the user.
- When lacking a rollback plan, stop and ask the user.
- When encountering repeatedly unresolved contract drift, patch stacking, or validation evidence distortion, stop and ask the user.
- When uncertain about the impact on user-visible capabilities, CLI/API behavior, deployment methods, notification methods, or report structures, stop and ask the user before making changes.
- When uncertain about the impact on API/Schema/authentication linked changes, stop and ask the user to confirm compatibility implications.
- When uncertain about the impact on workflows, scripts, or Docker changes, stop and ask the user to confirm which pipelines, release paths, or deployment paths are affected.
- When uncertain about the impact on network or third-party dependency changes, stop and ask the user to confirm if online verification is needed and why it might be skipped.