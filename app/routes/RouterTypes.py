from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Type import TypeCreate, TypeUpdate, TypeRead
import app.services.ServiceTypes as sc

router = APIRouter(prefix="/types", tags=["Types"])


# Generic endpoints
@router.get("", dependencies=[Depends(JWTBearer())], response_model=list[TypeRead], status_code=200)
def get_all_types(session: Session = Depends(get_session)):
    return sc.get_all_types(session)


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_model=TypeRead, status_code=200)
def get_type_by_id(id: int, session: Session = Depends(get_session)):
    return sc.get_type_by_id(id, session)


@router.post("", dependencies=[Depends(JWTBearer())], status_code=200, response_model=TypeRead)
def create_type(type_data: TypeCreate, session: Session = Depends(get_session)):
    type = sc.create_type(type_data, session)
    if type:
        return type
    else:
        raise HTTPException(status_code=400, detail="Could not create type")


@router.patch("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def update_type(id: int, type_update: TypeUpdate, session: Session = Depends(get_session)):
    if sc.update_type(id, type_update, session):
        return {"Message": "Type updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update type")


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def delete_type(id: int, session: Session = Depends(get_session)):
    if sc.delete_type(id, session):
        return {"Message": "Type deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete type")