from fastapi.security import OAuth2PasswordBearer

Oauth2Schema = OAuth2PasswordBearer(tokenUrl="auth/login")