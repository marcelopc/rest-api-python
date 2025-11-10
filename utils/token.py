from jose import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
ALGORITHM = os.getenv('ALGORITHM')

def tokenGenerate(idusuario:int, ttl=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)) -> str:
    dataExpiracao = datetime.now(timezone.utc) + ttl
    payload = { 'sub': str(idusuario) , 'exp': dataExpiracao }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verifyToken(token:str):
    try:
        return jwt.decode(token, SECRET_KEY, ALGORITHM)
    except jwt.ExpiredSignatureError:
        raise Exception('Token expirado')
    except jwt.JWTError:
        raise Exception('Token inválido')