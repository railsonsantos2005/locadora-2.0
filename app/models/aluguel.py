from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class AluguelModel(Base):
    __tablename__ = "alugueis"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id")
    )

    carro_id = Column(
        Integer,
        ForeignKey("carros.id")
    )

    dias = Column(Integer)