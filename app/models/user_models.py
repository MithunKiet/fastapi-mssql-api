from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    email: Optional[str] = Field(None, max_length=200)

class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[str]
