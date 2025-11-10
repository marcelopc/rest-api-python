from fastapi import APIRouter, Depends, HTTPException, Response
from core.orders import get_orders, createOrder
from dependencies import create_session
from exceptions import AppException
from schemas.order import OrderSchema
from sqlalchemy.orm import Session
from middleware.auth import ValidateToken

PREFIX = '/orders'
orderRouter = APIRouter(prefix=PREFIX, tags=['Orders'], dependencies=[Depends(ValidateToken)])


@orderRouter.get('/')
async def route_get_orders():
    try:
        return await get_orders()
    except Exception as e:
        return {'message': 'Erro interno', 'error': str(e)}    

@orderRouter.post('/order')
async def orderCreate(order:OrderSchema, response: Response, session:Session=Depends(create_session)):
    try:
        output = await createOrder(order.usuario_id, session)
        response.status_code = output['status_code']
        return output
    except AppException as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro interno: {str(e)}')

@orderRouter.post('/{pedido_id}/cancelar')
async def orderCreate(pedido_id, session:Session=Depends(create_session)):
    try:

        return 'cancelar'
    except AppException as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro interno: {str(e)}')