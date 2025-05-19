# This is a sql engine i.e. it will handle everything related to database And it is going to be an async engine.
from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.Book.models import Book

engine = AsyncEngine(
create_engine(
    url=Config.DATABASE_URL,
    echo=True # For logging every transaction
))

# To keep the database connection live till the user is connected
async def init_db():
    async with engine.begin() as conn:

        await conn.run_sync(SQLModel.metadata.create_all)

# statement = text("SELECT 'hello';")
#
# result = await conn.execute(statement)
# print(result.all())





