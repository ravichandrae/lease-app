from typing import List

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import dal
import models
import schemas
from database import engine, SessionLocal

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:19006",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user_status/", response_model=schemas.UserStatus)
def create_user_status(user_status: schemas.UserStatus, db: Session = Depends(get_db)):
    db_user_status = dal.get_user_status_by_id(db, status_id=user_status.id)
    if db_user_status:
        raise HTTPException(status_code=400, detail="Status code already exists")
    return dal.create_user_status(db=db, user_status=user_status)


@app.get("/user_status/", response_model=List[schemas.UserStatus])
def read_user_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_statuses = dal.get_user_statuses(db, skip=skip, limit=limit)
    return user_statuses


@app.get("/user_status/{status_id}", response_model=schemas.UserStatus)
def read_user_status(status_id: str, db: Session = Depends(get_db)):
    db_user_status = dal.get_user_status_by_id(db, status_id=status_id)
    if db_user_status is None:
        raise HTTPException(status_code=404, detail="User status not found")
    return db_user_status


@app.post("/provider_status/", response_model=schemas.ProviderStatus)
def create_provider_status(provider_status: schemas.ProviderStatus, db: Session = Depends(get_db)):
    db_provider_status = dal.get_provider_status_by_id(db, status_id=provider_status.id)
    if db_provider_status:
        raise HTTPException(status_code=400, detail="Status code already exists")
    return dal.create_provider_status(db=db, provider_status=provider_status)


@app.get("/provider_status/", response_model=List[schemas.ProviderStatus])
def read_provider_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    provider_statuses = dal.get_provider_statuses(db, skip=skip, limit=limit)
    return provider_statuses


@app.get("/provider_status/{status_id}", response_model=schemas.ProviderStatus)
def read_provider_status(status_id: str, db: Session = Depends(get_db)):
    db_provider_status = dal.get_provider_status_by_id(db, status_id=status_id)
    if db_provider_status is None:
        raise HTTPException(status_code=404, detail="Provider status not found")
    return db_provider_status


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = dal.get_user_by_mobile(db, mobile=user.mobile)
    if db_user:
        raise HTTPException(status_code=400, detail="mobile already registered")
    return dal.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = dal.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = dal.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/login", response_model=schemas.UserLoginResponse)
