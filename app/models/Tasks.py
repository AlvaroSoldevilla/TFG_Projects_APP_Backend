from sqlalchemy import Date
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Tasks(SQLModel, table=True):
    id:                     int | None = Field(default=None, primary_key=True)
    id_section:             int | None = Field(default=None, foreign_key="task_sections.id")
    id_progress_section:    int | None = Field(default=None, foreign_key="task_progress.id")
    id_user_assigned:       int | None = Field(default=None, foreign_key="users.id")
    id_parent_task:         int | None = Field(default=None, foreign_key="tasks.id")
    id_user_created:        int | None = Field(default=None, foreign_key="users.id")
    id_priority:            int | None = Field(default=None, foreign_key="priorities.id")
    title:                  str | None = None
    description:            str | None = None
    progress:               int | None = 0
    creation_date:          Optional[Date]
    limit_date:             Optional[Date]
    finished:               bool | None = False

    section:                Optional["TaskSections"] = Relationship(back_populates="tasks")
    progress_section:       Optional["TaskProgress"] = Relationship(back_populates="tasks")
    user_assigned:          Optional["Users"] = Relationship(back_populates="tasks_assigned")
    parent:                 Optional["Tasks"] = Relationship(back_populates="children")
    children:               Optional[list["Tasks"]] = Relationship(back_populates="parent")
    user_created:           Optional["Users"] = Relationship(back_populates="tasks_created")
    priority:               Optional["Priorities"] = Relationship(back_populates="tasks")
    dependencies:           Optional[list["TaskDependencies"]] = Relationship(back_populates="task")
    dependents:             Optional[list["TaskDependencies"]] = Relationship(back_populates="depends_on")
