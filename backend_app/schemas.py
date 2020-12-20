from pydantic import BaseModel


class UserBase(BaseModel):
    mobile: str
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    mobile: str
    name: str

    class Config:
        orm_mode = True
