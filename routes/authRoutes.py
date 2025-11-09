from fastapi import APIRouter
from controllers.user import createAccount

PREFIX = '/auth'
authRouter = APIRouter(prefix=PREFIX, tags=['Authentication'])

@authRouter.get('/')
async def auth():
    try:
        return {'message':'Você acessou a rota padrão de autenticação', 'auth': False}
    except Exception as e:
        return {'message': 'Erro interno', 'error': str(e)}    
    
