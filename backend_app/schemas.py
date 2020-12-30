from pydantic import BaseModel
from datetime import datetime


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


class UserLogin(UserBase):
    mobile: str
    otp: str

    class Config:
        orm_mode = True


class UserLoginResponse(UserBase):
    message: str

    class Config:
        orm_mode = True


class MachineType(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class RateCardType(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class RateCard(BaseModel):
    type: RateCardType
    quantity: float
    amount: float
    currency: str

    class Config:
        orm_mode = True


class Machine(BaseModel):
    name: str
    type: MachineType
    rate_card: RateCard
    user: User

    class Config:
        orm_mode = True


class MachineCreate(BaseModel):
    type_id: str
    name: str
    rate_card_id: int
    user_id: int


class PaymentType(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class PaymentStatus(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class BookingStatus(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class Booking(BaseModel):
    id: int
    machine: Machine
    from_date: datetime
    to_date: datetime
    status_id: str
    payment_id: int
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True


class Payment(BaseModel):
    id: int
    amount: float
    type_id: str
    status_id: str
    ref_id: str

    class Config:
        orm_mode = True
