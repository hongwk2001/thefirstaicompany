---
source_url: local_setup_telemetry
ingested: 2026-06-12
sha256: 87d901f68dbaf712ad04b1fef37fa73833175ababe3e1f1009b3d38ee8026c63
---
# Hermes Setup Chronicle
Detailed timeline and setup steps for Billy Hong's (TKPROF) developer workstation, bridging local development and Telegram BOT gateway communications.

### Timeline & Components:
1. **Operating System Environment:**
   - Host: Windows 11 PC workstation.
   - Local Sandbox: Windows Subsystem for Linux (WSL 2) running Ubuntu Linux.
   - Access Bridge: Host filesystems are mounted under WSL `/mnt/d/git_repo/thefirstaicompany` allowing seamless editing from Windows IDEs (VS Code/Cursor) while executing code inside WSL.

2. **Local Model Infrastructure (Ollama):**
   - Goal: Minimize cloud API dependency, token leaks, and internet latency.
   - Implementation: Installed Ollama service locally inside WSL 2 (`.swarm/wsl_install_ollama.sh`).
   - Active Models: Offline models like Qwen-2.5-Coder and Llama 3 running locally on WSL for standard coding tasks, leveraging high speed and zero usage cost.

3. **Hermes Bot Gateway Integration:**
   - Goal: Bring high-security mobile telemetry control and chat interface directly to Telegram.
   - Configuration: Written under `~/.hermes/config.yaml` with rigorous user lockouts.
   - Webhook & WebSocket Bridge: Initiated `hermes gateway` daemon to feed telemetry logs and command queues between local WSL execution loops and Telegram client channels.
