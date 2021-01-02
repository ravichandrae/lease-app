from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class UserType(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class UserStatus(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    mobile: str
    name: str


class UserCreate(UserBase):
    type_id: Optional[str] = None
    status_id: Optional[str] = None


class User(UserBase):
    id: int
    mobile: str
    name: str
    type: Optional[UserType] = None
    status: Optional[UserStatus] = None

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


class RateCardCreate(BaseModel):
    type_id: str
    quantity: float
    amount: float
    currency: str

    class Config:
        orm_mode = True


class RateCard(BaseModel):
    type: RateCardType
    quantity: float
    amount: float
    currency: str

    class Config:
        orm_mode = True


class MakerBase(BaseModel):
    name: str


class Maker(MakerBase):
    id: int

    class Config:
        orm_mode = True


class MachineModelCreate(BaseModel):
    maker_id: int
    name: str
    type_id: str


class MachineModel(BaseModel):
    id: int
    maker: Maker
    type: MachineType
    name: str

    class Config:
        orm_mode = True


class Machine(BaseModel):
    id: int
    model: MachineModel
    rate_card: RateCard
    user: User

    class Config:
        orm_mode = True


class MachineCreate(BaseModel):
    model_id: int
    rate_card_id: int
    user_id: int
    mf_year: Optional[int] = None


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
    status_id: Optional[str] = None
    payment_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        orm_mode = True


class BookingRequest(BaseModel):
    machine_id: int
    from_date: datetime
    to_date: datetime


class BookingStatusUpdate(BaseModel):
    id: int
    status_id: str


class BookingPaymentUpdate(BaseModel):
    id: int
    payment_id: str


class Payment(BaseModel):
    id: int
    amount: float
    type_id: str
    status_id: str
    ref_id: str

    class Config:
        orm_mode = True
