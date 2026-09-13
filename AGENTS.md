# AGENTS.md

This file is used to constrain the default development process of this repository, aiming to reduce repetitive communication, reduce rework, and ensure that changes are consistent with the current project structure.

If this file is inconsistent with scripts, workflows, or code status in the repository, the actual executable content shall prevail, and the document shall be corrected accordingly in related changes to prevent the rule from continuing to drift.

## 1. Hard Rules

- Follow existing directory boundaries:
  - Backend logic preferably placed in `src/`, `data_provider/`, `api/`, `bot/`
  - Web frontend changes in `apps/dsa-web/`
  - Desktop endpoint changes in `apps/dsa-desktop/`
  - Deployment and pipeline changes in `scripts/`, `.github/workflows/`, `docker/`
- Do not execute `git commit`, `git tag`, `git push` without explicit confirmation.
- Commit messages use English, without adding `Co-Authored-By`.
- Do not hardcode secrets, accounts, paths, model names, ports, or environment difference logic.
- Prioritize reuse of existing modules, configuration entry points, scripts, and tests; avoid adding parallel implementations.
- Default stability priority over "handy optimizations"; refactoring, abstraction, and infrastructure migration not directly required by the current task shall be restrained.
- When adding new configuration items, must synchronously update `.env.example` and related documents.
- When involving user-visible capabilities, CLI/API behavior, deployment methods, notification methods, or report structure changes, must synchronously update related documents and `docs/CHANGELOG.md`.
- When modifying report format, report rendering effects, or Web UI interface, PR description must attach screenshots of affected reports/pages; for before-after differences, prioritize before-after comparisons; if screenshots cannot be taken, explain why and provide alternative visual evidence.
- Issue/PR process screenshots, review screenshots, one-time acceptance screenshots, and temporary visual evidence must not be committed as repository files; they should be placed in PR description, PR comments, GitHub attachments, Actions artifacts, or external accessible evidence links. Long-term product documentation requiring retention of schematic images is exempt, but file names and document semantics must be detached from specific issue/PR numbers.
- The `[Unreleased]` section of `docs/CHANGELOG.md` uses flat format: each item on its own line, format `- [类型] 描述`, type values: `新功能`/`改进`/`修复`/`文档`/`测试`/`chore`; prohibited to add new `### 类目标标题` in `[Unreleased]` to reduce merge conflicts. The maintainer consolidates into titled formal format upon release.
- `README.md` is only used for project positioning, core capabilities overview, quick start, main entry points, sponsorship/cooperation homepage-level information; avoid unnecessary updates to prevent continual bloat.
- For finer module behavior, page interactions, special configurations, troubleshooting instructions, field contracts, implementation semantics, and boundary conditions, prioritize updating corresponding `docs/*.md` or specialized documents, not writing into `README.md`.
- When changing one of the bilingual documents, assess whether the other needs synchronization; if not synchronized, the delivery explanation should state the reason.
- Comments, docstrings, and log copy should be clear and accurate; English is not enforced, but should be consistent with the file context.

### 1.1 PR Title Specification (Non-blocking Suggestion)

- It is recommended to use `<类型>: <修改内容>` as the PR title, for example `fix: 修复大盘分析历史记录丢失`, with priority given to types `fix`/`feat`/`refactor`/`docs`/`chore`/`test`/`ci`.
- The title should describe the actual change content; it is recommended not to add `[codex]`, `codex`, `autocode`, `copilot`, or other tool/agent source prefixes.
- This specification is only used for collaboration readability and consistency tips, and should not be used alone as a review process blocker.

### 1.2 Contribution Quality Bottom Line

- This repository does not accept PRs that substitute genuine design convergence with code volume stacking, diff face expansion, or patch-style responses to reviews.
- Contribution quality is judged by whether it solves clear problems, minimizes impact surface, maintains existing contract consistency, and covers real risk paths; not by new line count, file quantity, feature publicity, or "looks complete".
- Please do not treat this repository as a low-cost trial field, resume display field, or contribution farming field. Any PR must prove that the author understands the current system contract and has completed basic self-review, integration, and verification.
- Using AI-assisted development itself is not a problem; the problem is submitting AI-generated code without human semantic review, verification, and convergence. Such PRs will be treated as low-quality submissions.
- After review feedback, do not accept only adding local patches at the locations pointed out by reviewers. The author must re-examine all entrances, configurations, tests, documents, workflows, and user-visible paths related to the same business semantics.
- If a PR still exhibits the same contract drift, repeated fallback, test bypassing real risk layers, PR body and actual diff inconsistency, etc., after multiple rounds of review, maintainers may require closing and redoing instead of continuing point-by-point review.

