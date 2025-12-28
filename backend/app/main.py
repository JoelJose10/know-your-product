from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.qdrant_client import init_collection

app = FastAPI(title="Know Your Product API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_collection()

@app.get("/health")
def health_check():
    return {"status": "ok"}
