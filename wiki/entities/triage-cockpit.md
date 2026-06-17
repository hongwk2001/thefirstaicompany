---
title: Assisted Triage Cockpit
created: 2026-06-12
updated: 2026-06-12
type: entity
tags: [human-in-the-loop, swarm]
sources: [raw/articles/tkprof-factory-journey.md]
confidence: high
---
# Assisted Triage Cockpit

The Assisted Triage Cockpit (`triage_cockpit.js` / `approve_gate.js`) represents the strict, manual clearance gate that locks down the autonomous swarm.

## Mechanisms of Control
Instead of letting LLMs execute mutations blindly, the Triage Cockpit acts as a synchronous firewall:
1. **Mutation Freeze:** When high-impact tasks (production write, file deletion, server deployment) are triggered, the daemon halts execution.
2. **Metadata Output:** Prints a high-visibility terminal block showing the pending action, its target impact, and JSON schema metadata ^[raw/articles/tkprof-factory-journey.md].
3. **STDIN Lock:** Freezes the terminal or Telegram communication channel, requiring the human developer to explicitly type **`APPROVE`** or **`DENY`** before a transaction clearance is granted.

```
======================================================================
🛑 ASSIGNED ASSISTED TRIAGE COCKPIT - PENDING CLEARANCE
======================================================================
```

## See Also
- [[telegram-bot-gateway]] — Communication path for approvals
- [[mailbox-architecture]] — File-backed state machine holding messages
