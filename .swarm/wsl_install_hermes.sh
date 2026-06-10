#!/usr/bin/env bash
# Official NousResearch Hermes Agent Installer wrapper for WSL

echo "📥 Fetching and running official Hermes Agent installation script..."
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

echo "Checking installation path..."
if [ -f "$HOME/.local/bin/hermes" ] || command -v hermes >/dev/null 2>&1; then
    echo "✅ Hermes Agent successfully installed!"
else
    echo "⚠️ Installation script finished, please verify if 'hermes' command works."
fi
