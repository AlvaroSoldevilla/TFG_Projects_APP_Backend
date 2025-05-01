from sqlmodel import Session

import app.repositories.RepositoryPriorities as rp
from app.schemas.Priority import PriorityCreate, PriorityUpdate


def get_all_priorities(session: Session):
    return rp.get_all_priorities(session)


def get_priority_by_id(priority_id: int, session: Session):
    return rp.get_priority_by_id(priority_id, session)


def create_priority(priority_data: PriorityCreate, session: Session):
    return rp.create_priority(priority_data, session)


def update_priority(priority_id: int, priority_update: PriorityUpdate, session: Session):
    return rp.update_priority(priority_id, priority_update, session)


def delete_priority(priority_id: int, session: Session):
    return rp.delete_priority(priority_id, session)
