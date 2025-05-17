from sqlalchemy import select
from sqlmodel import Session

from app.models.Priorities import Priorities
from app.schemas.Priority import PriorityCreate, PriorityUpdate, PriorityRead


def get_all_priorities(session: Session):
    query = select(Priorities)
    priorities = session.exec(query).scalars().all()

    return [PriorityRead.model_validate(p) for p in priorities]


def get_priority_by_id(priority_id: int, session: Session):
    return session.get(Priorities, priority_id)


def create_priority(priority_data: PriorityCreate, session: Session):
    priority = Priorities(**priority_data.model_dump())
    session.add(priority)
    session.commit()
    session.refresh(priority)

    return priority


def update_priority(priority_id: int, priority_update: PriorityUpdate, session: Session):
    priority = session.get(Priorities, priority_id)

    if not priority:
        return False

    for k, v in priority_update.model_dump(exclude_unset=True).items():
        setattr(priority, k, v)

    session.add(priority)
    session.commit()
    session.refresh(priority)

    return True


def delete_priority(priority_id: int, session: Session):
    priority = session.get(Priorities, priority_id)

    if not priority:
        return False

    session.delete(priority)
    session.commit()

    return True
