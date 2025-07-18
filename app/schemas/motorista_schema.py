from pydantic import BaseModel, EmailStr

class MotoristaBase(BaseModel):
    nome: str
    email: EmailStr

class MotoristaCreate(MotoristaBase):
    senha: str  # Para criação

class MotoristaOut(MotoristaBase):
    id: int

    class Config:
        orm_mode = True
