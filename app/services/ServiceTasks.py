from datetime import date
from sqlmodel import Session

import app.repositories.RepositoryTasks as rt
from app.schemas.Task import TaskCreate, TaskUpdate
from app.services.ServiceUsers import get_user_by_id


def get_all_tasks(session: Session):
    return rt.get_all_tasks(session)


def get_task_by_id(task_id: int, session: Session):
    return rt.get_task_by_id(task_id, session)


def create_task(task_data: TaskCreate, session: Session):
    task_data.creation_date = date.today()
    return rt.create_task(task_data, session)


def update_task(task_id: int, task_update: TaskUpdate, session: Session):
    db_task = rt.get_task_by_id(task_update.id, session)
    if task_update.progress == 100:
        if db_task.completion_date is None:
            task_update.completion_date = date.today()
            task_update.finished = True
    else:
        if db_task.completion_date is not None:
            task_update.completion_date = None
            task_update.finished = False

    children = rt.get_tasks_by_parent(task_id, session)
    print(children)
    if task_update.is_parent and len(children) == 0:
        print(children)
        print("---------------------------------------------------------")
        print("Task:", task_id, "is no longer a parent")
        task_update.is_parent = False

    return rt.update_task(task_id, task_update, session)


def delete_task(task_id: int, session: Session):
    return rt.delete_task(task_id, session)


def get_tasks_by_task_section(id_section: int, session: Session):
    tasks = get_all_tasks(session)
    return [task for task in tasks if task.id_section == id_section]


def get_tasks_by_task_progress(id_progress_section: int, session: Session):
    tasks = get_all_tasks(session)
    return [task for task in tasks if task.id_progress_section == id_progress_section]


def get_user_assigned_by_task_id(id_task: int, session: Session):
    task = get_task_by_id(id_task, session)
    return get_user_by_id(task.id_user_assigned, session)


def get_user_created_by_task_id(id_task: int, session: Session):
    task = get_task_by_id(id_task, session)
    return get_user_by_id(task.id_user_created, session)


def get_tasks_by_parent(task_id: int, session: Session):
    return rt.get_tasks_by_parent(task_id, session)
