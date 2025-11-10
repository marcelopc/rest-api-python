from fastapi import APIRouter, Depends, HTTPException, Response
from dependencies import create_session, get_bcrypt, get_token_generator, get_token_verifier
from schemas.login import LoginSchema
from schemas.oauth import Oauth2Schema
from sqlalchemy.orm import Session
from controllers.auth import login, refreshToken
from exceptions import AppException

PREFIX = '/auth'
authRouter = APIRouter(prefix=PREFIX, tags=['Authentication'])

@authRouter.post('/login')
async def auth(
    body: LoginSchema, 
    response: Response, 
    session: Session = Depends(create_session),
    bcrypt = Depends(get_bcrypt),
    tokenGenerate = Depends(get_token_generator)
):
    try:
        output = login(body.email, body.senha, session, bcrypt, tokenGenerate)
        return output
    except AppException as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro interno: {str(e)}')
    
@authRouter.get('/refresh')
async def refresh(
    token: str = Depends(Oauth2Schema), 
    session: Session = Depends(create_session),
    tokenGenerate = Depends(get_token_generator),
    verifyToken = Depends(get_token_verifier)
):
    try:
        output = refreshToken(token, session, tokenGenerate, verifyToken)
        return output
    except AppException as e:
        raise HTTPException(status_code=e.status, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro interno: {str(e)}')
    
