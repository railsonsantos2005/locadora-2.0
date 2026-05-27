
from pydantic import BaseModel

class Carro(BaseModel):
    modelo: str
    placa: str
    disponivel: bool

    class Config:
        from_attributes = True
