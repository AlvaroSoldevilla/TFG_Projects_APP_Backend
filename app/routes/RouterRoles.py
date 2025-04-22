from fastapi import APIRouter, HTTPException

from app.schemas.Role import RoleCreate, RoleUpdate, RoleRead
import app.services.ServiceRoles as sr

router = APIRouter(prefix="/roles", tags=["Roles"])


# Generic endpoints
@router.get("/", response_model=list[RoleRead], status_code=200)
async def get_all_roles():
    return await sr.get_all_roles()


@router.get("/{id}", response_model=RoleRead, status_code=200)
async def get_role_by_id(id: int):
    return await sr.get_role_by_id(id)


@router.post("/", status_code=200)
async def create_role(role_data: RoleCreate):
    if await sr.create_role(role_data):
        return {"Message": "Role created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create role")


@router.patch("/{id}", status_code=200)
async def update_role(id: int, role_update: RoleUpdate):
    if await sr.update_role(id, role_update):
        return {"Message": "Role updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update role")


@router.delete("/{id}", status_code=200)
async def delete_role(id: int):
    if await sr.delete_role(id):
        return {"Message": "Role deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete role")
