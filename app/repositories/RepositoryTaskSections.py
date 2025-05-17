from sqlalchemy import select
from sqlmodel import Session

from app.models.TaskSections import TaskSections
from app.schemas.TaskSection import TaskSectionCreate, TaskSectionUpdate


def get_all_task_sections(session: Session):
    query = select(TaskSections)
    task_sections = session.exec(query).scalars().all()

    return [TaskSections.model_validate(s) for s in task_sections]


def get_task_section_by_id(task_section_id: int, session: Session):
    return session.get(TaskSections, task_section_id)


def create_task_section(task_section_data: TaskSectionCreate, session: Session):
    task_section = TaskSections(**task_section_data.model_dump())
    session.add(task_section)
    session.commit()
    session.refresh(task_section)

    return task_section


def update_task_section(task_section_id: int, task_section_update: TaskSectionUpdate, session: Session):
    task_section = session.get(TaskSections, task_section_id)

    if not task_section:
        return False

    for k, v in task_section_update.model_dump(exclude_unset=True).items():
        setattr(task_section, k, v)

    session.add(task_section)
    session.commit()
    session.refresh(task_section)

    return True


def delete_task_section(task_section_id: int, session: Session):
    task_section = session.get(TaskSections, task_section_id)

    if not task_section:
        return False

    session.delete(task_section)
    session.commit()

    return True
