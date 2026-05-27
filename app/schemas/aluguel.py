
from pydantic import BaseModel

class Aluguel(BaseModel):
    cliente_id: int
    carro_id: int
    dias: int

    class Config:
        from_attributes = True
