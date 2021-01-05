from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
import services


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_mobile(db: Session, mobile: str):
    return db.query(models.User).filter(models.User.mobile == mobile).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    current_date = datetime.now()
    db_user = models.User(mobile=user.mobile,
                          name=user.name,
                          created_at=current_date,
                          updated_at=current_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_provider(db: Session, provider_id: int):
    return db.query(models.Provider).filter(models.Provider.id == provider_id).first()


def get_provider_by_mobile(db: Session, mobile: str):
    return db.query(models.Provider).filter(models.Provider.mobile == mobile).first()


def get_providers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Provider).offset(skip).limit(limit).all()


def create_provider(db: Session, provider: schemas.CreateProviderRequest):
    current_date = datetime.now()
    db_provider = models.Provider(mobile=provider.mobile,
                                  name=provider.name,
                                  created_at=current_date,
                                  updated_at=current_date)
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider


def get_maker(db: Session, maker_id: int):
    return db.query(models.Maker).filter(models.Maker.id == maker_id).first()


def get_makers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Maker).offset(skip).limit(limit).all()


def create_machine(db: Session, machine: schemas.MachineCreate):
    current_date = datetime.now()
    db_machine = models.Machine(model_id=machine.model_id,
                                mf_year=machine.mf_year,
                                rate_card_id=machine.rate_card_id,
                                provider_id=machine.provider_id,
                                created_at=current_date,
                                updated_at=current_date
                                )
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine


def get_machine(db: Session, machine_id: int):
    return db.query(models.Machine).filter(models.Machine.id == machine_id).first()


def get_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Machine).offset(skip).limit(limit).all()


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


def get_machine_type(db: Session, machine_type_id: str):
    return db.query(models.MachineType).filter(models.MachineType.id == machine_type_id).first()


def get_machine_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MachineType).offset(skip).limit(limit).all()


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


def get_machine_model(db: Session, model_id: int):
    return db.query(models.MachineModel).filter(models.MachineModel.id == model_id).first()


def get_machine_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MachineModel).offset(skip).limit(limit).all()


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


def get_rate_card_type(db: Session, rate_card_type_id: str):
    return db.query(models.RateCardType).filter(models.RateCardType.id == rate_card_type_id).first()


def get_rate_card_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RateCardType).offset(skip).limit(limit).all()


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


def get_rate_card(db: Session, rate_card_id: int):
    return db.query(models.RateCard).filter(models.RateCard.id == rate_card_id).first()


def get_rate_cards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RateCard).offset(skip).limit(limit).all()


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


def get_booking_status(db: Session, booking_status_id: str):
    return db.query(models.BookingStatus).filter(models.BookingStatus.id == booking_status_id).first()


def get_booking_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BookingStatus).offset(skip).limit(limit).all()


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


def get_payment_type(db: Session, payment_type_id: str):
    return db.query(models.PaymentType).filter(models.PaymentType.id == payment_type_id).first()


def get_payment_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PaymentType).offset(skip).limit(limit).all()


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


def get_payment_status(db: Session, payment_status_id: str):
    return db.query(models.PaymentStatus).filter(models.PaymentStatus.id == payment_status_id).first()


def get_payment_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PaymentStatus).offset(skip).limit(limit).all()


def create_booking(db: Session, booking_request: schemas.BookingRequest):
    current_date = datetime.now()
    db_booking = models.Booking(machine_type_id=booking_request.machine_type_id,
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


def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()


def update_booking_status(db: Session, booking_status_update: schemas.BookingStatusUpdate):
    current_date = datetime.now()
    db_booking = get_booking(db, booking_status_update.id)
    db_booking.status_id = booking_status_update.status_id
    db_booking.updated_at = current_date
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def update_booking_start_date(db: Session, booking_start_request: schemas.BookingStartRequest):
    current_date = datetime.now()
    db_booking = get_booking(db, booking_start_request.id)
    db_booking.start_date = booking_start_request.start_date
    db_booking.updated_at = current_date
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def end_booking(db: Session, booking_end_request: schemas.BookingEndRequest):
    current_date = datetime.now()
    db_booking = get_booking(db, booking_end_request.id)
    db_booking.end_date = booking_end_request.end_date
    db_booking.area = booking_end_request.area
    db_booking.updated_at = current_date
    db_booking.amount = services.get_booking_amount(db_booking)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def update_booking_machine(db: Session, accept_booking_request: schemas.AcceptBookingRequest):
    current_date = datetime.now()
    db_booking = get_booking(db, accept_booking_request.id)
    db_booking.machine_id = accept_booking_request.machine_id
    db_booking.status_id = accept_booking_request.status_id
    db_booking.updated_at = current_date
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_user_status_by_id(db: Session, status_id: str):
    return db.query(models.UserStatus).filter(models.UserStatus.id == status_id).first()


def create_user_status(db: Session, user_status: schemas.UserStatus):
    current_date = datetime.now()
    db_user_status = models.UserStatus(id=user_status.id,
                                       description=user_status.description,
                                       created_at=current_date,
                                       updated_at=current_date)
    db.add(db_user_status)
    db.commit()
    db.refresh(db_user_status)
    return db_user_status


def get_user_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserStatus).offset(skip).limit(limit).all()


def get_provider_status_by_id(db: Session, status_id: str):
    return db.query(models.ProviderStatus).filter(models.ProviderStatus.id == status_id).first()


def create_provider_status(db: Session, provider_status: schemas.ProviderStatus):
    current_date = datetime.now()
    db_provider_status = models.ProviderStatus(id=provider_status.id,
                                               description=provider_status.description,
                                               created_at=current_date,
                                               updated_at=current_date)
    db.add(db_provider_status)
    db.commit()
    db.refresh(db_provider_status)
    return db_provider_status


def get_provider_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProviderStatus).offset(skip).limit(limit).all()
