from sqlmodel import Session

import app.repositories.RepositoryTaskSections as rts
from app.schemas.TaskSection import TaskSectionCreate, TaskSectionUpdate


async def get_all_task_sections(session: Session):
    return await rts.get_all_task_sections(session)


async def get_task_section_by_id(task_section_id: int, session: Session):
    return await rts.get_task_section_by_id(task_section_id, session)


async def create_task_section(task_section_data: TaskSectionCreate, session: Session):
    return await rts.create_task_section(task_section_data, session)


async def update_task_section(task_section_id: int, task_section_update: TaskSectionUpdate, session: Session):
    return await rts.update_task_section(task_section_id, task_section_update, session)


async def delete_task_section(task_section_id: int, session: Session):
    return await rts.delete_task_section(task_section_id, session)


async def get_task_sections_by_task_board(id_board: int, session: Session):
    task_sections = await rts.get_all_task_sections(session)
    return [task_section for task_section in task_sections if task_section.id_board == id_board]
