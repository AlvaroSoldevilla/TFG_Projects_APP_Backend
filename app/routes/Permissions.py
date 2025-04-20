from fastapi import APIRouter, HTTPException

from app.schemas.Permission import PermissionCreate, PermissionUpdate, PermissionRead
import app.services.ServicePermissions as sp

router = APIRouter(prefix="/permissions", tags=["Permissions"])


# Generic endpoints
@router.get("/", response_model=list[PermissionRead], status_code=200)
async def get_all_permissions():
    return sp.get_all_permissions()


@router.get("/{id}", response_model=PermissionRead, status_code=200)
async def get_permission_by_id(id: int):
    return sp.get_permission_by_id(id)


@router.post("/", status_code=200)
async def create_permission(permission_data: PermissionCreate):
    if sp.create_permission(permission_data):
        return {"Message": "Permission created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create permission")


@router.patch("/{id}", status_code=200)
async def update_permission(id: int, permission_update: PermissionUpdate):
    if sp.update_permission(id, permission_update):
        return {"Message": "Permission updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update permission")


@router.delete("/{id}", status_code=200)
async def delete_permission(id: int):
    if sp.delete_permission(id):
        return {"Message": "Permission deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete permission")