def login_user(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    print(user_login.mobile)
    print(user_login.otp)
    resp = schemas.UserLoginResponse(mobile="1234", message="Success")
    return resp


@app.post("/providers/", response_model=schemas.Provider)
def create_provider(provider: schemas.CreateProviderRequest, db: Session = Depends(get_db)):
    db_provider = dal.get_provider_by_mobile(db, mobile=provider.mobile)
    if db_provider:
        raise HTTPException(status_code=400, detail="Mobile already registered")
    return dal.create_provider(db=db, provider=provider)


@app.get("/providers/", response_model=List[schemas.Provider])
def read_providers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = dal.get_providers(db, skip=skip, limit=limit)
    return users


@app.get("/providers/{provider_id}", response_model=schemas.Provider)
def read_provider(provider_id: int, db: Session = Depends(get_db)):
    db_provider = dal.get_provider(db, provider_id=provider_id)
    if db_provider is None:
        raise HTTPException(status_code=404, detail="Provider not found")
    return db_provider


@app.post("/machines/", response_model=schemas.Machine)
def create_machine(machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    return dal.create_machine(db=db, machine=machine)


@app.get("/machines/", response_model=List[schemas.Machine])
def read_machines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = dal.get_machines(db, skip=skip, limit=limit)
    return users


@app.get("/machines/{machine_id}", response_model=schemas.Machine)
def read_machine(machine_id: int, db: Session = Depends(get_db)):
    db_machine = dal.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return db_machine


@app.post("/machine_types/", response_model=schemas.MachineType)
def create_machine_type(machine_type: schemas.MachineType, db: Session = Depends(get_db)):
    return dal.create_machine_type(db=db, machine_type=machine_type)


@app.get("/machine_types/", response_model=List[schemas.MachineType])
def read_machine_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machine_types = dal.get_machine_types(db, skip=skip, limit=limit)
    return machine_types


@app.get("/machine_types/{machine_type_id}", response_model=schemas.MachineType)
def read_machine_type(machine_type_id: str, db: Session = Depends(get_db)):
    db_machine_type = dal.get_machine_type(db, machine_type_id=machine_type_id)
    if db_machine_type is None:
        raise HTTPException(status_code=404, detail="Machine Type not found")
    return db_machine_type


@app.post("/makers/", response_model=schemas.Maker)
def create_maker(maker: schemas.MakerBase, db: Session = Depends(get_db)):
    return dal.create_maker(db=db, maker=maker)


@app.get("/makers/", response_model=List[schemas.Maker])
def read_makers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    makers = dal.get_makers(db, skip=skip, limit=limit)
    return makers


@app.get("/makers/{maker_id}", response_model=schemas.Maker)
def read_maker(maker_id: int, db: Session = Depends(get_db)):
    db_maker = dal.get_maker(db, maker_id=maker_id)
    if db_maker is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_maker


@app.post("/machine_models/", response_model=schemas.MachineModel)
def create_machine_model(machine_model: schemas.MachineModelCreate, db: Session = Depends(get_db)):
    return dal.create_machine_model(db=db, machine_model=machine_model)


@app.get("/machine_models/", response_model=List[schemas.MachineModel])
def read_machine_models(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machine_models = dal.get_machine_models(db, skip=skip, limit=limit)
    return machine_models


@app.get("/machine_models/{model_id}", response_model=schemas.MachineModel)
def read_machine_model(model_id: int, db: Session = Depends(get_db)):
    db_machine_model = dal.get_machine_model(db, model_id=model_id)
    if db_machine_model is None:
        raise HTTPException(status_code=404, detail="Machine model not found")
    return db_machine_model


@app.post("/rate_card_types/", response_model=schemas.RateCardType)
def create_rate_card_type(rate_card_type: schemas.RateCardType, db: Session = Depends(get_db)):
    return dal.create_rate_card_type(db=db, rate_card_type=rate_card_type)


@app.get("/rate_card_types/", response_model=List[schemas.RateCardType])
def read_rate_card_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rate_card_types = dal.get_rate_card_types(db, skip=skip, limit=limit)
    return rate_card_types


@app.get("/rate_card_types/{rate_card_type_id}", response_model=schemas.RateCardType)
def read_rate_card_type(rate_card_type_id: str, db: Session = Depends(get_db)):
    db_rate_card_type = dal.get_rate_card_type(db, rate_card_type_id=rate_card_type_id)
    if db_rate_card_type is None:
        raise HTTPException(status_code=404, detail="Rate card type not found")
    return db_rate_card_type


@app.post("/rate_cards/", response_model=schemas.RateCard)
def create_rate_card(rate_card: schemas.RateCardCreate, db: Session = Depends(get_db)):
    return dal.create_rate_card(db=db, rate_card=rate_card)


@app.get("/rate_cards/", response_model=List[schemas.RateCard])
def read_rate_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rate_cards = dal.get_rate_cards(db, skip=skip, limit=limit)
    return rate_cards


@app.get("/rate_cards/{rate_card_id}", response_model=schemas.RateCard)
def read_rate_card(rate_card_id: int, db: Session = Depends(get_db)):
    db_rate_card = dal.get_rate_card(db, rate_card_id=rate_card_id)
    if db_rate_card is None:
        raise HTTPException(status_code=404, detail="Rate card not found")
    return db_rate_card


@app.post("/booking_status/", response_model=schemas.BookingStatus)
def create_booking_status(booking_status: schemas.BookingStatus, db: Session = Depends(get_db)):
    return dal.create_booking_status(db=db, booking_status=booking_status)


@app.get("/booking_status/", response_model=List[schemas.BookingStatus])
def read_booking_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    booking_statuses = dal.get_booking_statuses(db, skip=skip, limit=limit)
    return booking_statuses


@app.get("/booking_status/{booking_status_id}", response_model=schemas.BookingStatus)
def read_booking_status(booking_status_id: str, db: Session = Depends(get_db)):
    db_booking_status = dal.get_booking_status(db, booking_status_id=booking_status_id)
    if db_booking_status is None:
        raise HTTPException(status_code=404, detail="Booking status not found")
    return db_booking_status


@app.post("/payment_types/", response_model=schemas.PaymentType)
def create_payment_type(payment_type: schemas.PaymentType, db: Session = Depends(get_db)):
    return dal.create_payment_type(db=db, payment_type=payment_type)


@app.get("/payment_types/", response_model=List[schemas.PaymentType])
def read_payment_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payment_types = dal.get_payment_types(db, skip=skip, limit=limit)
    return payment_types


@app.get("/payment_types/{payment_type_id}", response_model=schemas.PaymentType)
def read_payment_type(payment_type_id: str, db: Session = Depends(get_db)):
    db_payment_type = dal.get_payment_type(db, payment_type_id=payment_type_id)
    if db_payment_type is None:
        raise HTTPException(status_code=404, detail="Payment Type not found")
    return db_payment_type


@app.post("/payment_status/", response_model=schemas.PaymentStatus)
def create_payment_status(payment_status: schemas.PaymentStatus, db: Session = Depends(get_db)):
    db_payment_status = dal.get_payment_status(db, payment_status_id=payment_status.id)
    if db_payment_status:
        raise HTTPException(status_code=400, detail="Payment status code already registered")
    return dal.create_payment_status(db=db, payment_status=payment_status)


@app.get("/payment_status/", response_model=List[schemas.PaymentStatus])
def read_payment_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payment_statuses = dal.get_payment_statuses(db, skip=skip, limit=limit)
    return payment_statuses


@app.get("/payment_status/{payment_status_id}", response_model=schemas.PaymentStatus)
def read_payment_status(payment_status_id: str, db: Session = Depends(get_db)):
    db_payment_status = dal.get_payment_status(db, payment_status_id=payment_status_id)
    if db_payment_status is None:
        raise HTTPException(status_code=404, detail="Payment status not found")
    return db_payment_status


@app.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking_request: schemas.BookingRequest, db: Session = Depends(get_db)):
    return dal.create_booking(db=db, booking_request=booking_request)


@app.get("/bookings/", response_model=List[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = dal.get_bookings(db, skip=skip, limit=limit)
    return bookings


@app.get("/bookings/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = dal.get_booking(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking


@app.put("/bookings/status", response_model=schemas.Booking)
def update_booking_status(booking_status_update: schemas.BookingStatusUpdate, db: Session = Depends(get_db)):
    db_booking = dal.get_booking(db, booking_id=booking_status_update.id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return dal.update_booking_status(db=db, booking_status_update=booking_status_update)


@app.put("/bookings/machine", response_model=schemas.Booking)
def accept_booking(accept_booking_request: schemas.AcceptBookingRequest, db: Session = Depends(get_db)):
    db_booking = dal.get_booking(db, booking_id=accept_booking_request.id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return dal.update_booking_machine(db=db, accept_booking_request=accept_booking_request)


@app.put("/bookings/start_date", response_model=schemas.Booking)
def update_booking_start(booking_start_request: schemas.BookingStartRequest, db: Session = Depends(get_db)):
    db_booking = dal.get_booking(db, booking_id=booking_start_request.id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    if db_booking.machine_id is None:
        raise HTTPException(status_code=400, detail="Booking not accepted")
    return dal.update_booking_start_date(db=db, booking_start_request=booking_start_request)


@app.put("/bookings/end_date", response_model=schemas.Booking)
def update_booking_end(booking_end_request: schemas.BookingEndRequest, db: Session = Depends(get_db)):
    db_booking = dal.get_booking(db, booking_id=booking_end_request.id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    if db_booking.start_date is None:
        raise HTTPException(status_code=400, detail="Booking has not started")
    if db_booking.machine_id is None:
        raise HTTPException(status_code=400, detail="No machine allotted")
    return dal.end_booking(db=db, booking_end_request=booking_end_request)

