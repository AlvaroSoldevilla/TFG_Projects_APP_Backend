from sqlmodel import Session

import app.repositories.RepositoryRoles as rr
from app.schemas.Role import RoleCreate, RoleUpdate


async def get_all_roles(session: Session):
    return await rr.get_all_roles(session)


async def get_role_by_id(role_id: int, session: Session):
    return await rr.get_role_by_id(role_id, session)


async def create_role(role_data: RoleCreate, session: Session):
    return await rr.create_role(role_data, session)


async def update_role(role_id: int, role_update: RoleUpdate, session: Session):
    return await rr.update_role(role_id, role_update, session)


async def delete_role(role_id: int, session: Session):
    return await rr.delete_role(role_id, session)
