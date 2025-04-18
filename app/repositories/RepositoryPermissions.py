from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Permissions import Permissions
from app.schemas.Permission import PermissionCreate, PermissionUpdate


async def get_all_permissions(session: Session = Depends(get_session())):
    query = select(Permissions)
    permissions = session.exec(query).scalar().all()

    return [Permissions.model_validate(p) for p in permissions]


async def get_permission_by_id(permission_id: int, session: Session = Depends(get_session())):
    return session.get(Permissions, permission_id)


async def create_permission(permission_data: PermissionCreate, session: Session = Depends(get_session())):
    permission = Permissions(**permission_data.model_dump())
    session.add(permission)
    session.commit()
    session.refresh(permission)

    return True


async def update_permission(permission_id: int, permission_update: PermissionUpdate, session: Session = Depends(get_session())):
    permission = session.get(Permissions, permission_id)

    if not permission:
        return False

    for k, v in permission_update.model_dump(exclude_unset=True).items():
        setattr(permission, k, v)

    session.add(permission)
    session.commit()
    session.refresh(permission)

    return True


async def delete_permission(permission_id: int, session: Session = Depends(get_session())):
    permission = session.get(Permissions, permission_id)

    if not permission:
        return False

    session.delete(permission)
    session.commit()

    return True
