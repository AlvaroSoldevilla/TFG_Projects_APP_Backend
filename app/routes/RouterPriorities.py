from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.Priority import PriorityCreate, PriorityUpdate, PriorityRead
import app.services.ServicePriorities as sp

router = APIRouter(prefix="/priorities", tags=["Priorities"])


# Generic endpoints
@router.get("/", response_model=list[PriorityRead], status_code=200)
def get_all_priorities(session: Session = Depends(get_session)):
    return sp.get_all_priorities(session)


@router.get("/{id}", response_model=PriorityRead, status_code=200)
def get_priority_by_id(id: int, session: Session = Depends(get_session)):
    return sp.get_priority_by_id(id, session)


@router.post("/", status_code=200)
def create_priority(priority_data: PriorityCreate, session: Session = Depends(get_session)):
    if sp.create_priority(priority_data, session):
        return {"Message": "Priority created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create priority")


@router.patch("/{id}", status_code=200)
def update_priority(id: int, priority_update: PriorityUpdate, session: Session = Depends(get_session)):
    if sp.update_priority(id, priority_update, session):
        return {"Message": "Priority updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update priority")


@router.delete("/{id}", status_code=200)
def delete_priority(id: int, session: Session = Depends(get_session)):
    if sp.delete_priority(id, session):
        return {"Message": "Priority deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete priority")
