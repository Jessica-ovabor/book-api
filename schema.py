import pydantic as pydantic
import datetime as datetime
from typing import Optional

class BookBase(pydantic.BaseModel):
    
    title: str
    author: str
    year: int
    isbn: str

class BookUpdate(BookBase):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
    isbn: Optional[str]
class BookResponse(BookBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True




