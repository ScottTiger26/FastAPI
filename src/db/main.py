# This is a sql engine i.e. it will handle everything related to database And it is going to be an async engine.
from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(
create_engine(
    url=Config.DATABASE_URL,
    echo=True # For logging every transaction
))

# To keep the database connection live till the user is connected
async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")

        result = await conn.execute(statement)
        print(result.all())


