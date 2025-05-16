from fastapi import FastAPI
from .Book.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db



@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting ...")
    await init_db()
    yield                               # This will decide what will run first and second. Usually the one written above will run first.
    print(f"Server has been stopped.")

version = "v1.0.0"

app = FastAPI(
    title="Bookly",
    description="A REST API for book review web service",
    version=version,
    life_span=life_span

)
app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])