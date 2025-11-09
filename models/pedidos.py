from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base
from sqlalchemy_utils.types import ChoiceType

class Pedido(Base):
    __tablename__ = 'pedidos'

    # STATUS_PEDIDOS = (
    #     ('pendente', 'Pendente'),
    #     ('processando', 'Processando'),
    #     ('enviado', 'Enviado'),
    #     ('entregue', 'Entregue'),
    #     ('cancelado', 'Cancelado'),
    # )

    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column('usuario_id', ForeignKey('usuarios.id'), index=True)
    preco = Column('preco', Integer, index=True)
    status = Column('status',String, default='pendente')

    def __init__(self, usuario_id: int, preco: int = 0, status: str = 'pendente'):
        self.usuario_id = usuario_id
        self.preco = preco
        self.status = status