from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.motorista_schema import MotoristaCreate, MotoristaOut
from app.services import motorista_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MotoristaOut)
def criar_motorista(motorista: MotoristaCreate, db: Session = Depends(get_db)):
    return motorista_service.criar_motorista(db, motorista)

@router.get("/", response_model=list[MotoristaOut])
def listar_motoristas(db: Session = Depends(get_db)):
    return motorista_service.listar_motoristas(db)

@router.get("/{motorista_id}", response_model=MotoristaOut)
def obter_motorista(motorista_id: int, db: Session = Depends(get_db)):
    motorista = motorista_service.buscar_motorista_por_id(db, motorista_id)
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return motorista

@router.put("/{motorista_id}", response_model=MotoristaOut)
def atualizar_motorista(motorista_id: int, motorista: MotoristaCreate, db: Session = Depends(get_db)):
    motorista_atualizado = motorista_service.atualizar_motorista(db, motorista_id, motorista)
    if not motorista_atualizado:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return motorista_atualizado

@router.delete("/{motorista_id}")
def deletar_motorista(motorista_id: int, db: Session = Depends(get_db)):
    motorista_deletado = motorista_service.deletar_motorista(db, motorista_id)
    if not motorista_deletado:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return {"detail": "Motorista deletado com sucesso"}
