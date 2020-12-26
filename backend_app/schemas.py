from pydantic import BaseModel


class UserBase(BaseModel):
    mobile: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    mobile: str
    name: str

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    mobile: str
    otp: str

    class Config:
        orm_mode = True


class UserLoginResponse(UserBase):
    message: str

    class Config:
        orm_mode = True

