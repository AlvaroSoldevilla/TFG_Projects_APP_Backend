from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TaskBoards(SQLModel, table=True):
    id:             int | None = Field(default=None, primary_key=True)
    id_project:     int | None = Field(default=None, foreign_key="project.id")
    title:          str | None = None
    description:    str | None = None

    project:        Optional["Projects"] = Relationship(back_populates="task_boards")
    task_sections:       Optional[list["TaskSections"]] = Relationship(back_populates="task_board")
