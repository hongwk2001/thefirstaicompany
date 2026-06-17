---
title: Surgical Diffs
created: 2026-06-12
updated: 2026-06-12
type: concept
tags: [dev-qa, runtime]
sources: [raw/articles/tkprof-factory-journey.md]
confidence: high
---
# Surgical Diffs

Surgical Diffs represent the core code-preservation strategy of the TKPROF factory, governed strictly by rules written in `.cursorrules` and `CLAUDE.md`.

## The Problem
Standard autonomous agents often rewrite hundreds of lines of stable, working code to fix a single-line bug. This speculative rewriting breaks unrelated dependencies, blows up token counts, and destroys clean system states ^[raw/articles/tkprof-factory-journey.md].

## The Rule
Agents are strictly forbidden from writing speculative boilerplate code or overwriting entire files. 
- **Locate and Isolate:** Identify the exact line or block of failure.
- **Patch-Only Execution:** Apply targeted find-and-replace edits, keeping surrounding structures pristine.
- **Context Boundaries:** Preserve comments, styles, and other operational boundaries without silent changes.

This guarantees token-frugal edits and long-term codebase stability.

## See Also
- [[dev-qa-loop]] — Error-correction loop driving these surgical diffs
- [[hermes-agent]] — Runtime enforcing these guidelines
