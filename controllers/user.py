from models import Usuario
from exceptions import AppException


async def createAccount(email:str, senha:str, nome:str, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    
    if usuario:
        raise AppException('Usuário já existe', 409)

    novoUsuario = Usuario(nome, email, senha)
    session.add(novoUsuario)
    session.commit()
    return {'message': 'Usuário criado com sucesso', 'status_code': 201}
