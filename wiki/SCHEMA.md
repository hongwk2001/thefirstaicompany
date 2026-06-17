# Wiki Schema

## Domain
This wiki covers **Hermes Setup, Local DevOps configurations, and TKPROF AI Agent Factory Multi-Agent Swarm Architectures**. It acts as the core procedural memory and architecture blueprint for localized, file-backed swarm coordination sandboxes.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `mailbox-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/.../source-file.md]` at the end of paragraphs whose claims come from a specific source.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
---
```

## Tag Taxonomy
- `runtime`: Central execution engine, orchestrator, and environments (Hermes, WSL).
- `local-llm`: Offline local inference models and providers (Ollama, Qwen, Llama).
- `swarm`: Multi-agent transaction coordination networks and daemon engines.
- `security`: Gateways, lockdowns, permission rulesets, and user restrictions.
- `human-in-the-loop`: Synchronous approval gateways, clearances, and triage consoles.
- `dev-qa`: Autonomous compilation, testing, error-interception, and self-healing.
- `asset`: Video reels, speech synthesis, image assets, and compiling.
- `strategy`: Strategic comparisons, architectural syntheses, and design paradigms.

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed, add it here first, then use it.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source.
- **Add to existing page** when a source mentions something already covered.
- **DON'T create a page** for passing mentions or minor details.
- **Split a page** when it exceeds ~200 lines.
- **Archive a page** when its content is fully superseded (move to `_archive/`).
