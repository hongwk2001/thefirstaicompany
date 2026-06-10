#!/usr/bin/env bash
# Script to install Ollama and configure systemd in WSL 2

echo "⚙️  Step 1: Checking systemd configuration in /etc/wsl.conf..."
if grep -q "systemd=true" /etc/wsl.conf 2>/dev/null; then
    echo "✅ systemd is already configured in /etc/wsl.conf."
else
    echo "⚙️  Adding systemd=true to /etc/wsl.conf (requires sudo)..."
    echo -e "[boot]\nsystemd=true" | sudo tee -a /etc/wsl.conf > /dev/null
    echo "⚠️  CRITICAL: systemd was enabled. You MUST restart WSL for this to take effect."
    echo "Please shut down WSL from Windows PowerShell using: wsl --shutdown"
    echo "Then reopen your WSL terminal and run this script again to complete the Ollama installation."
    exit 0
fi

# Ensure zstd is installed (required by Ollama installer)
if ! command -v zstd >/dev/null 2>&1; then
    echo "⚙️  zstd is missing. Installing zstd (requires sudo)..."
    sudo apt-get update && sudo apt-get install -y zstd
fi

echo "⚙️  Step 2: Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo "⚙️  Step 3: Checking Ollama service status..."
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl restart ollama
sudo systemctl status ollama --no-pager

echo "🎉 Ollama installation and setup complete!"
echo "Now you can pull models. Examples:"
echo "  ollama pull qwen2.5-coder:14b"
echo "  ollama pull gemma2:9b"
