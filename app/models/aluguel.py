
from sqlalchemy import Column, Integer
from app.core.database import Base

class AluguelModel(Base):
    __tablename__ = "alugueis"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    carro_id = Column(Integer)
    dias = Column(Integer)
