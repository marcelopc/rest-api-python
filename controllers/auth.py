from sqlalchemy.orm import Session
from models import Usuario
from exceptions import AppException
from datetime import timedelta
from typing import Callable


def login(
    email: str, 
    senha: str, 
    session: Session, 
    bcrypt, 
    tokenGenerate: Callable[[int, timedelta], str]
):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    
    if not usuario:
        raise AppException('Usuário ou senha incorretos', 404 )

    if bcrypt.verify(senha, usuario.senha) is False:
        raise AppException('Usuário ou senha incorretos', 401 )

    token = tokenGenerate(usuario.id)
    refreshToken = tokenGenerate(usuario.id, timedelta(days=7))

    return {'token': token, 'token_type': 'Bearer', 'refreshToken': refreshToken}

def refreshToken(
    token: str, 
    session: Session, 
    tokenGenerate: Callable[[int, timedelta], str], 
    verifyToken: Callable[[str], dict[str, any]]
):
    try:
        payload = verifyToken(token)
        usuario_id = int(payload['sub'])
        usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
        
        newRefreshToken = tokenGenerate(usuario.id, timedelta(days=7))

        return {'token': newRefreshToken, 'token_type': 'Bearer'}
    except Exception as e:
        error_message = str(e)
        if 'Token expirado' in error_message:
            raise AppException('Token expirado', 403)
        if 'Token inválido' in error_message:
            raise AppException('Token inválido', 401)
        raise AppException(e, 401)
