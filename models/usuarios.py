from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column('nome', String, unique=True, index=True)
    email = Column('email', String, unique=True, index=True, nullable=False)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean, default=True)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, nome: str, email: str, senha: str, ativo: bool = True, admin: bool = False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
