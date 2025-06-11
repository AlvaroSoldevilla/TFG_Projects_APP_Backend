from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Priority import PriorityCreate, PriorityUpdate, PriorityRead
import app.services.ServicePriorities as sp

router = APIRouter(prefix="/priorities", tags=["Priorities"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[PriorityRead], status_code=200)
def get_all_priorities(session: Session = Depends(get_session)):
    return sp.get_all_priorities(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=PriorityRead, status_code=200)
def get_priority_by_id(id: int, session: Session = Depends(get_session)):
    priority = sp.get_priority_by_id(id, session)
    if priority is None:
        raise HTTPException(status_code=404, detail="Priority not found")
    else:
        return priority


@router.post("/", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=PriorityRead)
def create_priority(priority_data: PriorityCreate, session: Session = Depends(get_session)):
    priority = sp.create_priority(priority_data, session)
    if priority:
        return priority
    else:
        raise HTTPException(status_code=400, detail="Could not create priority")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_priority(id: int, priority_update: PriorityUpdate, session: Session = Depends(get_session)):
    if sp.update_priority(id, priority_update, session):
        return {"Message": "Priority updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update priority")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_priority(id: int, session: Session = Depends(get_session)):
    if sp.delete_priority(id, session):
        return {"Message": "Priority deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete priority")
