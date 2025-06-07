from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Permission import PermissionCreate, PermissionUpdate, PermissionRead
import app.services.ServicePermissions as sp

router = APIRouter(prefix="/permissions", tags=["Permissions"])


# Generic endpoints
@router.get("", dependencies=[Depends(JWTBearer())], response_model=list[PermissionRead], status_code=200)
def get_all_permissions(session: Session = Depends(get_session)):
    return sp.get_all_permissions(session)


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_model=PermissionRead, status_code=200)
def get_permission_by_id(id: int, session: Session = Depends(get_session)):
    return sp.get_permission_by_id(id, session)


@router.post("", dependencies=[Depends(JWTBearer())], status_code=200, response_model=PermissionRead)
def create_permission(permission_data: PermissionCreate, session: Session = Depends(get_session)):
    permission = sp.create_permission(permission_data, session)
    if permission:
        return permission
    else:
        raise HTTPException(status_code=400, detail="Could not create permission")


@router.patch("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def update_permission(id: int, permission_update: PermissionUpdate, session: Session = Depends(get_session)):
    if sp.update_permission(id, permission_update, session):
        return {"Message": "Permission updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update permission")


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def delete_permission(id: int, session: Session = Depends(get_session)):
    if sp.delete_permission(id, session):
        return {"Message": "Permission deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete permission")
