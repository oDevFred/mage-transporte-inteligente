from fastapi import FastAPI
from app.api.v1 import onibus

app = FastAPI(
    title="Mage Transporte Inteligente",
    version="1.0.0"
)

app.include_router(onibus.router, prefix="/api/v1/onibus")