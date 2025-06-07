from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.UserProjectPermission import UserProjectPermissionCreate, UserProjectPermissionUpdate, UserProjectPermissionRead
import app.services.ServiceUserProjectPermissions as supp

router = APIRouter(prefix="/user_project_permissions", tags=["User_Project_Permissions"])


# Generic endpoints
@router.get("", dependencies=[Depends(JWTBearer())], response_model=list[UserProjectPermissionRead], status_code=200)
def get_all_user_project_permissions(session: Session = Depends(get_session)):
    return supp.get_all_user_project_permissions(session)


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_model=UserProjectPermissionRead, status_code=200)
def get_user_project_permission_by_id(id: int, session: Session = Depends(get_session)):
    return supp.get_user_project_permission_by_id(id, session)


@router.post("", dependencies=[Depends(JWTBearer())], status_code=200, response_model=UserProjectPermissionRead)
def create_user_project_permission(user_project_permission_data: UserProjectPermissionCreate, session: Session = Depends(get_session)):
    user_project_permission = supp.create_user_project_permission(user_project_permission_data, session)
    if user_project_permission:
        return user_project_permission
    else:
        raise HTTPException(status_code=400, detail="Could not create user_project_permission")


@router.patch("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def update_user_project_permission(id: int, user_project_permission_update: UserProjectPermissionUpdate, session: Session = Depends(get_session)):
    if supp.update_user_project_permission(id, user_project_permission_update, session):
        return {"Message": "User_Project_Permission updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update user_project_permission")


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def delete_user_project_permission(id: int, session: Session = Depends(get_session)):
    if supp.delete_user_project_permission(id, session):
        return {"Message": "User_Project_Permission deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete user_project_permission")


# Model Specific endpoints
@router.get("/user/{id}", dependencies=[Depends(JWTBearer())], response_model=list[UserProjectPermissionRead], status_code=200)
def get_user_project_permissions_by_user(id: int, session: Session = Depends(get_session)):
    return supp.get_user_project_permissions_by_user(id, session)


@router.get("/project/{id}", dependencies=[Depends(JWTBearer())], response_model=list[UserProjectPermissionRead], status_code=200)
def get_user_project_permissions_by_project(id: int, session: Session = Depends(get_session)):
    return supp.get_user_project_permissions_by_project(id, session)


@router.get("/permission/{id}", dependencies=[Depends(JWTBearer())], response_model=list[UserProjectPermissionRead], status_code=200)
def get_user_project_permissions_by_permission(id: int, session: Session = Depends(get_session)):
    return supp.get_user_project_permissions_by_permission(id, session)


@router.get("/user/{id_user}/project/{id_project}", dependencies=[Depends(JWTBearer())], response_model=list[UserProjectPermissionRead], status_code=200)
def get_user_project_permissions_by_user_and_project(id_user: int, id_project: int, session: Session = Depends(get_session)):
    return supp.get_user_project_permissions_by_user_and_project(id_user, id_project, session)
