import app.repositories.RepositoryTaskSections as rts
from app.schemas.TaskSection import TaskSectionCreate, TaskSectionUpdate


async def get_all_task_sections():
    return rts.get_all_task_sections()


async def get_task_section_by_id(task_section_id: int):
    return rts.get_task_section_by_id(task_section_id)


async def create_task_section(task_section_data: TaskSectionCreate):
    return rts.create_task_section(task_section_data)


async def update_task_section(task_section_id: int, task_section_update: TaskSectionUpdate):
    return rts.update_task_section(task_section_id, task_section_update)


async def delete_task_section(task_section_id: int):
    return rts.delete_task_section(task_section_id)


async def get_task_sections_by_task_board(id_board: int):
    task_sections = rts.get_all_task_sections()
    return [task_section for task_section in task_sections if task_section.id_board == id_board]
