from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TaskDependencies(SQLModel, table=True):
    id:                 int | None = Field(default=None, primary_key=True)
    id_task:            int | None = Field(default=None, foreign_key="tasks.id")
    id_depends_on:      int | None = Field(default=None, foreign_key="tasks.id")
    unlock_at:          int | None = 100

    task:               Optional["Tasks"] = Relationship(back_populates="dependencies")
    depends_on:         Optional["Tasks"] = Relationship(back_populates="dependents")
