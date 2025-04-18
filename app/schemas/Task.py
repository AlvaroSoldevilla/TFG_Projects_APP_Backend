from sqlmodel import SQLModel
from typing import Optional
from sqlalchemy import Date


class TaskCreate(SQLModel):
    id_section:             int
    id_progress_section:    int
    id_user_created:        int
    title:                  str
    id_user_assigned:       int | None
    id_parent_task:         int | None
    id_priority:            int | None
    description:            str | None = ""
    progress:               int | None = 0
    creation_date:          Optional[Date]
    limit_date:             Optional[Date]
    finished:               bool | None = False


class TaskRead(TaskCreate):
    id:                     int


class TaskUpdate(SQLModel):
    id_section:             int | None = None
    id_progress_section:    int | None = None
    id_user_assigned:       int | None = None
    id_parent_task:         int | None = None
    id_user_created:        int | None = None
    id_priority:            int | None = None
    title:                  str | None = None
    description:            str | None = None
    progress:               int | None = None
    limit_date:             Optional[Date]
    finished:               bool | None = None
