#
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException, Path, Query, status

#  Import FILES
from data.dict_db import BOOKS
from models.models import Book, BookRequest

#   ...

app = FastAPI()


# BOOKS = []


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"Message": "This is root"}


@app.get(path="/books", response_model=None, status_code=status.HTTP_200_OK)
async def read_all_books() -> list[Book]:
    return BOOKS


@app.get(path="/books/{book_id]", status_code=status.HTTP_200_OK, response_model=None)
async def read_book(book_id: int = Path(gt=0)) -> Book | None:
    # async def read_book(book_id: int) -> Book | None:
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.put(path="/books/update_book", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest) -> None:
    book_changed: bool = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed: bool = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get(path="/books/", response_model=None, status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)) -> list[Book]:
    books_to_return: list[Book] = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get(path="/books/publish/", response_model=None, status_code=status.HTTP_201_CREATED)
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)) -> list[Book]:
    books_to_return: list[Book] = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


# {"id": 7, "title": "A book", "author": "Me Myself", "description": "another book", "rating": 4}
@app.post(path="/create-book", status_code=status.HTTP_204_NO_CONTENT)  # , response_model=None)
async def create_book(book_request: BookRequest) -> None:
    new_book = Book(**book_request.model_dump())
    # new_book = Book(**book_request.dict())
    print(type(book_request))
    print(type(new_book))
    BOOKS.append(find_book_id(book=new_book))
    # BOOKS.append(new_book)


#  NB Add "Body": from fastapi import FastAPI, Body
# @app.post(path="/create-book", response_model=None)
# async def create_book(book_request: Book = Body(default=...)) -> None:
#     BOOKS.append(book_request)


def find_book_id(book: Book) -> Book:
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book


@app.delete("/books/{book_id}", response_model=None)
async def delete_book(book_id: int = Path(gt=0)) -> None:
    book_changed: bool = =False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed: bool = True
            break               
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")


#
#  Import LIBRARIES
#  Import FILES
#   ...
