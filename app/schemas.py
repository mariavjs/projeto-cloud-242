from pydantic import BaseModel

# Modelo Pydantic para criação de usuário
class UserCreate(BaseModel):
    nome: str
    email: str
    password: str

# Modelo Pydantic para login de usuário
class UserLogin(BaseModel):
    email: str
    password: str

# Modelo Pydantic para resposta de autenticação
class AuthResponse(BaseModel):
    jwt: str
