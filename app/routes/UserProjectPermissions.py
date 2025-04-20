from fastapi import APIRouter, HTTPException

from app.schemas.UserProjectPermission import UserProjectPermissionCreate, UserProjectPermissionUpdate, UserProjectPermissionRead
import app.services.ServiceUserProjectPermissions as supp

router = APIRouter(prefix="/user_project_permissions", tags=["User_Project_Permissions"])


# Generic endpoints
@router.get("/", response_model=list[UserProjectPermissionRead], status_code=200)
async def get_all_user_project_permissions():
    return supp.get_all_user_project_permissions()


@router.get("/{id}", response_model=UserProjectPermissionRead, status_code=200)
async def get_user_project_permission_by_id(id: int):
    return supp.get_user_project_permission_by_id(id)


@router.post("/", status_code=200)
async def create_user_project_permission(user_project_permission_data: UserProjectPermissionCreate):
    if supp.create_user_project_permission(user_project_permission_data):
        return {"Message": "User_Project_Permission created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create user_project_permission")


@router.patch("/{id}", status_code=200)
async def update_user_project_permission(id: int, user_project_permission_update: UserProjectPermissionUpdate):
    if supp.update_user_project_permission(id, user_project_permission_update):
        return {"Message": "User_Project_Permission updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update user_project_permission")


@router.delete("/{id}", status_code=200)
async def delete_user_project_permission(id: int):
    if supp.delete_user_project_permission(id):
        return {"Message": "User_Project_Permission deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete user_project_permission")


# Model Specific endpoints
@router.get("/user/{id}", response_model=list[UserProjectPermissionRead], status_code=200)
async def get_user_project_permissions_by_user(id_user: int):
    return supp.get_user_project_permissions_by_user(id_user)


@router.get("/project/{id}", response_model=list[UserProjectPermissionRead], status_code=200)
async def get_user_project_permissions_by_project(id_project: int):
    return supp.get_user_project_permissions_by_project(id_project)


@router.get("/permission/{id}", response_model=list[UserProjectPermissionRead], status_code=200)
async def get_user_project_permissions_by_permission(id_permission: int):
    return supp.get_user_project_permissions_by_permission(id_permission)


@router.get("/user/{id_user}/project/{id_project}", response_model=list[UserProjectPermissionRead], status_code=200)
async def get_user_project_permissions_by_user_and_project(id_user: int, id_project: int):
    return supp.get_user_project_permissions_by_user_and_project(id_user, id_project)
