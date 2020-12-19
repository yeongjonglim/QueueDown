from typing import Optional
from datetime import datetime

from pydantic import BaseModel


# Shared properties
class QueueBase(BaseModel):
    mobile_number: str
    pax: int
    booking_datetime: Optional[datetime] = datetime.utcnow()


# To register new customer
class QueueCreate(QueueBase):
    pass


# To register customer arrival
class QueueEntry(QueueBase):
    actual_entry: datetime


# To register customer departure
class QueueExit(QueueBase):
    actual_exit: datetime


class QueueInDBBase(QueueBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Basic properties in DB
class Queue(QueueInDBBase):
    pass


# All properties in DB
class QueueInDB(QueueInDBBase):
    actual_entry: Optional[datetime] = None
    actual_exit: Optional[datetime] = None
