---
title: Automated Dev-QA Loop
created: 2026-06-12
updated: 2026-06-12
type: concept
tags: [dev-qa, swarm]
sources: [raw/articles/tkprof-factory-journey.md]
confidence: high
---
# Automated Dev-QA Loop

The Automated Dev-QA Loop represents the self-correcting error interception pipeline that automates software debugging without manual copy-paste cycles.

## Error Interception Mechanics
When a developer agent writes code, the system doesn't rely on the user to run tests. It orchestrates a programmatic verification circle ^[raw/articles/tkprof-factory-journey.md]:
1. **Compilation Trigger:** The QA agent launches the testing suite (`test_runner.js`) via `child_process.spawn()`.
2. **Interception:** If the execution fails (exit code !== 0), the runner captures the raw `stdout` and `stderr` error traces.
3. **Payload Generation:** It packages this trace into a structured JSON payload of type `EXECUTION_FAILURE` and drops it straight into the developer's mailbox `/inbox/`.
4. **Autonomous Self-Healing:** The developer picks up the failure trace, parses the error line, applies a surgical patch in `[[surgical-diffs]]`, and re-submits to the test runner. The loop iterates autonomously until tests pass cleanly.

## See Also
- [[mailbox-architecture]] — Filesystem queue driving the loop
- [[surgical-diffs]] — Code preservation rules for patches
