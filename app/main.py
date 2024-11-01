from fastapi import FastAPI
from routes import router as user_router
from database import engine, Base

app = FastAPI()

# Incluindo as rotas
app.include_router(user_router)

# Criação do banco de dados
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "API is running"}
