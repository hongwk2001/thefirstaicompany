---
source_url: local_chronicle
ingested: 2026-06-12
sha256: 0d7f3bd33b4027702851a7414f81246eb9fb27e2a42a2caabc80720e6d2544eb
---
# 🧠 The TKPROF AI Agent Factory: Billy learning Multi Agent platform

**Author:** Billy Hong (TKPROF)  
**Date:** June 10, 2026  
**Environment:** Windows 11 Host PC + WSL 2 Subsystem  
**Target Root:** `D:\git_repo\thefirstaicompany`

---

## 🗺️ Architectural Flow

Here is how the control flow operates across boundaries on our daily development stack:

```
[ Windows 11 PC Host (Workstation) ]
       │  (Runs Browser Web Dashboard, Chrome/Edge, VS Code)
       ▼  (Mounts D:\git_repo\thefirstaicompany\ via WSL 2 Network Bridge)
[ WSL 2 Linux Subsystem (Local Sandbox) ]
       ├── Ollama Engine (Runs local Qwen / Llama LLMs offline)
       ├── Project Directory (Local repository and transaction ledger)
       └── Hermes Agent Runtime (Orchestrator making decisions)
              │
              ├─[External API]───► Google Gemini API (High-reasoning, billed strictly under project quota)
              ├─[External API]───► Telegram Bot API (Receiving manual trigger controls)
              └─[External App]───► Telegram Client App (Your mobile cockpit surface)
```


## 🛠️ The Four Design Pillars of the Factory

### 1. Surgical Diffs (`CLAUDE.md`)
Instead of allowing developer agents to rewrite whole files, we enforce **Diff-Surgical Edits** in our core operational instructions. 
* **The Rule:** Developer agents are strictly prohibited from writing speculative or boilerplate code.
* **The Enforcement:** If a file has an error, agents are instructed to locate the precise line of failure, modify only the functional code, and leave the surrounding system pristine. This protects context boundaries and prevents code rot.

### 2. File-Backed Mailbox Architecture (`.swarm/mailboxes/`)
Instead of introducing complex, heavy databases or message brokers (like RabbitMQ or Redis) which make local setups difficult to maintain, we treat the **filesystem as our database**.
* We initialized local transaction mailboxes on the WSL 2 filesystem:
  * `.swarm/mailboxes/developer/inbox/`
  * `.swarm/mailboxes/developer/processed/`
  * `.swarm/mailboxes/qa/inbox/`
  * `.swarm/mailboxes/promoter/inbox/`
* Agents communicate asynchronously by placing standard JSON payloads inside each other's mailboxes. An active daemon (`agent_daemon.js`) monitors these directories and triggers tasks when new files arrive.

### 3. The `/grill-me` Assisted Triage Cockpit (`triage_cockpit.js`)
We refuse to run autonomous models without manual oversight. The **Assisted Triage Cockpit** is a strict, synchronous gate.
* When a high-impact operation (like a production write, deployment, or financial transaction) is requested, the system halts.
* It displays a high-visibility terminal block showing the pending action, its target impact, and the transaction metadata.
* It locks the console until the human developer explicitly types **`APPROVE`** or **`DENY`**.

```
======================================================================
🛑 ASSIGNED ASSISTED TRIAGE COCKPIT - PENDING CLEARANCE
======================================================================

👉 ACTION: deploy_core_sandbox
👉 IMPACT: Modify local configuration stack and master roadmap

⚠️  CRITICAL: This operation requires explicit manual clearance.
Any mutation or deployment is frozen until approved.

📝 Enter "APPROVE" to clear this action, or "DENY" to reject:
```

### 4. Automated Error Interception Loops (`test_runner.js`)
Rather than relying on the developer to manually copy-paste terminal compiler failures back into the AI's chat window, we built a **Self-Correcting QA Runner**.
* The runner executes tests or build commands via `child_process.spawn()`.
* If a process fails (exit code !== 0), the runner intercepts the failure, captures the precise `stdout` and `stderr` streams, and formats it into a typed **`EXECUTION_FAILURE`** JSON schema.
* It automatically drops this JSON file straight into the developer agent’s inbox directory. The developer daemon instantly picks it up, analyzes the error trace, applies a surgical fix, and re-triggers the test until it passes.

---

## 🧪 Simulation Walkthrough: The Dev-QA Loop

To test this framework, we built an automated validation script (`.swarm/run_dev_qa_demo.sh`):

1. **Bug Insertion:** A junior developer script writes a buggy module (`calculator.js` with a missing check for division-by-zero) and a testing script (`test.js`).
2. **QA Run:** The system triggers `node .swarm/test_runner.js node test.js`.
3. **Failure Intercepted:** The division-by-zero returns `Infinity`, causing the unit test to fail. `test_runner.js` catches the failure and generates a typed error JSON file:
   ```json
   {
     "type": "EXECUTION_FAILURE",
     "timestamp": "2026-06-10T...",
     "command": "node test.js",
     "exitCode": 1,
     "summary": "FAIL: Division by zero returned Infinity instead of throwing!",
     "stdout": "Running unit tests...\n",
     "stderr": "FAIL: Division by zero returned Infinity instead of throwing!"
   }
   ```
4. **Developer Inboxed:** This JSON is written directly to `.swarm/mailboxes/developer/inbox/error_17585.json`.
5. **Self-Correction:** The developer agent reads the error report, modifies only the failing `divide()` function to throw an explicit error on zero division, writes the surgical fix, and updates the test file.
6. **Verification:** The test runner runs again, passes with code 0, and logs the milestone successfully.

---

## 🚀 The Path Forward
The TKPROF Agent Factory is successfully running its infrastructure setup and event-driven ledger. Future steps include:
* **Docker Isolation Practice:** Migrating test execution completely inside lightweight, isolated Docker containers to prevent any raw filesystem access during untrusted QA runs.
* **Auto-Publishing Integration:** Enabling Promoter agents to automatically pull completed milestones from `.swarm/progress.md`, format them, and publish them as draft blogs on Jigsawpuzzle Helper, GitHub, or Medium.
