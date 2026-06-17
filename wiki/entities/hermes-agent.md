---
title: Hermes Agent
created: 2026-06-12
updated: 2026-06-12
type: entity
tags: [runtime, security]
sources: [raw/transcripts/hermes-setup-chronicle.md]
confidence: high
---
# Hermes Agent

Hermes Agent is the core, high-reasoning runtime and orchestrator that acts as the primary decision engine for the TKPROF factory.

## Environment & Role
- **WSL 2 Runtime:** Hermes runs inside the WSL 2 Linux subsystem, executing local scripts, performing git transactions, and managing files on the mounted shared directory `/mnt/d/git_repo/thefirstaicompany` [[ollama-wsl2]].
- **Secured Communications:** Integrates directly with the user's mobile device via the [[telegram-bot-gateway]] bridge, sending high-fidelity progress updates, images, and HTML artifacts while responding to on-the-fly commands ^[raw/transcripts/hermes-setup-chronicle.md].

## Integration inside the Swarm
- Operates as the central mind that interfaces with local developer, QA, and Promoter agents by checking file transaction queues in the [[mailbox-architecture]].

## See Also
- [[ollama-wsl2]] — Local model engine supporting Hermes
- [[telegram-bot-gateway]] — Direct secure communication gate
- [[mailbox-architecture]] — Decentralized messaging queue
