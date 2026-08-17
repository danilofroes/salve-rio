from fastapi import FastAPI

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