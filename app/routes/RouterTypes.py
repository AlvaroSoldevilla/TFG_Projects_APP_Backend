from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.Type import TypeCreate, TypeUpdate, TypeRead
import app.services.ServiceTypes as sc

router = APIRouter(prefix="/types", tags=["Types"])


# Generic endpoints
@router.get("/", response_model=list[TypeRead], status_code=200)
async def get_all_types(session: Session = Depends(get_session)):
    return await sc.get_all_types(session)


@router.get("/{id}", response_model=TypeRead, status_code=200)
async def get_type_by_id(id: int, session: Session = Depends(get_session)):
    return await sc.get_type_by_id(id, session)


@router.post("/", status_code=200)
async def create_type(type_data: TypeCreate, session: Session = Depends(get_session)):
    if await sc.create_type(type_data, session):
        return {"Message": "Type created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create type")


@router.patch("/{id}", status_code=200)
async def update_type(id: int, type_update: TypeUpdate, session: Session = Depends(get_session)):
    if await sc.update_type(id, type_update, session):
        return {"Message": "Type updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update type")


@router.delete("/{id}", status_code=200)
async def delete_type(id: int, session: Session = Depends(get_session)):
    if await sc.delete_type(id, session):
        return {"Message": "Type deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete type")