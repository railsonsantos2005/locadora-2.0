
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.cliente import Cliente
from app.models.cliente import ClienteModel
from app.core.database import SessionLocal

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(ClienteModel).all()

@router.post("/")
def criar(cliente: Cliente, db: Session = Depends(get_db)):

    novo_cliente = ClienteModel(
        nome=cliente.nome,
        cpf=cliente.cpf,
        telefone=cliente.telefone
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente

@router.put("/{id}")
def atualizar(id: int, cliente: Cliente, db: Session = Depends(get_db)):

    cliente_db = db.query(ClienteModel).filter(ClienteModel.id == id).first()

    if not cliente_db:
        return {"erro": "Cliente não encontrado"}

    cliente_db.nome = cliente.nome
    cliente_db.cpf = cliente.cpf
    cliente_db.telefone = cliente.telefone

    db.commit()

    return {"mensagem": "Cliente atualizado"}

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):

    cliente_db = db.query(ClienteModel).filter(ClienteModel.id == id).first()

    if not cliente_db:
        return {"erro": "Cliente não encontrado"}

    db.delete(cliente_db)
    db.commit()

    return {"mensagem": "Cliente removido"}
