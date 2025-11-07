#
#  Import LIBRARIES
from pydantic import BaseModel, ConfigDict, Field

#  Import FILES
#   ...


class BookRequest(BaseModel):
    id: int | None = Field(default=None, description="ID is not needed on creation")
    # id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "A new book",
                "author": "CodingwithManny",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029,
            }
        }
    )


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: int) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
