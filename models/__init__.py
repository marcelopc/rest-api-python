from sqlalchemy import create_engine
from .base import Base
from .usuarios import Usuario
from .pedidos import Pedido
from .itensPedido import ItemPedido

db = create_engine('sqlite:///banco.db')

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=db)

