from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TaskSections(SQLModel, table=True):
    __tablename__ = "task_sections"

    id:                     int | None = Field(default=None, primary_key=True)
    id_board:               int | None = Field(default=None, foreign_key="task_boards.id")
    title:                  str | None = None
    order:                  int | None = 0

    task_board:             Optional["TaskBoards"] = Relationship(back_populates="task_sections")
    progress_sections:      Optional[list["TaskProgress"]] = Relationship(back_populates="task_section", cascade_delete=True)
    tasks:                  Optional[list["Tasks"]] = Relationship(back_populates="task_section", cascade_delete=True)
