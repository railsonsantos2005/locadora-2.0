from fastapi import FastAPI

from app.core.database import Base, engine

from app.models.cliente import ClienteModel
from app.models.carro import CarroModel
from app.models.aluguel import AluguelModel

from app.routers import clientes, carros, alugueis

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Locadora")

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

app.include_router(clientes.router)
app.include_router(carros.router)
app.include_router(alugueis.router)