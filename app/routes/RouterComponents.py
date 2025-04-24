from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.Component import ComponentCreate, ComponentUpdate, ComponentRead
import app.services.ServiceComponents as sc

router = APIRouter(prefix="/components", tags=["Components"])


# Generic endpoints
@router.get("/", response_model=list[ComponentRead], status_code=200)
async def get_all_components(session: Session = Depends(get_session)):
    return await sc.get_all_components(session)


@router.get("/{id}", response_model=ComponentRead, status_code=200)
async def get_component_by_id(id: int, session: Session = Depends(get_session)):
    return await sc.get_component_by_id(id, session)


@router.post("/", status_code=200)
async def create_component(component_data: ComponentCreate, session: Session = Depends(get_session)):
    if await sc.create_component(component_data, session):
        return {"Message": "Component created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create component")


@router.patch("/{id}", status_code=200)
async def update_component(id: int, component_update: ComponentUpdate, session: Session = Depends(get_session)):
    if await sc.update_component(id, component_update, session):
        return {"Message": "Component updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update component")


@router.delete("/{id}", status_code=200)
async def delete_component(id: int, session: Session = Depends(get_session)):
    if await sc.delete_component(id, session):
        return {"Message": "Component deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete component")


# Model Specific endpoints
@router.get("/board/{id}", response_model=list[ComponentRead], status_code=200)
async def get_components_by_board(id_board: int, session: Session = Depends(get_session)):
    return await sc.get_components_by_board(id_board, session)
