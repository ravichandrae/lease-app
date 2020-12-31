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
    db_machine = models.Machine(type_id=machine.type_id,
                                model_id=machine.model_id,
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
