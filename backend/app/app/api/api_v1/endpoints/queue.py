from typing import Any, List, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Queue])
def read_today_queue(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve queue
    """
    qs = crud.queue.get_by_date(db=db, skip=skip, limit=limit)
    return qs


@router.get("/all", response_model=List[schemas.QueueInDB])
def read_queue(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve queue
    """
    qs = crud.queue.get_multi(db=db, skip=skip, limit=limit)
    return qs


@router.post("/", response_model=schemas.Queue)
def create_queue(
    *,
    db: Session = Depends(deps.get_db),
    queue_in: schemas.QueueCreate,
) -> Any:
    """
    Create new queue.
    """
    item = crud.queue.create(db=db, obj_in=queue_in)
    return item


@router.put("/{id}", response_model=schemas.Queue)
def update_queue(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: Union[schemas.QueueEntry, schemas.QueueExit, schemas.QueueCreate],
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a queue.
    """
    item = crud.queue.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.queue.update(db=db, db_obj=item, obj_in=obj_in)
    return item
