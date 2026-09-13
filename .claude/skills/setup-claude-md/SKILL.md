# Setup Claude MD Skill

This skill generates a CLAUDE.md file for any project by analyzing the project structure and generating appropriate guidance for Claude Code.

When invoked, follow these steps:

## Step 1: Analyze Project Structure
- Use Glob to find key files that indicate project type and structure
- Look for: package.json, requirements.txt, setup.py, pyproject.toml, Cargo.toml, go.mod, pom.xml, build.gradle, etc.
- Identify primary language(s) and framework(s)
- Note existing documentation files (README.md, AGENTS.md, etc.)
- Check for configuration files (.env.example, docker-compose.yml, etc.)

## Step 2: Determine Hard Rules and Stop Conditions
- If AGENTS.md exists, read it for hard rules and stop conditions
- If CLAUDE.md exists, read it for reference
- Otherwise, use these default hard rules:
  - Stay within existing directory boundaries (backend/frontend/etc.)
  - Do not execute git commit/tag/push without explicit confirmation
  - Commit messages must be in English without Co-Authored-By
  - Do not hardcode secrets, accounts, paths, model names, ports
  - Reuse existing modules/configuration/scripts/tests; avoid parallel implementations
  - Prioritize stability over "handy optimizations"
  - When adding new configuration items, update .env.example and documentation
  - For user-visible changes, update documentation and CHANGELOG.md
  - Issue/PR screenshots and visual evidence must not be committed; use PR descriptions/attachments
  - CHANGELOG.md [Unreleased] section uses flat format: `- [类型] 描述`
  - README.md is for project positioning only; avoid unnecessary updates
  - For finer module behavior, update docs/*.md instead of README.md
  - When changing bilingual documents, assess synchronization needs
  - Comments/docstrings/log copy should be clear and accurate; consistent with file context
- Default stop conditions:
  - Correctness or security issues
  - Blocking-type CI failures
  - PR description contradicts actual changes
  - Lacking rollback plan
  - Repeatedly unresolved contract drift/patch stacking/validation distortion
  - Uncertain impact on user-visible capabilities/API behavior/deployment/notification/report structures
  - Uncertain impact on API/Schema/authentication linked changes
  - Uncertain impact on workflows/scripts/Docker changes
  - Uncertain impact on network/third-party dependency changes

## Step 3: Determine Core Commands
- Identify project type(s) from found files:
  - Python: requirements.txt, setup.py, pyproject.toml, Pipfile
    - Install: `pip install -r requirements.txt`
    - Test: `./scripts/ci_gate.sh` or `python -m pytest -m "not network"`
    - Run: `python main.py` (or with --webui for web interface)
    - Server: `uvicorn server:app --reload --host 0.0.0.0 --port 8000`
    - Web frontend: `cd apps/dsa-web && npm run lint && npm run build`
    - Desktop frontend: `cd apps/dsa-desktop && npm run build` (after web)
  - Node.js: package.json
    - Install: `npm ci`
    - Test: `npm test`
    - Run: `npm start`
    - Build: `npm run build`
    - Lint: `npm run lint`
  - Java: pom.xml or build.gradle
    - Install: `mvn clean install` or `gradle build`
    - Test: `mvn test` or `gradle test`
    - Run: `mvn spring-boot:run` or `gradle bootRun`
  - Rust: Cargo.toml
    - Install: `cargo build`
    - Test: `cargo test`
    - Run: `cargo run`
  - Go: go.mod
    - Install: `go mod download`
    - Test: `go test ./...`
    - Run: `go run .`
    - Build: `go build`
- Adjust commands based on actual project structure (e.g., if main.py is in src/, adjust path)
- Include commands for linting, formatting, and type checking if applicable
- For web projects, include commands for development server and production build

## Step 4: Identify Authority and Important Files
- Authority files:
  - AGENTS.md: Single source of truth for repository AI collaboration rules
  - CLAUDE.md: Must symlink to AGENTS.md for Claude ecosystem compatibility
  - .github/copilot-instructions.md and .github/instructions/*.instructions.md: GitHub Copilot/Coding Agent mirrors
- Important directories/files to note:
  - Skills: .claude/skills/ (can be committed); analysis artifacts: .claude/reviews/ (local)
  - Root SKILL.md and docs/openclaw-skill-integration.md: product/external integration explanations
  - Verification script: `python scripts/check_ai_assets.py`
  - Key entry points: 
    - Main: main.py, server.py, app.js, index.js, main.go, main.rs, etc.
    - Web frontend: apps/dsa-web/, src/, public/
    - Desktop: apps/dsa-desktop/, electron/
    - Backend: src/, api/, bot/, data_provider/
    - Configuration: .env.example, config/, docker-compose.yml
    - Workflows: .github/workflows/
    - Scripts: scripts/, .github/scripts/
    - Tests: tests/, __tests__, spec/
    - Documentation: docs/, README.md, CHANGELOG.md
- Describe core responsibilities by directory:
  - src/core/ or similar: main process orchestration
  - src/services/: business service layer
  - src/repositories/: data access layer
  - src/reports/: report generation
  - src/schemas/: schema/data structures
  - data_provider/: multi-source adaptation with fallback
  - api/: API layer
  - bot/: robot/integration access
  - scripts/: local automation scripts
  - .github/scripts/: GitHub automation scripts
  - tests/: test suites
  - docs/: documentation and instructions

## Step 5: Generate CLAUDE.md Content
Create a file with exactly these sections:

```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Hard Rules
[List hard rules as bullet points, max 150 lines total]

## Core Commands
[List essential commands for development, building, testing, running]

## Authority & Important Files
[Describe key files, directories, and their purposes]

## Stop Conditions
[List specific scenarios where Claude must stop and ask the user]
```

## Step 6: Write the File
- Use Write tool to create/overwrite CLAUDE.md with the generated content
- If CLAUDE.md already exists, back it up first (e.g., to CLAUDE.md.bak) unless user confirms overwrite
- Keep the file under 150 lines; prefer deletion over verbosity
- Use bullet points only; avoid long paragraphs
- Include only universally applicable hard rules and essential workflows
- Do not guess uncertain project details; omit if unclear