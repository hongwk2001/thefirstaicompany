#!/usr/bin/env bash
# WSL Environment Setup Script for TKPROF AI Agent Factory

echo "⏳ Checking WSL packages..."

# 1. Check Git
if command -v git >/dev/null 2>&1; then
    echo "✅ Git is installed ($(git --version))"
else
    echo "⚠️ Git is missing. Installing..."
    apt-get update && apt-get install -y git
fi

# 2. Check Node.js
if command -v node >/dev/null 2>&1; then
    echo "✅ Node.js is installed ($(node --version))"
else
    echo "⚠️ Node.js is missing. Installing LTS node..."
    apt-get update
    apt-get install -y ca-certificates curl gnupg
    mkdir -p /etc/apt/keyrings
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
    NODE_MAJOR=20
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/etc/sources.list.d/nodesource.list
    apt-get update
    apt-get install nodejs -y
fi

# 3. Check Docker
if command -v docker >/dev/null 2>&1; then
    if docker info >/dev/null 2>&1; then
        echo "✅ Docker is running and integrated with WSL."
    else
        echo "❌ Docker command exists, but daemon is not running or accessible. Ensure Docker Desktop is active."
    fi
else
    echo "❌ Docker integration is missing. Ensure WSL Integration is enabled in Docker Desktop."
fi

echo "🎉 WSL Environment verification complete!"
