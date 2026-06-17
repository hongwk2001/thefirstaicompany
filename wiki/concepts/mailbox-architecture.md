---
title: Mailbox Architecture
created: 2026-06-12
updated: 2026-06-12
type: concept
tags: [swarm]
sources: [raw/articles/tkprof-factory-journey.md]
confidence: high
---
# File-Backed Mailbox Architecture

The File-Backed Mailbox Architecture represents the core asynchronous communication grid of the TKPROF AI Agent Factory, treating the local filesystem as a transaction ledger.

## Core Design
To avoid heavy, high-maintenance database services or message brokers (like Redis, PostgreSQL, or RabbitMQ) in a localized sandbox, the system organizes transaction queues strictly as standard file directories on the WSL 2 disk ^[raw/articles/tkprof-factory-journey.md]:
- `.swarm/mailboxes/developer/inbox/`
- `.swarm/mailboxes/developer/processed/`
- `.swarm/mailboxes/qa/inbox/`
- `.swarm/mailboxes/promoter/inbox/`

## Messaging Sequence
1. **Task Delivery:** An agent dumps a standardized JSON payload detailing the goal, parameters, and task ID directly into another agent's `/inbox/`.
2. **Daemon Monitoring:** A persistent lightweight background daemon (`agent_daemon.js` or `orchestrator.py`) monitors mailbox paths via directory polling.
3. **Processing & Handoff:** Once detected, the target agent executes the task, archives the input file into `/processed/`, writes its output payload to the next inbox, and continues the cycle.

This ensures **100% auditable history**, instant restarts on failure, and complete data safety.

## See Also
- [[triage-cockpit]] — Clearances integrated within mailboxes
- [[dev-qa-loop]] — Automated testing pipelines leveraging mailboxes
