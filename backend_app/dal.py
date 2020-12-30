from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_mobile(db: Session, mobile: str):
    return db.query(models.User).filter(models.User.mobile == mobile).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(mobile=user.mobile, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_machine(db: Session, machine: schemas.Machine):
    db_machine = models.Machine(type=machine.type, rate_card=machine.rate_card, user=machine.user)
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine
