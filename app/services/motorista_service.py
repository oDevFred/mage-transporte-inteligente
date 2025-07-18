from sqlalchemy.orm import Session
from app.db import models
from app.schemas.motorista_schema import MotoristaCreate

def criar_motorista(db: Session, motorista: MotoristaCreate):
    novo_motorista = models.Motorista(
        nome=motorista.nome,
        email=motorista.email,
        senha=motorista.senha  # Idealmente a senha seria criptografada (deixamos isso para o JWT)
    )
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista

def listar_motoristas(db: Session):
    return db.query(models.Motorista).all()

def buscar_motorista_por_id(db: Session, motorista_id: int):
    return db.query(models.Motorista).filter(models.Motorista.id == motorista_id).first()

def atualizar_motorista(db: Session, motorista_id: int, motorista: MotoristaCreate):
    motorista_db = buscar_motorista_por_id(db, motorista_id)
    if motorista_db:
        motorista_db.nome = motorista.nome
        motorista_db.email = motorista.email
        motorista_db.senha = motorista.senha
        db.commit()
        db.refresh(motorista_db)
    return motorista_db

def deletar_motorista(db: Session, motorista_id: int):
    motorista_db = buscar_motorista_por_id(db, motorista_id)
    if motorista_db:
        db.delete(motorista_db)
        db.commit()
    return motorista_db
