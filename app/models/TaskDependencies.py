from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class TaskDependencies(SQLModel, table=True):
    __tablename__ = "task_dependencies"

    id:                 int | None = Field(default=None, primary_key=True)
    id_task:            int | None = Field(default=None, foreign_key="tasks.id", sa_column_kwargs={"ondelete": "CASCADE"})
    id_depends_on:      int | None = Field(default=None, foreign_key="tasks.id", sa_column_kwargs={"ondelete": "CASCADE"})
    unlock_at:          int | None = 100

    task:               Optional["Tasks"] = Relationship(
        back_populates="dependencies",
        sa_relationship_kwargs={"foreign_keys": "[TaskDependencies.id_task]"}
    )

    depends_on:         Optional["Tasks"] = Relationship(
        back_populates="dependents",
        sa_relationship_kwargs={"foreign_keys": "[TaskDependencies.id_depends_on]"}
    )
