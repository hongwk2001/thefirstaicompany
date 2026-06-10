# 🏁 TKPROF AI Project Operational Parameters

## Execution Constraints
- The master design roadmap for this software environment is strictly logged in `roadmap.md`.
- Sub-agents must never alter architectural decisions or context scopes without cross-referencing files in this directory.

## Diff-Surgical Instruction Rules
- **Ban Speculative Re-writes**: Never perform large-scale or speculative re-writes of existing code. All edits must be surgical, precise, and targeted.
- **Trace-Driven Debugging**: Limit code edits to only the specific functional lines that are throwing diagnostic traces, causing test failures, or strictly required by the prompt.
- **Minimal Diff Footprint**: Use small, localized edits to achieve the task. Avoid cosmetic, stylistic, or refactoring-related edits that are unrelated to fixing functionality.
- **Strict Scope Boundaries**: Conversational chat padding, opinion questions, and speculative code shifts are fully restricted. Fix functional execution metrics cleanly using minimal diff edits.

## Triage Cockpit & Read-Only Boundaries
- **Manual Clearance Gate**: Any script, tool execution, or deployment action that performs file mutations or changes external state must run through the clearance cockpit (`node .swarm/triage_cockpit.js <action_name> <impact_summary>`) and obtain `APPROVE` before continuing.
- **Strict Read-Only Default**: Workflows must default to read-only operation. No automated execution is permitted to modify the core host environment or production configurations without explicit cockpit triage approval.