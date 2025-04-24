from sqlmodel import Session

import app.repositories.RepositoryPermissions as rp
from app.schemas.Permission import PermissionCreate, PermissionUpdate


async def get_all_permissions(session: Session):
    return await rp.get_all_permissions(session)


async def get_permission_by_id(permission_id: int, session: Session):
    return await rp.get_permission_by_id(permission_id, session)


async def create_permission(permission_data: PermissionCreate, session: Session):
    return await rp.create_permission(permission_data, session)


async def update_permission(permission_id: int, permission_update: PermissionUpdate, session: Session):
    return await rp.update_permission(permission_id, permission_update, session)


async def delete_permission(permission_id: int, session: Session):
    return await rp.delete_permission(permission_id, session)
