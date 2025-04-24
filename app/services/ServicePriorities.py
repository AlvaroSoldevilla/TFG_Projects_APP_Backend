from sqlmodel import Session

import app.repositories.RepositoryPriorities as rp
from app.schemas.Priority import PriorityCreate, PriorityUpdate


async def get_all_priorities(session: Session):
    return await rp.get_all_priorities(session)


async def get_priority_by_id(priority_id: int, session: Session):
    return await rp.get_priority_by_id(priority_id, session)


async def create_priority(priority_data: PriorityCreate, session: Session):
    return await rp.create_priority(priority_data, session)


async def update_priority(priority_id: int, priority_update: PriorityUpdate, session: Session):
    return await rp.update_priority(priority_id, priority_update, session)


async def delete_priority(priority_id: int, session: Session):
    return await rp.delete_priority(priority_id, session)
