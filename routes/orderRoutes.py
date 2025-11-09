from fastapi import APIRouter
from controllers.orders import get_orders

PREFIX = "/order"
orderRouter = APIRouter(prefix=PREFIX, tags=["Orders"])


@orderRouter.get("/")
async def route_get_orders():
    try:
        return await get_orders()
    except Exception as e:
        return {'message': 'Erro interno', 'error': str(e)}    