from passlib.context import CryptContext
import jwt
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
from models import User
from database import get_db
import os


# Chave secreta e algoritmo para JWT
SECRET_KEY = str(os.getenv("SECRET_KEY", "secret"))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def authenticate_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalars().first()


    #mudei aqui , antes estava user.hashed_password
    hashed_password = get_password_hash(password)
    if not user:
        return False
    if not verify_password(password, hashed_password):
        return False
    return user

async def validate_jwt(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded  
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

