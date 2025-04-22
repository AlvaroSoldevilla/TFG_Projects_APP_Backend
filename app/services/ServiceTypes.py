import app.repositories.RepositoryTypes as rt
from app.schemas.Type import TypeCreate, TypeUpdate


async def get_all_types():
    return await rt.get_all_types()


async def get_type_by_id(type_id: int):
    return await rt.get_type_by_id(type_id)


async def create_type(type_data: TypeCreate):
    return await rt.create_type(type_data)


async def update_type(type_id: int, type_update: TypeUpdate):
    return await rt.update_type(type_id, type_update)


async def delete_type(type_id: int):
    return await rt.delete_type(type_id)
