from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TaskProgress(SQLModel, table=True):
    __tablename__ = "task_progress"

    id:                     int | None = Field(default=None, primary_key=True)
    id_section:             int | None = Field(default=None, foreign_key="task_sections.id")
    title:                  str | None = None
    modifies_progress:      bool | None = False
    progress_value:         int | None = 0

    task_section:           Optional["TaskSections"] = Relationship(back_populates="progress_sections")
    tasks:                  Optional[list["Tasks"]] = Relationship(back_populates="progress_section")
