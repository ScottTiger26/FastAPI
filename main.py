from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel

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
books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downy",
        "publisher": "O'Reilly Media",
        "published_date": "2020-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Think Different",
        "author": "Allen V. Downy",
        "publisher": "O'Reilly Media",
        "published_date": "2020-01-01",
        "page_count": 1144,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Python Vibes",
        "author": "Rodriguez B. Downy",
        "publisher": "Tata MacGraw Hill",
        "published_date": "2025-01-01",
        "page_count": 1342,
        "language": "Sanskrit",
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
# Model to Update
class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

# CRUD Routing
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump() # It converts the new_book to dictionary
    books.append(new_book)
    return new_book

@app.get("/books/{book_id}")
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Book not Found"
    )

@app.patch("/books/{book_id}")
async def update_a_book(book_id: int, book_update_data: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Does not exist."
    )

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

        return {}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Book not found"
    )
