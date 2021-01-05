from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class UserStatus(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class ProviderStatus(BaseModel):
    id: str
    description: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    mobile: str
    name: str


class User(UserBase):
    id: int
    status: Optional[UserStatus] = None

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    mobile: str
    otp: str

    class Config:
        orm_mode = True


class UserLoginResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True


class Provider(BaseModel):
    id: int
    name: str
    mobile: str

    class Config:
        orm_mode = True


class CreateProviderRequest(BaseModel):
    name: str
    mobile: str


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
    id: int
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
    provider: Provider

    class Config:
        orm_mode = True


class MachineCreate(BaseModel):
    model_id: int
    rate_card_id: int
    provider_id: int
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
    machine: Optional[Machine] = None
    from_date: datetime
    to_date: datetime
    status_id: Optional[str] = None
    payment_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    area: Optional[float] = None
    amount: Optional[float] = None

    class Config:
        orm_mode = True


class BookingRequest(BaseModel):
    machine_type_id: str
    from_date: datetime
    to_date: datetime


class BookingStatusUpdate(BaseModel):
    id: int
    status_id: str


class AcceptBookingRequest(BaseModel):
    id: int
    status_id: str
    machine_id: int


class BookingStartRequest(BaseModel):
    id: int
    start_date: datetime


class BookingEndRequest(BaseModel):
    id: int
    end_date: Optional[datetime] = None
    area: Optional[float] = None


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
