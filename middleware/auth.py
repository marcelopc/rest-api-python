from fastapi import Depends, HTTPException
from dependencies import get_token_verifier
from schemas.oauth import Oauth2Schema
from exceptions import AppException

def ValidateToken( token: str = Depends(Oauth2Schema), verifyToken = Depends(get_token_verifier)):
    try:
        verifyToken(token)
    except Exception as e:
        error_message = str(e)
        if 'Token expirado' in error_message:
            raise AppException('Token expirado', 403)
        if 'Token inválido' in error_message:
            raise AppException('Token inválido', 401)
    