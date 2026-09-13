# Repository Claude Skills

This directory stores repository-level collaboration skills, which are version control assets.

- Rule truth source: Repository root `AGENTS.md`
- Compatibility entry: Repository root `CLAUDE.md` (should be a symlink pointing to `AGENTS.md`)
- Skills in this directory need to be consistent with `AGENTS.md`
- `.claude/reviews/` belongs to local analysis products, not rule truth source

If future compatibility with other agent directories (such as `.agents/skills/` or `.github/skills/`) is needed, a single truth source should be clarified first, then synchronized via scripts or mirroring, rather than manually maintaining multiple synonymous contents long-term.