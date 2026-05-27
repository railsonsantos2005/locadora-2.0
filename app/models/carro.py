
from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class CarroModel(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, nullable=False)
    placa = Column(String, unique=True)
    disponivel = Column(Boolean, default=True)
