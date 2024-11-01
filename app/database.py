# app/database.py

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT")

# Configuração do banco de dados, troque pela sua URL do banco de dados
DATABASE_URL = f"postgresql+asyncpg://cloud:cloud@db:5432/usuarios"

# Cria o engine assíncrono para o banco de dados
engine = create_async_engine(DATABASE_URL)

# Cria uma sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base para as classes de modelo
Base = declarative_base()

# Função que é usada como dependência para obter uma sessão do banco
async def get_db():
    async with SessionLocal() as session:
        yield session
