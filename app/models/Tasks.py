from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Tasks(SQLModel, table=True):
    __tablename__ = "tasks"

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
    creation_date:          Optional[date] | None
    limit_date:             Optional[date] | None
    completion_date:        Optional[date] | None
    finished:               bool | None = False

    task_section:           Optional["TaskSections"] = Relationship(back_populates="tasks")
    progress_section:       Optional["TaskProgress"] = Relationship(back_populates="tasks")
    user_assigned:          Optional["Users"] = Relationship(
        back_populates="tasks_assigned",
        sa_relationship_kwargs={"foreign_keys": "[Tasks.id_user_assigned]"}
    )
    user_created:           Optional["Users"] = Relationship(
        back_populates="tasks_created",
        sa_relationship_kwargs={"foreign_keys": "[Tasks.id_user_created]"}
    )
    priority:               Optional["Priorities"] = Relationship(back_populates="tasks")
    dependencies:           list["TaskDependencies"] = Relationship(
        back_populates="task",
        sa_relationship_kwargs={"foreign_keys": "[TaskDependencies.id_task]"},
        cascade_delete=True
    )
    dependents:             list["TaskDependencies"] = Relationship(
        back_populates="depends_on",
        sa_relationship_kwargs={"foreign_keys": "[TaskDependencies.id_depends_on]"},
        cascade_delete=True
    )
