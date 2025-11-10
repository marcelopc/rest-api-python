from sqlalchemy.orm import sessionmaker
from models import db
from utils.crypto import bcrypt_context
from utils.token import tokenGenerate, verifyToken

def create_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def get_bcrypt():
    return bcrypt_context

def get_token_generator():
    return tokenGenerate

def get_token_verifier():
    return verifyToken
