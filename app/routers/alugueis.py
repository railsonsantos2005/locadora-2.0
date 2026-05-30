from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.aluguel import Aluguel
from app.models.aluguel import AluguelModel
from app.core.database import get_db

router = APIRouter(
    prefix="/alugueis",
    tags=["Aluguéis"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(AluguelModel).all()

@router.post("/")
def criar(aluguel: Aluguel, db: Session = Depends(get_db)):

    novo_aluguel = AluguelModel(
        cliente_id=aluguel.cliente_id,
        carro_id=aluguel.carro_id,
        dias=aluguel.dias
    )

    db.add(novo_aluguel)
    db.commit()
    db.refresh(novo_aluguel)

    return novo_aluguel
