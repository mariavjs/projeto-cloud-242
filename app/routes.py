from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session
from auth import create_access_token, verify_password, authenticate_user, get_password_hash, validate_jwt
from models import User
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Request
from database import get_db
from sqlalchemy.future import select
from scraping import get_random_dog
import jwt
from auth import SECRET_KEY

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic model para criação de usuário
class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

# Modelo para login
class UserLogin(BaseModel):
    email: str
    senha: str

class AuthResponse(BaseModel):
    jwt: str

# Registrar o usuário
@router.post("/registrar", response_model=AuthResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # Use o select em vez de query
    result = await db.execute(select(User).filter(User.email == user.email))
    db_user = result.scalars().first()

    if db_user:
        raise HTTPException(status_code=409, detail="Email já registrado")
    
    hashed_password = get_password_hash(user.senha)
    # Certifique-se de que o modelo User está usando `nome` em vez de `name`
    new_user = User(nome=user.nome, email=user.email, senha_hash=hashed_password)
 

    db.add(new_user)
    await db.commit()  # Comitar de forma assíncrona
    await db.refresh(new_user)  # Atualizar a instância do usuário após a criação
    
    # Gera o token de acesso
    token = create_access_token({"sub": new_user.email})

    return {
        "jwt": token,
    }

# Faça login 
@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = await authenticate_user(db, user.email, user.senha)
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": db_user.email})
    return {"jwt": token}

# Endpoint GET /consultar que exige autenticação via JWT
@router.get("/consultar")
def consultar_data(token: str):
    # Verifica se o header Authorization foi enviado corretamente
    #decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    
       
        return  get_random_dog()
    
    except jwt.InvalidTokenError:
        raise {"error": "token inválido"}
    
