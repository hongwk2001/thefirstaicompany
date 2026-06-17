---
title: Ollama on WSL 2
created: 2026-06-12
updated: 2026-06-12
type: entity
tags: [local-llm, runtime]
sources: [raw/transcripts/hermes-setup-chronicle.md]
confidence: high
---
# Ollama on WSL 2

Ollama is a lightweight local LLM execution engine running directly within the WSL 2 subsystem.

## Strategic Purpose
To achieve extreme token frugality and 100% offline security, the TKPROF AI Agent Factory relies on Ollama for repetitive coding and validation tasks. This avoids wasting expensive external Gemini or OpenAI tokens on intermediate development cycles ^[raw/transcripts/hermes-setup-chronicle.md].

## Configured Models
- **Qwen-2.5-Coder:** Used as the local "muscle" for developer agents. Fast, highly focused on code syntax, and optimized for offline file generation.
- **Llama 3:** Employed for general parsing and log structuring.

## Synergy with Hermes
[[hermes-agent]] monitors local setup readiness by verifying Ollama's active models (e.g. executing `ollama ps` and checks) before running automated multi-agent tasks, guaranteeing a reliable execution pipeline.

## See Also
- [[hermes-agent]] — The core high-reasoning orchestrator
- [[mailbox-architecture]] — The communication grid for offline agents
