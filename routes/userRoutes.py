from fastapi import APIRouter, Depends, HTTPException, Response
from core.user import createAccount
from dependencies import create_session
from utils.crypto import bcrypt_context
from exceptions import AppException
from schemas.usuario import UsuarioSchema
from sqlalchemy.orm import Session

PREFIX = '/user'
userRouter = APIRouter(prefix=PREFIX, tags=['User'])

@userRouter.get('/')
async def user():
    try:
        return {'message':'Você acessou a rota padrão de usuário'}
    except Exception as e:
        return {'message': 'Erro interno', 'error': str(e)}    
    
@userRouter.post('/create')
async def userCreate(usuario:UsuarioSchema, response: Response, session:Session=Depends(create_session)):
    try:
        hashed_password = bcrypt_context.hash(usuario.senha)
        result = await createAccount(usuario.email, hashed_password, usuario.nome, session)
        response.status_code = result['status_code']
        return result
    except AppException as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro interno: {str(e)}')
