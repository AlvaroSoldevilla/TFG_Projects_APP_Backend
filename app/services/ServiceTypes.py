from sqlmodel import Session

import app.repositories.RepositoryTypes as rt
from app.schemas.Type import TypeCreate, TypeUpdate


def get_all_types(session: Session):
    return rt.get_all_types(session)


def get_type_by_id(type_id: int, session: Session):
    return rt.get_type_by_id(type_id, session)


def create_type(type_data: TypeCreate, session: Session):
    return rt.create_type(type_data, session)


def update_type(type_id: int, type_update: TypeUpdate, session: Session):
    return rt.update_type(type_id, type_update, session)


def delete_type(type_id: int, session: Session):
    return rt.delete_type(type_id, session)
