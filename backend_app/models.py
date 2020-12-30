from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    mobile = Column(String(12), unique=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status_code = Column(String(2))


class MachineType(Base):
    __tablename__ = "machine_types"

    id = Column(String(2), primary_key=True, index=True)
    name = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Maker(Base):
    __tablename__ = "makers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class MachineModel(Base):
    __tablename__ = "machine_models"

    id = Column(Integer, primary_key=True, index=True)
    maker_id = Column(Integer, ForeignKey('makers.id'))
    maker = relationship(Maker)
    name = Column(String(50))
    type_id = Column(String(2), ForeignKey('machine_types.id'))
    type = relationship(MachineType)


class RateCardType(Base):
    __tablename__ = "rate_card_types"

    id = Column(String(2), primary_key=True, index=True)
    description = Column(String(50))


class RateCard(Base):
    __tablename__ = "rate_card"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(String(2), ForeignKey('rate_card_types.id'))
    type = relationship(RateCardType)
    quantity = Column(Float)
    amount = Column(Float)
    currency = Column(String(3))


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey('machine_models.id'))
    machine_model = relationship(MachineModel)
    rate_card_id = Column(Integer, ForeignKey('rate_card.id'))
    rate_card = relationship(RateCard)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)


class BookingStatus(Base):
    __tablename__ = "booking_status"

    id = Column(String(2), primary_key=True, index=True)
    description = Column(String(50))


class PaymentType(Base):
    __tablename__ = "payment_type"

    id = Column(String(2), primary_key=True, index=True)
    description = Column(String(50))


class PaymentStatus(Base):
    __tablename__ = "payment_status"

    id = Column(String(2), primary_key=True, index=True)
    description = Column(String(50))


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type_id = Column(String(2), ForeignKey('payment_type.id'))
    type = relationship(PaymentType)
    status_id = Column(String(2), ForeignKey('payment_status.id'))
    status = relationship(PaymentStatus)
    ref_id = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey('machine.id'))
    machine = relationship(Machine)
    from_date = Column(DateTime)
    to_date = Column(DateTime)
    status_id = Column(String(2), ForeignKey('booking_status.id'))
    status = relationship(BookingStatus)
    payment_id = Column(Integer, ForeignKey('payments.id'))
    payment = relationship(Payment)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
