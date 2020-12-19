from datetime import datetime
from typing import Optional, List, Union

from sqlalchemy.orm import Session
from sqlalchemy import Date, cast

from app.crud.base import CRUDBase
from app.models.queue import Queue
from app.schemas.queue import QueueCreate, QueueEntry, QueueExit


class CRUDQueue(CRUDBase[Queue, QueueCreate, Union[QueueEntry, QueueExit]]):
    def get_by_date(
        self,
        db: Session,
        *,
        d: Optional[datetime] = datetime.utcnow(),
        skip: int = 0,
        limit: int = 100,
    ) -> Optional[List[Queue]]:
        return db.query(Queue).filter(
            cast(Queue.booking_datetime, Date) == datetime.today().date()
        ).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: QueueCreate) -> Queue:
        db_obj = Queue(
            mobile_number=obj_in.mobile_number,
            pax=obj_in.pax,
            booking_datetime=obj_in.booking_datetime
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


queue = CRUDQueue(Queue)
