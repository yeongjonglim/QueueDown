import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_class import Base


class Queue(Base):
    __tablename__ = "queue"

    id = Column(Integer, primary_key=True, index=True)
    mobile_number = Column(String, nullable=False)
    pax = Column(Integer, nullable=False)
    booking_datetime = Column(DateTime,
                              default=datetime.datetime.utcnow,
                              nullable=False)
    actual_entry = Column(DateTime)
    actual_exit = Column(DateTime)
