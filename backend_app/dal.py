from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_mobile(db: Session, mobile: str):
    return db.query(models.User).filter(models.User.mobile == mobile).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    current_date = datetime.now()
    db_user = models.User(mobile=user.mobile,
                          name=user.name,
                          status_id=user.status_id,
                          type_id=user.type_id,
                          created_at=current_date,
                          updated_at=current_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_machine(db: Session, machine: schemas.MachineCreate):
    current_date = datetime.now()
    db_machine = models.Machine(model_id=machine.model_id,
                                mf_year=machine.mf_year,
                                rate_card_id=machine.rate_card_id,
                                user_id=machine.user_id,
                                created_at=current_date,
                                updated_at=current_date
                                )
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine


def create_machine_type(db: Session, machine_type: schemas.MachineType):
    current_date = datetime.now()
    db_machine_type = models.MachineType(id=machine_type.id,
                                         name=machine_type.name,
                                         created_at=current_date,
                                         updated_at=current_date
                                         )
    db.add(db_machine_type)
    db.commit()
    db.refresh(db_machine_type)
    return db_machine_type


def create_maker(db: Session, maker: schemas.MakerBase):
    current_date = datetime.now()
    db_maker = models.Maker(name=maker.name, created_at=current_date, updated_at=current_date)
    db.add(db_maker)
    db.commit()
    db.refresh(db_maker)
    return db_maker


def create_machine_model(db: Session, machine_model: schemas.MachineModelCreate):
    current_date = datetime.now()
    db_machine_model = models.MachineModel(maker_id=machine_model.maker_id,
                                           name=machine_model.name,
                                           type_id=machine_model.type_id,
                                           created_at=current_date,
                                           updated_at=current_date)
    db.add(db_machine_model)
    db.commit()
    db.refresh(db_machine_model)
    return db_machine_model


def create_rate_card_type(db:Session, rate_card_type: schemas.RateCardType):
    current_date = datetime.now()
    db_rate_card_type = models.RateCardType(id=rate_card_type.id,
                                            description=rate_card_type.description,
                                            created_at=current_date,
                                            updated_at=current_date)
    db.add(db_rate_card_type)
    db.commit()
    db.refresh(db_rate_card_type)
    return db_rate_card_type


def create_rate_card(db: Session, rate_card: schemas.RateCardCreate):
    current_date = datetime.now()
    db_rate_card = models.RateCard(type_id=rate_card.type_id,
                                   quantity=rate_card.quantity,
                                   amount=rate_card.amount,
                                   currency=rate_card.currency,
                                   created_at=current_date,
                                   updated_at=current_date)
    db.add(db_rate_card)
    db.commit()
    db.refresh(db_rate_card)
    return db_rate_card


def create_booking_status(db: Session, booking_status: schemas.BookingStatus):
    current_date = datetime.now()
    db_booking_status = models.BookingStatus(id=booking_status.id,
                                             description=booking_status.description,
                                             created_at=current_date,
                                             updated_at=current_date)
    db.add(db_booking_status)
    db.commit()
    db.refresh(db_booking_status)
    return db_booking_status


def create_payment_type(db: Session, payment_type: schemas.PaymentType):
    current_date = datetime.now()
    db_payment_type = models.PaymentType(id=payment_type.id,
                                         description=payment_type.description,
                                         created_at=current_date,
                                         updated_at=current_date)
    db.add(db_payment_type)
    db.commit()
    db.refresh(db_payment_type)
    return db_payment_type


def create_payment_status(db: Session, payment_status: schemas.PaymentStatus):
    current_date = datetime.now()
    db_payment_status = models.PaymentStatus(id=payment_status.id,
                                             description=payment_status.description,
                                             created_at=current_date,
                                             updated_at=current_date)
    db.add(db_payment_status)
    db.commit()
    db.refresh(db_payment_status)
    return db_payment_status


def create_booking(db: Session, booking_request: schemas.BookingRequest):
    current_date = datetime.now()
    db_booking = models.Booking(machine_id=booking_request.machine_id,
                                from_date=booking_request.from_date,
                                to_date=booking_request.to_date,
                                created_at=current_date,
                                updated_at=current_date)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()


def update_booking(db: Session, booking_status_update: schemas.BookingStatusUpdate):
    current_date = datetime.now()
    db_booking = get_booking(db, booking_status_update.id)
    db_booking.status_id = booking_status_update.status_id
    db_booking.updated_at = current_date
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
