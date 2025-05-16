from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.Role import RoleCreate, RoleUpdate, RoleRead
import app.services.ServiceRoles as sr

router = APIRouter(prefix="/roles", tags=["Roles"])


# Generic endpoints
@router.get("/", response_model=list[RoleRead], status_code=200)
def get_all_roles(session: Session = Depends(get_session)):
    return sr.get_all_roles(session)


@router.get("/{id}", response_model=RoleRead, status_code=200)
def get_role_by_id(id: int, session: Session = Depends(get_session)):
    return sr.get_role_by_id(id, session)


@router.post("/", status_code=200, response_model=RoleRead)
def create_role(role_data: RoleCreate, session: Session = Depends(get_session)):
    role = sr.create_role(role_data, session)
    if role:
        return role
    else:
        raise HTTPException(status_code=400, detail="Could not create role")


@router.patch("/{id}", status_code=200)
def update_role(id: int, role_update: RoleUpdate, session: Session = Depends(get_session)):
    if sr.update_role(id, role_update, session):
        return {"Message": "Role updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update role")


@router.delete("/{id}", status_code=200)
def delete_role(id: int, session: Session = Depends(get_session)):
    if sr.delete_role(id, session):
        return {"Message": "Role deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete role")
