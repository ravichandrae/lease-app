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


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = dal.get_user_by_mobile(db, mobile=user.mobile)
    if db_user:
        raise HTTPException(status_code=400, detail="mobile already registered")
    return dal.create_user(db=db, user=user)


@app.post("/users/login", response_model=schemas.UserLoginResponse)
def login_user(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    print(user_login.mobile)
    print(user_login.otp)
    resp = schemas.UserLoginResponse(mobile="1234", message="Success")
    return resp


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


@app.post("/machines/", response_model=schemas.Machine)
def create_machine(machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    return dal.create_machine(db=db, machine=machine)


@app.post("/machine_types/", response_model=schemas.MachineType)
def create_machine(machine_type: schemas.MachineType, db: Session = Depends(get_db)):
    return dal.create_machine_type(db=db, machine_type=machine_type)


@app.post("/makers/", response_model=schemas.Maker)
def create_machine(maker: schemas.MakerBase, db: Session = Depends(get_db)):
    return dal.create_maker(db=db, maker=maker)


@app.post("/machine_models/", response_model=schemas.MachineModel)
def create_machine_model(machine_model: schemas.MachineModelCreate, db: Session = Depends(get_db)):
    return dal.create_machine_model(db=db, machine_model=machine_model)


@app.post("/rate_card_types/", response_model=schemas.RateCardType)
def create_rate_card_type(rate_card_type: schemas.RateCardType, db: Session = Depends(get_db)):
    return dal.create_rate_card_type(db=db, rate_card_type=rate_card_type)


@app.post("/rate_cards/", response_model=schemas.RateCard)
def create_rate_card(rate_card: schemas.RateCardCreate, db: Session = Depends(get_db)):
    return dal.create_rate_card(db=db, rate_card=rate_card)


@app.post("/booking_status/", response_model=schemas.BookingStatus)
def create_booking_status(booking_status: schemas.BookingStatus, db: Session = Depends(get_db)):
    return dal.create_booking_status(db=db, booking_status=booking_status)


@app.post("/payment_types/", response_model=schemas.PaymentType)
def create_payment_type(payment_type: schemas.PaymentType, db: Session = Depends(get_db)):
    return dal.create_payment_type(db=db, payment_type=payment_type)


@app.post("/payment_status/", response_model=schemas.PaymentStatus)
def create_payment_status(payment_status: schemas.PaymentStatus, db: Session = Depends(get_db)):
    return dal.create_payment_status(db=db, payment_status=payment_status)


@app.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking_request: schemas.BookingRequest, db: Session = Depends(get_db)):
    return dal.create_booking(db=db, booking_request=booking_request)


@app.put("/bookings", response_model=schemas.Booking)
def update_booking(booking_status_update: schemas.BookingStatusUpdate, db: Session = Depends(get_db)):
    return dal.update_booking(db=db, booking_status_update=booking_status_update)

