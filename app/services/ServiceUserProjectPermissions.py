from sqlmodel import Session

import app.repositories.RepositoryUserProjectPermissions as rupp
from app.schemas.UserProjectPermission import UserProjectPermissionCreate, UserProjectPermissionUpdate


async def get_all_user_project_permissions(session: Session):
    return await rupp.get_all_user_project_permissions(session)


async def get_user_project_permission_by_id(user_project_permission_id: int, session: Session):
    return await rupp.get_user_project_permission_by_id(user_project_permission_id, session)


async def create_user_project_permission(user_project_permission_data: UserProjectPermissionCreate, session: Session):
    return await rupp.create_user_project_permission(user_project_permission_data, session)


async def update_user_project_permission(user_project_permission_id: int, user_project_permission_update: UserProjectPermissionUpdate, session: Session):
    return await rupp.update_user_project_permission(user_project_permission_id, user_project_permission_update, session)


async def delete_user_project_permission(user_project_permission_id: int, session: Session):
    return await rupp.delete_user_project_permission(user_project_permission_id, session)


async def get_user_project_permissions_by_user(id_user: int, session: Session):
    user_project_permissions = await rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if user_project_permission.id_user == id_user]


async def get_user_project_permissions_by_project(id_project: int, session: Session):
    user_project_permissions = await rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if user_project_permission.id_project == id_project]


async def get_user_project_permissions_by_permission(id_permission: int, session: Session):
    user_project_permissions = await rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if user_project_permission.id_permission == id_permission]


async def get_user_project_permissions_by_user_and_project(id_user: int, id_project: int, session: Session):
    user_project_permissions = await rupp.get_all_user_project_permissions(session)
    return [user_project_permission for user_project_permission in user_project_permissions
            if (user_project_permission.id_user == id_user and user_project_permission.id_project == id_project)]
