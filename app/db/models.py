from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Motorista(Base):
    __tablename__ = "motoristas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    senha = Column(String, nullable=False)

    onibus = relationship("Onibus", back_populates="motorista")


class Onibus(Base):
    __tablename__ = "onibus"
    
    id = Column(Integer, primary_key=True, index=True)
    linha = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    motorista_id = Column(Integer, ForeignKey("motoristas.id"))

    motorista = relationship("Motorista", back_populates="onibus")
