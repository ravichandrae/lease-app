from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    mobile: str


class UserCreate(UserBase):
    name: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
