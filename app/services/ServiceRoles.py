import app.repositories.RepositoryRoles as rr
from app.schemas.Role import RoleCreate, RoleUpdate


async def get_all_roles():
    return await rr.get_all_roles()


async def get_role_by_id(role_id: int):
    return await rr.get_role_by_id(role_id)


async def create_role(role_data: RoleCreate):
    return await rr.create_role(role_data)


async def update_role(role_id: int, role_update: RoleUpdate):
    return await rr.update_role(role_id, role_update)


async def delete_role(role_id: int):
    return await rr.delete_role(role_id)
