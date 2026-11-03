#!/usr/bin/env bash
# ==============================================================================
# Blast Radius Zero — Automated 1-Click Deployment on Vultr Cloud Compute
# Hackathon: Agent Rush 2026 (Challenge 1: Blast Radius Zero)
# ==============================================================================

set -e

echo "🚀 [1/5] Updating host packages and installing Docker on Vultr Cloud Compute..."
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Install Docker Engine if not present
if ! command -v docker &> /dev/null; then
    echo "📦 Installing Docker engine..."
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update -y
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo systemctl enable docker
    sudo systemctl start docker
fi

echo "🛡️ [2/5] Building minimal throwaway sandbox container image..."
sudo docker build -t blast-radius-sandbox:latest -f sandbox_image/Dockerfile.sandbox .

echo "⚙️ [3/5] Setting up environment and permissions..."
mkdir -p /tmp/blast_radius_sandboxes
chmod 777 /tmp/blast_radius_sandboxes

if [ ! -f .env ]; then
    echo "Creating .env template..."
    cp .env.example .env
fi

echo "🚢 [4/5] Launching Blast Radius Zero orchestrator and web app..."
sudo docker compose down || true
sudo docker compose up -d --build

PUBLIC_IP=$(curl -s https://api.ipify.org || echo "YOUR_VULTR_VM_IP")

echo "=============================================================================="
echo "✅ DEPLOYMENT COMPLETE!"
echo "🌐 Public Web App URL: http://${PUBLIC_IP}"
echo "🔒 Sandbox Containment: blast-radius-sandbox:latest (Active & Ready)"
echo "📡 Vultr Serverless Inference: https://api.vultrinference.com/v1"
echo "=============================================================================="
