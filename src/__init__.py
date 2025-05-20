from fastapi import FastAPI
from .Book.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

version = "v1.0.0"

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server has been stopped.")

app = FastAPI(
    title="Bookly",
    description="A REST API for book review web service",
    version=version,
    lifespan=lifespan  # Note: lowercase 'lifespan'
)

# Include the router with proper prefix
app.include_router(
    book_router,
    prefix=f"/api/{version}",  # Remove '/books' from here since it's in the router
    tags=['Books']
)