from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import List
# from pydantic import BaseModel
from FastAPI.src.Book.book_data import books
from FastAPI.src.Book.schemas import Book, BookUpdate

app = FastAPI()

#
# @app.get("/")
# async def read_root():
#     return {"message": "Hello Vishwajeet"}
#
#
# # If path parameter is not provided then the parameter inside the function is treated as query parameter
# @app.get("/greet")
# async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name}, Hope your are fantastic!!!!  :)))), ", "age": age}
#
#
# class BookCreateModal(BaseModel):
#     title: str
#     author: str
#
#
# @app.post("/create_book")
# async def create_book(book_data: BookCreateModal):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }
#
#
# @app.get('/get_headers', status_code=200)
# # @app.get('/get_headers', status_code=500)  # We can customize the status code from here.
# async def get_headers(
#         accept: str = Header(None),
#         content_type: str = Header(None),
#         user_agent: str = Header(None),
#         host: str = Header(None),
# ):
#     request_header = {}
#     request_header["Accept"] = accept
#     request_header["Content-Type"] = content_type
#     request_header["User-Agent"] = user_agent
#     request_header["Host"] = host
#     return request_header


# ********************************************** CRUD *************************************


# CRUD Routing
