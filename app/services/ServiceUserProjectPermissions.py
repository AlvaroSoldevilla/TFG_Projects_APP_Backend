from sqlmodel import Session

import app.repositories.RepositoryUserProjectPermissions as rupp
from app.schemas.UserProjectPermission import UserProjectPermissionCreate, UserProjectPermissionUpdate


def get_all_user_project_permissions(session: Session):
    return rupp.get_all_user_project_permissions(session)


def get_user_project_permission_by_id(user_project_permission_id: int, session: Session):
    return rupp.get_user_project_permission_by_id(user_project_permission_id, session)


def create_user_project_permission(user_project_permission_data: UserProjectPermissionCreate, session: Session):
    return rupp.create_user_project_permission(user_project_permission_data, session)


def update_user_project_permission(user_project_permission_id: int, user_project_permission_update: UserProjectPermissionUpdate, session: Session):
    return rupp.update_user_project_permission(user_project_permission_id, user_project_permission_update, session)


def delete_user_project_permission(user_project_permission_id: int, session: Session):
    return rupp.delete_user_project_permission(user_project_permission_id, session)


def get_user_project_permissions_by_user(id_user: int, session: Session):
    user_project_permissions = rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if user_project_permission.id_user == id_user]


def get_user_project_permissions_by_project(id_project: int, session: Session):
    user_project_permissions = rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if user_project_permission.id_project == id_project]


def get_user_project_permissions_by_permission(id_permission: int, session: Session):
    user_project_permissions = rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if user_project_permission.id_permission == id_permission]


def get_user_project_permissions_by_user_and_project(id_user: int, id_project: int, session: Session):
    user_project_permissions = rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if (user_project_permission.id_user == id_user and user_project_permission.id_project == id_project)]
