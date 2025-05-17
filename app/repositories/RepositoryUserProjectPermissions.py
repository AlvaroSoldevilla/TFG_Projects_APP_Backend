from sqlalchemy import select
from sqlmodel import Session

from app.models.UserProjectPermissions import UserProjectPermissions
from app.schemas.UserProjectPermission import UserProjectPermissionCreate, UserProjectPermissionUpdate


def get_all_user_project_permissions(session: Session):
    query = select(UserProjectPermissions)
    user_role_permissions = session.exec(query).scalars().all()

    return [UserProjectPermissions.model_validate(urp) for urp in user_role_permissions]


def get_user_project_permission_by_id(user_project_permission_id: int, session: Session):
    return session.get(UserProjectPermissions, user_project_permission_id)


def create_user_project_permission(user_project_permission_data: UserProjectPermissionCreate, session: Session):
    user_project_permission = UserProjectPermissions(**user_project_permission_data.model_dump())
    session.add(user_project_permission)
    session.commit()
    session.refresh(user_project_permission)

    return user_project_permission


def update_user_project_permission(user_project_permission_id: int, user_project_permission_update: UserProjectPermissionUpdate, session: Session):
    user_project_permission = session.get(UserProjectPermissions, user_project_permission_id)

    if not user_project_permission:
        return False

    for k, v in user_project_permission_update.model_dump(exclude_unset=True).items():
        setattr(user_project_permission, k, v)

    session.add(user_project_permission)
    session.commit()
    session.refresh(user_project_permission)

    return True


def delete_user_project_permission(user_project_permission_id: int, session: Session):
    user_project_permission = session.get(UserProjectPermissions, user_project_permission_id)

    if not user_project_permission:
        return False

    session.delete(user_project_permission)
    session.commit()

    return True
