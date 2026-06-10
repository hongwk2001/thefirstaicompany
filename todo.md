# 📋 Hermes Swarm Project TODOs

This file tracks active learning and setup tasks for your Hermes Agent workspace.

## 🏁 Today's Objectives

### 1. Telegram Bot Gateway Setup
- [ ] Check Bot Token created yesterday via Telegram `@BotFather`
- [ ] Add `TELEGRAM_BOT_TOKEN` to `~/.hermes/.env`
- [ ] Retrieve your numeric Telegram user ID using `@userinfobot`
- [ ] Configure `allowed_chats` in `~/.hermes/config.yaml` to secure the bot
- [ ] Run `hermes gateway start` and verify messages are received

### 2. Retrospective Documentation (Install to Validation)
- [ ] Create a static HTML summary of the setup process (Windows 11 ➡️ WSL 2 ➡️ Node/Ollama ➡️ Hermes Agent ➡️ Gemini/Local Qwen configuration)
- [ ] Save draft for publishing on Medium / Jigsawpuzzle Helper

### 3. Familiarizing with Hermes Core Features
- [ ] Explore session recovery using the TUI and CLI (`hermes -c` / `hermes sessions list`)
- [ ] Inspect how tools are dynamically loaded and registered

### 4. Educational Content Creation Pipeline Use Case
- [ ] Design an agent pipeline blueprint to ingest documents/web pages and auto-generate educational study sheets, summaries, and revision cards

### 5. Docker Integration and Source Code Deep-Dive
- [ ] Locate the source code pieces inside `/home/hongw/.hermes/hermes-agent` showing how the Docker container backend spawns and runs commands
- [ ] Practice running commands within the isolated Docker sandbox environment
