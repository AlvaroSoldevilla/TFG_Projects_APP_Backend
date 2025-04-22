import app.repositories.RepositoryPriorities as rp
from app.schemas.Priority import PriorityCreate, PriorityUpdate


async def get_all_priorities():
    return await rp.get_all_priorities()


async def get_priority_by_id(priority_id: int):
    return await rp.get_priority_by_id(priority_id)


async def create_priority(priority_data: PriorityCreate):
    return await rp.create_priority(priority_data)


async def update_priority(priority_id: int, priority_update: PriorityUpdate):
    return await rp.update_priority(priority_id, priority_update)


async def delete_priority(priority_id: int):
    return await rp.delete_priority(priority_id)
