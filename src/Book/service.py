from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdate
from sqlmodel import select, desc
from .models import Book

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))

        result = await session.execute(statement)
        return result.all()


    async def get_book(self, book_uid:str,session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.execute(statement)
        return result.first()

    async def create_book(self, book_data:BookCreateModel,session: AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(
            **book_data_dict
        )
        session.add(new_book)
        await session.commit()
        # await session.refresh(new_book)
        return new_book

    async def update_book(self, book_uid:str,update_data:BookUpdate,session: AsyncSession):
        pass
    async def delete_book(self, book_uid:str,session: AsyncSession):
        pass