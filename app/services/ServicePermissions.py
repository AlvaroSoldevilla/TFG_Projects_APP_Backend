from sqlmodel import Session

import app.repositories.RepositoryPermissions as rp
from app.schemas.Permission import PermissionCreate, PermissionUpdate


def get_all_permissions(session: Session):
    return rp.get_all_permissions(session)


def get_permission_by_id(permission_id: int, session: Session):
    return rp.get_permission_by_id(permission_id, session)


def create_permission(permission_data: PermissionCreate, session: Session):
    return rp.create_permission(permission_data, session)


def update_permission(permission_id: int, permission_update: PermissionUpdate, session: Session):
    return rp.update_permission(permission_id, permission_update, session)


def delete_permission(permission_id: int, session: Session):
    return rp.delete_permission(permission_id, session)
