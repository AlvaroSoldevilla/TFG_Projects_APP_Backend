import app.repositories.RepositoryPriorities as rp
from app.schemas.Priority import PriorityCreate, PriorityUpdate


async def get_all_priorities():
    return rp.get_all_priorities()


async def get_priority_by_id(priority_id: int):
    return rp.get_priority_by_id(priority_id)


async def create_priority(priority_data: PriorityCreate):
    return rp.create_priority(priority_data)


async def update_priority(priority_id: int, priority_update: PriorityUpdate):
    return rp.update_priority(priority_id, priority_update)


async def delete_priority(priority_id: int):
    return rp.delete_priority(priority_id)
