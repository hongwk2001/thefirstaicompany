---
title: Agent Coordination Models
created: 2026-06-12
updated: 2026-06-12
type: comparison
tags: [swarm, strategy]
sources: [raw/articles/tkprof-factory-journey.md]
confidence: high
---
# Multi-Agent Coordination Models

A strategic comparison of multi-agent messaging patterns inside local development sandboxes.

| Dimension | File-Backed Mailbox (TKPROF Pattern) | Database-Driven Queues (PostgreSQL/Redis) | Heavy Brokers (RabbitMQ/Kafka) |
|---|---|---|---|
| **Dependencies** | None (Local Filesystem) | High (Requires active DB servers) | Extreme (Requires JVM / message brokers) |
| **Auditability** | Perfect (Standard JSON files on disk) | Medium (Requires database queries) | Hard (Requires specialized visualizers) |
| **Recovery** | Instant (Reposition file in `/inbox`) | Complex (Manual row mutations) | Complex (Re-queuing and ACK-logic) |
| **Setup Cost** | Zero (Standard directory layout) | Medium (Docker-compose config) | High (Port configurations & cluster setup) |
| **Speed (WSL 2)** | Extreme (Native Linux RAM caching) | High (Network latency overhead) | High (Network protocol overhead) |

## Strategic Synthesis
For localized, high-frugality development sandboxes like the TKPROF AI Agent Factory, **File-Backed Mailboxes** ([[mailbox-architecture]]) are the superior coordination model. They provide complete transparency, zero external service dependency, perfect git audit trails, and extreme speed on local WSL filesystem mounts ^[raw/articles/tkprof-factory-journey.md].

## See Also
- [[mailbox-architecture]] — Core implementation detail
- [[dev-qa-loop]] — Workflow utilizing this comparison model
