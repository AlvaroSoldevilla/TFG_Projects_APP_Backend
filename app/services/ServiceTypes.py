from sqlmodel import Session

import app.repositories.RepositoryTypes as rt
from app.schemas.Type import TypeCreate, TypeUpdate


async def get_all_types(session: Session):
    return await rt.get_all_types(session)


async def get_type_by_id(type_id: int, session: Session):
    return await rt.get_type_by_id(type_id, session)


async def create_type(type_data: TypeCreate, session: Session):
    return await rt.create_type(type_data, session)


async def update_type(type_id: int, type_update: TypeUpdate, session: Session):
    return await rt.update_type(type_id, type_update, session)


async def delete_type(type_id: int, session: Session):
    return await rt.delete_type(type_id, session)
