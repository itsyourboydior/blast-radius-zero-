Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.Rate = 0
$synth.Volume = 100

# Choose English voice if available
$voices = $synth.GetInstalledVoices()
foreach ($v in $voices) {
    if ($v.VoiceInfo.Culture.Name -like "en*") {
        $synth.SelectVoice($v.VoiceInfo.Name)
        break
    }
}

$outputPath = "C:\Users\Besitzer\.gemini\antigravity\scratch\blast-radius-zero\video\voiceover.wav"
$synth.SetOutputToWaveFile($outputPath)

$scriptText = @"
Welcome to Blast Radius Zero.
The autonomous data analytics platform engineered for safe execution on Vultr Cloud Compute.

Large language models excel at writing complex data analysis pipelines.
However, running untrusted, AI-generated Python code on production servers introduces catastrophic security vulnerabilities.
Without containment, malicious or hallucinated code can exfiltrate sensitive datasets through network sockets, steal host environment API keys, corrupt local file systems, or trigger infinite loops that starve CPU compute.

Blast Radius Zero eliminates this danger with zero-trust architectural isolation.
Powered by Vultr Cloud Compute and Vultr Serverless Inference, every query executes inside an ephemeral, throwaway Docker sandbox.
Our security model enforces four non-negotiable containment pillars:
First: Zero network egress. The container operates under network none, completely isolating it from the public internet.
Second: Complete secret hygiene. Host environment variables and cloud credentials are scrubbed, ensuring zero secrets exist in the sandbox.
Third: Read-only data mounting. Source datasets are mounted strictly as read-only, preventing unauthorized modifications or ransomware encryption.
Fourth: Hardware resource caps. Memory is capped at 256 megabytes and CPU execution is strictly monitored by an autonomous watchdog.

When an attack or hostile script attempts unauthorized access, the sandbox neutralizes the threat instantly.
The blast radius is strictly zero.
Meanwhile, verified analytical results, statistical summaries, and high-resolution charts are safely harvested and explained by Vultr Serverless Inference.
If an error occurs, an autonomous self-healing loop automatically repairs the code and re-executes.

Blast Radius Zero. Turning autonomous AI agents into safe, enterprise-grade production software on Vultr Cloud Compute.
"@

$synth.Speak($scriptText)
$synth.Dispose()
Write-Host "Audio generated successfully at $outputPath"
