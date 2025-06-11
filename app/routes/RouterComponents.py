from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Component import ComponentCreate, ComponentUpdate, ComponentRead
import app.services.ServiceComponents as sc

router = APIRouter(prefix="/components", tags=["Components"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[ComponentRead], status_code=200)
def get_all_components(session: Session = Depends(get_session)):
    return sc.get_all_components(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=ComponentRead, status_code=200)
def get_component_by_id(id: int, session: Session = Depends(get_session)):
    component = sc.get_component_by_id(id, session)
    if component is None:
        raise HTTPException(status_code=404, detail="Component not found")
    else:
        return component


@router.post("", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=ComponentRead)
def create_component(component_data: ComponentCreate, session: Session = Depends(get_session)):
    component = sc.create_component(component_data, session)
    if component:
        return component
    else:
        raise HTTPException(status_code=400, detail="Could not create component")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_component(id: int, component_update: ComponentUpdate, session: Session = Depends(get_session)):
    if sc.update_component(id, component_update, session):
        return {"Message": "Component updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update component")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_component(id: int, session: Session = Depends(get_session)):
    if sc.delete_component(id, session):
        return {"Message": "Component deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete component")


# Model Specific endpoints
@router.get("/board/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[ComponentRead], status_code=200)
def get_components_by_board(id: int, session: Session = Depends(get_session)):
    return sc.get_components_by_board(id, session)
