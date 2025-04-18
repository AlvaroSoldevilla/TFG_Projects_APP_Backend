from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TaskSections(SQLModel, table=True):
    id:                     int | None = Field(default=None, primary_key=True)
    id_board:               int | None = Field(default=None, foreign_key="task_boards.id")
    title:                  str | None = None

    task_board:             Optional["TaskBoards"] = Relationship(back_populates="task_sections")
    progress_sections:      Optional[list["TaskProgress"]] = Relationship(back_populates="task_section")
