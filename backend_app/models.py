from sqlalchemy import Column, Integer, String, Date

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    mobile = Column(String, unique=True, index=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    status_code = Column(String)
