from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base

class ItemPedido(Base):
    __tablename__ = 'itens_pedido'

    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    quantidade = Column('quantidade', Integer, index=True)
    sabor = Column('sabor', String, index=True)
    tamanho = Column('tamanho', String, index=True)
    preco_unitario = Column('preco_unitario', Integer, index=True)
    pedido_id = Column('pedido_id', ForeignKey('pedidos.id'), index=True)
    ativo = Column('ativo', Boolean, default=True)

    def __init__(self, quantidade: int, sabor: str, tamanho: str, preco_unitario: int, pedido_id: int, ativo: bool = True):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido_id = pedido_id
        self.ativo = ativo