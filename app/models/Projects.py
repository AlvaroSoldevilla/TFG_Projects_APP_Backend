from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Projects(SQLModel, table=True):
    __tablename__ = "projects"

    id:                     int | None = Field(default=None, primary_key=True)
    title:                  str | None = None
    description:            str | None = None

    user_permissions:       Optional[list["UserProjectPermissions"]] = Relationship(back_populates="project", cascade_delete=True)
    users:                  Optional[list["ProjectUsers"]] = Relationship(back_populates="project", cascade_delete=True)
    concepts:               Optional[list["Concepts"]] = Relationship(back_populates="project", cascade_delete=True)
    task_boards:            Optional[list["TaskBoards"]] = Relationship(back_populates="project", cascade_delete=True)
