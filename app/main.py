
from fastapi import FastAPI
from app.routers import clientes, carros, alugueis

app = FastAPI(title="Sistema de Locadora")

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

app.include_router(clientes.router)
app.include_router(carros.router)
app.include_router(alugueis.router)
