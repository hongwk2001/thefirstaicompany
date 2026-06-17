---
title: Telegram Bot Gateway
created: 2026-06-12
updated: 2026-06-12
type: entity
tags: [runtime, security]
sources: [raw/transcripts/hermes-setup-chronicle.md]
confidence: high
---
# Telegram Bot Gateway

The Telegram Bot Gateway is the secure communication telemetry bridge connecting local WSL 2 processing loops to the developer's mobile device.

## System Security & Lockdown
- **Config-Level Guardrails:** Configured inside `~/.hermes/config.yaml` to mandate absolute user lockout.
- **User ID Lockdown:** Restricts execution strictly to Billy Hong's authenticated user ID, preventing any external prompt injections or unauthorized command executions on the underlying host.
- **Telemetry Streams:** Employs persistent WebSockets/Webhooks to beam live compiler logs, Build-In-Public multimedia artifacts (rendered dashboard PNGs, raw HTML documents), and triage approvals back to the Telegram client app ^[raw/transcripts/hermes-setup-chronicle.md].

## See Also
- [[hermes-agent]] — Primary execution runtime
- [[triage-cockpit]] — Human clearance mechanism operated via Telegram
