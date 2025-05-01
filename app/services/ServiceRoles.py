from sqlmodel import Session

import app.repositories.RepositoryRoles as rr
from app.schemas.Role import RoleCreate, RoleUpdate


def get_all_roles(session: Session):
    return rr.get_all_roles(session)


def get_role_by_id(role_id: int, session: Session):
    return rr.get_role_by_id(role_id, session)


def create_role(role_data: RoleCreate, session: Session):
    return rr.create_role(role_data, session)


def update_role(role_id: int, role_update: RoleUpdate, session: Session):
    return rr.update_role(role_id, role_update, session)


def delete_role(role_id: int, session: Session):
    return rr.delete_role(role_id, session)
