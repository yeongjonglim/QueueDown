import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    joined_datetime = Column(DateTime,
                             default=datetime.datetime.utcnow,
                             nullable=False)
    last_login = Column(DateTime,
                        default=datetime.datetime.utcnow,
                        nullable=False)
