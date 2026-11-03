# 🎬 Demo Video Script & Walkthrough (2-3 Minutes)
### Hackathon: Agent Rush 2026 — Challenge 1: Blast Radius Zero

---

## 🕒 Timing & Scene Breakdown

### Scene 1: The Problem & The Solution (0:00 - 0:35)
- **Visual**: Show the Blast Radius Zero Dashboard with the glowing containment badges (NET: NONE, SECRETS: 0, CAP: 256MB).
- **Narration**:  
  *"Welcome to Blast Radius Zero. Autonomous AI coding agents are incredibly powerful, but running untrusted AI code on production servers is dangerous. A single malicious or hallucinated script can steal API keys, corrupt files, or hijack compute resources.*  
  *Blast Radius Zero solves this. Powered by Vultr Cloud Compute and Vultr Serverless Inference, it executes untrusted data analytics code inside an ephemeral, hardened Docker sandbox with zero network egress, zero secrets exposed, and read-only data isolation."*

---

### Scene 2: Real Work with Receipts (CSV Analyst) (0:35 - 1:25)
- **Visual**:  
  1. Select the `Vultr Cloud Compute Metrics` dataset.
  2. Click the suggestion: *"Compare avg CPU & memory utilization across Vultr regions and highlight instances with >80% load."*
  3. Click **"Execute in Isolated Sandbox"**.
  4. Watch the pipeline tracker turn cyan and emerald in real-time.
- **Narration**:  
  *"Notice what happens under the hood. The orchestrator inspects the CSV schema, contacts Vultr Serverless Inference at `api.vultrinference.com`, and receives Python code.*  
  *It spins up a throwaway container with no network access and memory capped at 256MB. Look at the output: real calculated tables, instance loads, and high-resolution charts rendered by Matplotlib. Every single finding has deterministic receipts in standard output, fully explained by the model."*

---

### Scene 3: The Critical "Containment Moment" (1:25 - 2:15)
- **Visual**:  
  1. Click the **"Containment Test"** tab.
  2. Click **"1. Network Exfiltration Attack"** or **"2. Secret Environment Exfiltration"**.
  3. Open the terminal stdout tab to show the error caught and neutralized by the sandbox.
- **Narration**:  
  *"Now for our containment moment. What happens if a malicious prompt or compromised model attempts to exfiltrate data or steal host API keys?*  
  *Let's simulate a hostile attack directly. Here, the injected script tries to connect to an external server and scan environment variables for Vultr API keys.*  
  *Boom! The Docker sandbox stops it dead in its tracks. Docker's `--network none` flag completely denies socket egress, and our strict zero-secrets policy means no API keys or host credentials exist in the container environment. The threat is completely neutralized. The blast radius is strictly ZERO."*

---

### Scene 4: Architecture on Vultr & Closing (2:15 - 2:45)
- **Visual**:  
  1. Switch to the **"Vultr Arch"** tab.
  2. Highlight the Vultr VM host and Serverless Inference architecture.
- **Narration**:  
  *"Blast Radius Zero runs entirely on Vultr infrastructure: hosted on a Vultr Cloud Compute VM, powered by Vultr Serverless Inference, and secured by container isolation. It turns AI agents from risky chatbot demos into hardened, enterprise-grade products.*  
  *Check out our live public URL and public GitHub repository linked in the submission. Thank you!"*
