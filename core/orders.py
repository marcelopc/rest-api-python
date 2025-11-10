from sqlalchemy.orm import Session
from models import Pedido
from models import Usuario
from exceptions import AppException

async def get_orders():
    return { 'message': 'Você acessou a rota de pedidos'}

async def createOrder(usuario:int, session:Session):
    usuario = session.query(Usuario).filter(Usuario.id == usuario).first()

    if not usuario:
        raise AppException('usuário não encontrado', 404 )
    
    order = Pedido(usuario)
    session.add(order)
    session.commit()
    return {'message': 'Pedido criado com sucesso', 'status_code':201}