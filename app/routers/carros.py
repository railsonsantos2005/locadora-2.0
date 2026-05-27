
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.carro import Carro
from app.models.carro import CarroModel
from app.core.database import SessionLocal

router = APIRouter(
    prefix="/carros",
    tags=["Carros"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(CarroModel).all()

@router.post("/")
def criar(carro: Carro, db: Session = Depends(get_db)):

    novo_carro = CarroModel(
        modelo=carro.modelo,
        placa=carro.placa,
        disponivel=carro.disponivel
    )

    db.add(novo_carro)
    db.commit()
    db.refresh(novo_carro)

    return novo_carro

@router.put("/{id}")
def atualizar(id: int, carro: Carro, db: Session = Depends(get_db)):

    carro_db = db.query(CarroModel).filter(CarroModel.id == id).first()

    if not carro_db:
        return {"erro": "Carro não encontrado"}

    carro_db.modelo = carro.modelo
    carro_db.placa = carro.placa
    carro_db.disponivel = carro.disponivel

    db.commit()

    return {"mensagem": "Carro atualizado"}

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):

    carro_db = db.query(CarroModel).filter(CarroModel.id == id).first()

    if not carro_db:
        return {"erro": "Carro não encontrado"}

    db.delete(carro_db)
    db.commit()

    return {"mensagem": "Carro removido"}
