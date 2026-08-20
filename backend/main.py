from fastapi import FastAPI
from backend.database.base import engine
from backend.database import models

models.Base.metadata.create_all(bind=engine) # Transforma os modelos criados em tabelas no Postgres

# Inicialização da FastAPI
app = FastAPI(
    title="API SALVE",
    description="Sistema de Alerta e Vigilância Epidemiológica",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "SALVE",
        "version": "0.1.0"
    }