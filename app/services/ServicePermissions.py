import app.repositories.RepositoryPermissions as rp
from app.schemas.Permission import PermissionCreate, PermissionUpdate


async def get_all_permissions():
    return await rp.get_all_permissions()


async def get_permission_by_id(permission_id: int):
    return await rp.get_permission_by_id(permission_id)


async def create_permission(permission_data: PermissionCreate):
    return await rp.create_permission(permission_data)


async def update_permission(permission_id: int, permission_update: PermissionUpdate):
    return await rp.update_permission(permission_id, permission_update)


async def delete_permission(permission_id: int):
    return await rp.delete_permission(permission_id)
