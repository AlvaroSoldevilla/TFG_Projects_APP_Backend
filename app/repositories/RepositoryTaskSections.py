from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.TaskSections import TaskSections
from app.schemas.TaskSection import TaskSectionCreate, TaskSectionUpdate


async def get_all_task_sections(session: Session = Depends(get_session())):
    query = select(TaskSections)
    task_sections = session.exec(query).scalar().all()

    return [TaskSections.model_validate(s) for s in task_sections]


async def get_task_section_by_id(task_section_id: int, session: Session = Depends(get_session())):
    return session.get(TaskSections, task_section_id)


async def create_task_section(task_section_data: TaskSectionCreate, session: Session = Depends(get_session())):
    task_section = TaskSections(**task_section_data.model_dump())
    session.add(task_section)
    session.commit()
    session.refresh(task_section)

    return True


async def update_task_section(task_section_id: int, task_section_update: TaskSectionUpdate, session: Session = Depends(get_session())):
    task_section = session.get(TaskSections, task_section_id)

    if not task_section:
        return False

    for k, v in task_section_update.model_dump(exclude_unset=True).items():
        setattr(task_section, k, v)

    session.add(task_section)
    session.commit()
    session.refresh(task_section)

    return True


async def delete_task_section(task_section_id: int, session: Session = Depends(get_session())):
    task_section = session.get(TaskSections, task_section_id)

    if not task_section:
        return False

    session.delete(task_section)
    session.commit()

    return True
