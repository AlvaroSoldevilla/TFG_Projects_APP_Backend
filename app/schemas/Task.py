from sqlmodel import SQLModel
from typing import Optional
from datetime import date


class TaskCreate(SQLModel):
    id_section:             int
    id_progress_section:    int | None
    id_user_created:        int
    title:                  str
    id_user_assigned:       int | None
    id_parent_task:         int | None
    id_priority:            int | None
    description:            str | None = ""
    progress:               int | None = 0
    creation_date:          Optional[date] | None = None
    limit_date:             Optional[date] | None = None
    completion_date:        Optional[date] | None = None
    finished:               bool | None = False
    is_parent:              bool | None = False


class TaskRead(TaskCreate):
    id:                     int


class TaskUpdate(SQLModel):
    id:                     int | None = None
    id_section:             int | None = None
    id_progress_section:    int | None = None
    id_user_assigned:       int | None = None
    id_parent_task:         int | None = None
    id_user_created:        int | None = None
    id_priority:            int | None = None
    title:                  str | None = None
    description:            str | None = None
    progress:               int | None = None
    limit_date:             Optional[date] | None = None
    completion_date:        Optional[date] | None = None
    finished:               bool | None = None
    is_parent:              bool | None = None
