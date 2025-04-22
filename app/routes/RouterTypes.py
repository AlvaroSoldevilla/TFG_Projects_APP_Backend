from fastapi import APIRouter, HTTPException

from app.schemas.Type import TypeCreate, TypeUpdate, TypeRead
import app.services.ServiceTypes as sc

router = APIRouter(prefix="/types", tags=["Types"])


# Generic endpoints
@router.get("/", response_model=list[TypeRead], status_code=200)
async def get_all_types():
    return await sc.get_all_types()


@router.get("/{id}", response_model=TypeRead, status_code=200)
async def get_type_by_id(id: int):
    return await sc.get_type_by_id(id)


@router.post("/", status_code=200)
async def create_type(type_data: TypeCreate):
    if await sc.create_type(type_data):
        return {"Message": "Type created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create type")


@router.patch("/{id}", status_code=200)
async def update_type(id: int, type_update: TypeUpdate):
    if await sc.update_type(id, type_update):
        return {"Message": "Type updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update type")


@router.delete("/{id}", status_code=200)
async def delete_type(id: int):
    if await sc.delete_type(id):
        return {"Message": "Type deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete type")