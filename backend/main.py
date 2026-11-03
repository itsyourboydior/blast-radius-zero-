"""
Blast Radius Zero - FastAPI Server & Vultr Cloud Backend.
"""
import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from backend.sample_data import seed_sample_data
from backend.sandbox import SandboxExecutor, is_docker_available
from backend.llm_client import LLMClient
from backend.orchestrator import Orchestrator, ATTACK_PAYLOADS

app = FastAPI(
    title="Blast Radius Zero — Sandboxed AI Data Analyst",
    description="Agent Rush Hackathon 2026: Safe, autonomous agent execution on Vultr Cloud Compute.",
    version="1.0.0"
)

# Enable CORS for local dev or separate client builds
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
FRONTEND_DIR = BASE_DIR / "frontend"
SANDBOX_TEMP_DIR = Path(tempfile.gettempdir()) / "blast_radius_sandboxes"

# Seed sample datasets on launch
seed_sample_data(str(BASE_DIR))

# Singletons
sandbox_exec = SandboxExecutor(base_work_dir=str(SANDBOX_TEMP_DIR))
llm_client = LLMClient()
orchestrator = Orchestrator(llm_client=llm_client, sandbox_executor=sandbox_exec)

class AnalyzeRequest(BaseModel):
    dataset_name: str
    query: str
    api_key: Optional[str] = None
    model: Optional[str] = None

class AttackSimRequest(BaseModel):
    vector: str
    dataset_name: Optional[str] = None

@app.get("/api/health")
def health_check():
    docker_status = is_docker_available()
    return {
        "status": "healthy",
        "service": "Blast Radius Zero",
        "vultr_host": "Vultr Cloud Compute (AMD64 / Ubuntu 24.04)",
        "vultr_inference_endpoint": llm_client.base_url,
        "active_model": llm_client.model,
        "docker_available": docker_status,
        "sandbox_isolation_tier": "Docker Container (cgroups/namespaces)" if docker_status else "Subprocess Jail (Scrubbed Zero-Secret Env)"
    }

@app.get("/api/sample-datasets")
def list_sample_datasets():
    datasets = []
    if DATA_DIR.exists():
        for file in DATA_DIR.glob("*.csv"):
            datasets.append({
                "filename": file.name,
                "size_bytes": file.stat().st_size,
                "label": file.stem.replace("_", " ").title()
            })
    return {"datasets": datasets}

@app.post("/api/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    
    dest_path = DATA_DIR / file.filename
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "size_bytes": dest_path.stat().st_size,
        "status": "uploaded"
    }

@app.post("/api/analyze")
def run_analysis(req: AnalyzeRequest):
    data_path = DATA_DIR / req.dataset_name
    if not data_path.exists():
        # Fallback to first available csv
        csv_files = list(DATA_DIR.glob("*.csv"))
        if not csv_files:
            raise HTTPException(status_code=404, detail="No dataset found.")
        data_path = csv_files[0]

    # Dynamically apply client key/model if supplied
    if req.api_key:
        llm_client.set_config(api_key=req.api_key, model=req.model)

    result = orchestrator.process_query(
        data_file_path=str(data_path),
        query=req.query
    )
    return result

@app.get("/api/attack-vectors")
def list_attack_vectors():
    return {
        "vectors": [
            {
                "key": k,
                "title": v["title"],
                "description": v["description"]
            }
            for k, v in ATTACK_PAYLOADS.items()
        ]
    }

@app.post("/api/simulate-attack")
def simulate_attack(req: AttackSimRequest):
    dataset_name = req.dataset_name or "vultr_cloud_compute_metrics.csv"
    data_path = DATA_DIR / dataset_name
    if not data_path.exists():
        csv_files = list(DATA_DIR.glob("*.csv"))
        if csv_files:
            data_path = csv_files[0]
        else:
            raise HTTPException(status_code=404, detail="Dataset not found for attack test.")

    try:
        report = orchestrator.run_attack_simulation(req.vector, str(data_path))
        return report
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.get("/artifacts/{run_id}/{filename}")
def get_artifact(run_id: str, filename: str):
    file_path = SANDBOX_TEMP_DIR / run_id / "output" / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Artifact not found or destroyed.")
    return FileResponse(file_path)

# Serve web frontend
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/")
    def index():
        return FileResponse(FRONTEND_DIR / "index.html")