## 2. AI Collaboration Asset Governance

- `AGENTS.md` is the sole true source of AI collaboration rules within the repository.
- `CLAUDE.md` must be a symlink pointing to `AGENTS.md` for Claude ecosystem compatibility.
- `.github/copilot-instructions.md` and `.github/instructions/*.instructions.md` are mirrors or layered supplements for GitHub Copilot/Coding Agent; if they conflict with this file, this file (`AGENTS.md`) takes precedence.
- Repository collaboration skills are stored in `.claude/skills/`; analysis artifacts are stored in `.claude/reviews/`; the former can be committed, the latter are by default regarded as local products.
- Root `SKILL.md` and `docs/openclaw-skill-integration.md` belong to product or external integration explanations, not the repository collaboration rules true source.
- If in the future `.agents/skills/` or other agent-specific directories are added, a single true source must be clarified first, then synchronized via scripts or mirroring; manual long-term maintenance of multiple synonymous contents is prohibited.
- When modifying AI collaboration governance assets, execute:
  ```bash
  python scripts/check_ai_assets.py
  ```

## 3. Repository Overview

- Project positioning: Intelligent stock analysis system, covering A-shares, Hong Kong stocks, US stocks.
- Main process: Data retrieval -> Technical analysis/news retrieval -> LLM analysis -> Report generation -> Notification push.
- Key entrances:
  - `main.py`: Main entrance for analysis tasks
  - `server.py`: FastAPI service entrance
  - `apps/dsa-web/`: Web frontend
  - `apps/dsa-desktop/`: Electron desktop endpoint
  - `.github/workflows/`: CI, release, daily tasks
- Core responsibilities:
  - `src/core/`: Main process orchestration
  - `src/services/`: Business service layer
  - `src/repositories/`: Data access layer
  - `src/reports/`: Report generation
  - `src/schemas/`: Schema/data structures
  - `data_provider/`: Multi-source adaptation with fallback
  - `api/`: FastAPI API
  - `bot/`: Robot access
  - `scripts/`: Local scripts
  - `.github/scripts/`: GitHub automation scripts
  - `tests/`: pytest tests
  - `docs/`: Documentation and instructions

## 4. Common Commands

### Run Application

```bash
python main.py
python main.py --debug
python main.py --dry-run
python main.py --stocks 600519,hk00700,AAPL
python main.py --market-review
python main.py --schedule
python main.py --serve
python main.py --serve-only
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

### Backend Verification

```bash
pip install -r requirements.txt
pip install flake8 pytest
./scripts/ci_gate.sh
python -m pytest -m "not network"
python -m py_compile <changed_python_files>
```

### Web/Desktop

```bash
cd apps/dsa-web
npm ci
npm run lint
npm run build

