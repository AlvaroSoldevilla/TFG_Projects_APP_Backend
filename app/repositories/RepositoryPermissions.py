from sqlalchemy import select
from sqlmodel import Session

from app.models.Permissions import Permissions
from app.schemas.Permission import PermissionCreate, PermissionUpdate


def get_all_permissions(session: Session):
    query = select(Permissions)
    permissions = session.exec(query).scalars().all()

    return [Permissions.model_validate(p) for p in permissions]


def get_permission_by_id(permission_id: int, session: Session):
    return session.get(Permissions, permission_id)


def create_permission(permission_data: PermissionCreate, session: Session):
    permission = Permissions(**permission_data.model_dump())
    session.add(permission)
    session.commit()
    session.refresh(permission)

    return permission


def update_permission(permission_id: int, permission_update: PermissionUpdate, session: Session):
    permission = session.get(Permissions, permission_id)

    if not permission:
        return False

    for k, v in permission_update.model_dump(exclude_unset=True).items():
        setattr(permission, k, v)

    session.add(permission)
    session.commit()
    session.refresh(permission)

    return True


def delete_permission(permission_id: int, session: Session):
    permission = session.get(Permissions, permission_id)

    if not permission:
        return False

    session.delete(permission)
    session.commit()

    return True
