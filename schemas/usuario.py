from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    email:str
    senha:str

    class Config:
        from_attributes = True