cd ../dsa-desktop
npm install
npm run build
```

### PR/CI Evidence

```bash
gh pr view <pr_number>
gh pr checks <pr_number>
gh run view <run_id> --log-failed
```

## 5. Default Workflow

1. First determine task type: `fix`/`feat`/`refactor`/`docs`/`chore`/`test`/`review`
2. Read existing implementation, configuration, tests, scripts, workflows, and documents before making modifications.
3. Identify change boundaries: backend/API/Web/Desktop/Workflow/Docs/AI collaboration assets.
4. First determine whether it hits high-risk areas: configuration semantics, API/Schema, data source fallback, report structure, authentication, scheduling, release process, desktop startup chain.
5. Only make the smallest change directly related to the current task; do not sneak in unrelated refactoring.
6. If documentation, scripts, or workflow descriptions are found to be inconsistent, trust the actual code and workflow first, then decide whether to correct the documentation.
7. After completion, execute checks according to the verification matrix below.
8. Final delivery should default to explaining:
   - What was changed
   - Why it was changed this way
   - Verification status
   - Unverified items
   - Risk points
   - Rollback method

## 6. Verification Matrix

### CI Coverage Principle

Current repository CI mainly includes:

| Check Item | Source | Description | Whether Blocking |
|------------|--------|-------------|------------------|
| `ai-governance` | `.github/workflows/ci.yml` | Validates `AGENTS.md`/`CLAUDE.md`/`.github` instructions/`.claude/skills` relationship | Yes |
| `backend-gate` | `.github/workflows/ci.yml` | Executes `./scripts/ci_gate.sh` | Yes |
| `docker-build` | `.github/workflows/ci.yml` | Docker build and key module import smoke test | Yes |
| `web-gate` | `.github/workflows/ci.yml` | When frontend changes, execute `npm run lint` + `npm run build` | Yes (when triggered) |
| `network-smoke` | `.github/workflows/network-smoke.yml` | `pytest -m network` + `scripts/test.sh quick` | No, observation item |
| `pr-review` | `.github/workflows/pr-review.yml` | PR static check + AI review + automatic labeling | No, auxiliary item |

If corresponding CI results already exist on the PR, CI conclusions can be directly cited; if CI does not cover the change surface, or local and CI environment differences are large, local verification needs to be supplemented with explanation of the gap.

### By Change Surface Execution

- **Backend Python changes**:
  - Applicable scope: `main.py`, `src/`, `data_provider/`, `api/`, `bot/`, `tests/`
  - Priority execution: `./scripts/ci_gate.sh`
  - Minimum requirement: `python -m py_compile <changed_python_files>`
  - If affecting API, task scheduling, report generation, notification sending, data source fallback, authentication, scheduling, the delivery explanation should clarify whether the corresponding paths have been covered.

- **Web frontend changes**:
  - Applicable scope: `apps/dsa-web/`
  - Default execution: `cd apps/dsa-web && npm ci && npm run lint && npm run build`
  - If involving API联调, routing, state management, Markdown/chart rendering, or authentication status, the delivery explanation should clearly state the联调 surface and uncovered risks.

- **Desktop endpoint changes**:
  - Applicable scope: `apps/dsa-desktop/`, `scripts/run-desktop.ps1`, `scripts/build-desktop*.ps1`, `scripts/build-*.sh`, `docs/desktop-package.md`
  - Default execution: build Web first, then build desktop endpoint
  - If platform limitations prevent complete validation, it is necessary to clearly state whether Web build products, Electron build, and release workflow impact have been validated.

- **API/Schema/authentication联动 changes**:
  - Applicable scope: `api/**`, `src/schemas/**`, `src/services/**`, `apps/dsa-web/**`, `apps/dsa-desktop/**`
  - At least cover corresponding backend validation + affected client build validation.
  - If involving login, Cookie, session, polling status, field addition/deletion or enumeration changes, compatibility impact must be clearly stated.

- **Document and governance file changes**:
  - Applicable scope: `README.md`, `docs/**`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/**`, `.claude/skills/**`
  - No mandatory code testing.
  - Need to confirm commands, configuration items, file names, workflow names match actual repository.
  - When modifying AI collaboration governance assets, execute `python scripts/check_ai_assets.py`.

- **Workflow/script/Docker changes**:
  - Applicable scope: `.github/**`, `scripts/**`, `docker/**`
  - Run local validation closest to the change surface.
  - When delivering, explain which pipelines, release paths, or deployment paths are affected.
  - If Docker/GitHub Actions-related validation is not executed, clearly state the reason and potential risks.

- **Network or third-party dependency-related changes**:
  - First run offline or deterministic checks.
  - Prioritize confirming whether timeout, retry, fallback, exception copy, downgrade paths are still valid.
  - If online validation is not executed, the reason must be clearly stated.

## 7. Stability Guardrails

- **Configuration and run entrances**:
  - When modifying `.env` semantics, default values, CLI parameters, service startup methods, or scheduling semantics, the impact on local operation, Docker, GitHub Actions, API, Web, Desktop should be simultaneously evaluated.
  - New configuration priority: "可运行也可不配置，配置后增强能力" to avoid stacking switches and mutually exclusive modes.

- **Data source and fallback**:
  - When modifying `data_provider/`, pay attention to data source priority, failure degradation, field standardization, cache and timeout strategy.
  - Single data source failure should not drag down the entire analysis process, unless requirements explicitly require fail-fast.

- **API/Web/Desktop compatibility**:
  - When changing API/Schema/authentication/report payload, the backend, Web, and Desktop compatibility should be simultaneously checked.
  - Default priority: append fields, retain old fields, or provide compatibility layer to avoid silent breaking of existing clients.

- **Report/Prompt/Notification**:
  - When modifying report structure, Prompt, extractor, notification template, or robot link, upstream input and downstream consumer compatibility should be checked.
  - Single notification channel failure should not drag down the entire analysis main process, unless requirements explicitly require fail-fast.
  - When modifying `src/services/image_stock_extractor.py`'s `EXTRACT_PROMPT`, the PR description should attach the complete latest prompt.

- **Workflow/release/packaging**:
  - When modifying auto-tag, release, Docker release, daily analysis, or desktop packaging processes, evaluate trigger conditions, product paths, permission boundaries, and rollback methods.
  - Auto-tag defaults to opt-in: only commit titles containing `#patch`, `#minor`, `#major` trigger version number updates, unless requirements explicitly require changing release strategy.

## 8. Issue/PR/Skill Workflow

- The repository has the following skills available for preferential reuse:
  - `.claude/skills/analyze-issue/SKILL.md`
  - `.claude/skills/analyze-pr/SKILL.md`
  - `.claude/skills/fix-issue/SKILL.md`
- If the task is clearly issue analysis, PR review, or issue fixing, prioritize executing according to the corresponding skill, and save the product to `.claude/reviews/`.
- Skill commands, templates, verification sequence, and delivery structure must be consistent with `AGENTS.md`.
- Before each PR creation/update, PR review, or issue analysis, the latest code baseline must be synchronized first: check workspace status and execute `git fetch --all --prune`; if workspace is clean and current branch can fast-forward, execute `git pull --ff-only`. If there are local changes, conflict status, untracked risk files, or inability to fast-forward, do not forcibly switch branches, stash, reset, or overwrite local state; PR review/issue analysis can use already fetched remote refs/PR head for analysis, and the analysis document should clearly record the reason for not updating the local workspace tree, current local HEAD vs. used remote baseline; PR creation/update should first explain the difference between current branch and target baseline, and request user confirmation for rebase/merge or continuing based on current branch if necessary.
- Skills default to prioritizing CI/workflow evidence, then deciding whether to supplement local validation.
- Except for the PR creation/update/PR review/issue analysis safe fast-forward synchronization above, skills must not default to executing `git pull`, `git push`, `git tag`, `gh pr create`, etc., operations that change remote or current branch status; these operations must require user confirmation.
- PR review default sequence:
  1. Necessity
  2. Relevance
  3. Title suggestion (`<类型>: <修改内容>`, tool/agent prefixes not included; not a hard blocker)
  4. Description completeness (check against `.github/PULL_REQUEST_TEMPLATE.md`)
  5. Validation evidence
  6. Implementation correctness
  7. Merge judgment
- For `fix` type PRs, it is necessary to explain: original problem, root cause, fix point, regression risk.
- Merge blocking conditions:
  - Correctness or security issues
  - Blocking-type CI not passed
  - PR description substantially contradicts actual change content
  - Lack of rollback plan
  - Repeated occurrence of unresolved contract drift, patch stacking, or validation evidence distortion

## 8.1 Review Feedback Processing and Patch Stacking Prohibition

When processing review feedback, it is prohibited to only add local patches at the locations pointed out by reviewers and then claim "all fixed". You must first re-understand the business contract pointed out by the reviewer, then check all entrances, configurations, tests, documents, workflows, and user-visible paths related to the same language semantics.

After receiving review feedback, the following steps must be followed:

1. List out the original problems pointed out by the reviewer item by item.
2. Explain the root cause, not just describe "which few lines were changed".
3. Find all related paths affected by the same language semantics, such as runtime, API/Web, CLI, diagnostics, workflow, docs, tests.
4. Fix the complete contract, not just fix the current failed test or current comment line.
5. Supplement regression test cases that can cover the reviewer's counterexample, final entrance verification, or clearly explain why verification is not possible.
6. Synchronize the PR body to ensure scope, validation results, compatibility, risk, and rollback plan are consistent with the current HEAD.

If the above convergence cannot be completed, do not continue to stack patches and do not claim ready for merge. Proactively explain that the current PR needs to be split, closed and redone, or request maintainer confirmation of a new minimum range.

The following behaviors will be regarded as low-quality PRs:

- Using broad fallback, silent degradation, `return False/None/[]` to cover unclear contracts.
- Test mocks bypassing real risk layers, only proving local implementation passes.
- After CI passes, claim the problem is closed, but without covering the reviewer's counterexample.
- After review, continue to add scattered patches instead of re-converging the complete language semantics.
- The same business semantics shows inconsistency in runtime, Web/API, docs, workflow, and tests.

CI passing can only indicate that automatic checks passed, cannot replace human semantic convergence, nor can it alone prove that the reviewer's counterexample has been closed.

## 9. Delivery and Release

- Default delivery structure:
  - What was changed
  - Why it was changed this way
  - Verification status
  - Unverified items
  - Risk points
  - Rollback method
- If it is a `docs` task, can directly write: `Docs only, tests not run`, but still need to confirm whether commands and file names were confirmed.
- Auto-tag defaults to not trigger; only commit titles containing `#patch`, `#minor`, `#major` will trigger version number updates.
- Manual tagging must use annotated tags.
- User-visible changes are preferably merged via PR, and labels and verification explanations are supplemented.