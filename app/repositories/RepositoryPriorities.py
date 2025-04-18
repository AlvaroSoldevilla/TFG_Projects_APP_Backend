from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Priorities import Priorities
from app.schemas.Priority import PriorityCreate, PriorityUpdate


async def get_all_priorities(session: Session = Depends(get_session())):
    query = select(Priorities)
    priorities = session.exec(query).scalar().all()

    return [Priorities.model_validate(p) for p in priorities]


async def get_priority_by_id(priority_id: int, session: Session = Depends(get_session())):
    return session.get(Priorities, priority_id)


async def create_priority(priority_data: PriorityCreate, session: Session = Depends(get_session())):
    priority = Priorities(**priority_data.model_dump())
    session.add(priority)
    session.commit()
    session.refresh(priority)

    return True


async def update_priority(priority_id: int, priority_update: PriorityUpdate, session: Session = Depends(get_session())):
    priority = session.get(Priorities, priority_id)

    if not priority:
        return False

    for k, v in priority_update.model_dump(exclude_unset=True).items():
        setattr(priority, k, v)

    session.add(priority)
    session.commit()
    session.refresh(priority)

    return True


async def delete_priority(priority_id: int, session: Session = Depends(get_session())):
    priority = session.get(Priorities, priority_id)

    if not priority:
        return False

    session.delete(priority)
    session.commit()

    return True
