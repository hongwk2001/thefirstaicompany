# 📋 Hermes Swarm Project TODOs

This file tracks active learning and setup tasks for your Hermes Agent workspace.

## 🏁 Today's Objectives

### 1. Telegram Bot Gateway Setup
- [x] Check Bot Token created yesterday via Telegram `@BotFather`
- [x] Add `TELEGRAM_BOT_TOKEN` to `~/.hermes/.env`
- [x] Retrieve your numeric Telegram user ID using `@userinfobot`
- [x] Configure `allowed_chats` in `~/.hermes/config.yaml` to secure the bot
- [x] Run `hermes gateway start` and verify messages are received

### 2. Retrospective Documentation (Install to Validation)
- [x] Create a static HTML summary of the setup process (Windows 11 ➡️ WSL 2 ➡️ Node/Ollama ➡️ Hermes Agent ➡️ Gemini/Local Qwen configuration)
- [x] Save draft for publishing on Medium / Jigsawpuzzle Helper (Draft saved at `TKPROF_AGENT_FACTORY_JOURNEY.md`)
- [x] Create roadmap under documentation (Strategic roadmap saved at `roadmap.md` and linked in retro summary HTML)
- [x] Refine and deploy `CLAUDE.md` and `.cursorrules` ruleset to enforce high-retention "No Man Company" AI development principles (surgical edits, triage cockpit gate, and error-intercept loops)

### 3. Familiarizing with Hermes Core Features
- [ ] Explore session recovery using the TUI and CLI (`hermes -c` / `hermes sessions list`)
- [ ] Inspect how tools are dynamically loaded and registered

### 4. Educational Content Creation Pipeline Use Case
- [ ] Design an agent pipeline blueprint to ingest documents/web pages and auto-generate educational study sheets, summaries, and revision cards

### 5. Docker Integration and Source Code Deep-Dive
- [x] Locate the source code pieces inside `/home/hongw/.hermes/hermes-agent` showing how the Docker container backend spawns and runs commands
- [ ] Practice running commands within the isolated Docker sandbox environment
