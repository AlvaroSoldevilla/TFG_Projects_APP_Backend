from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class ProjectUsers(SQLModel, table=True):
    __tablename__ = "project_users"

    id:             int | None = Field(default=None, primary_key=True)
    id_user:        int | None = Field(default=None, foreign_key="users.id", sa_column_kwargs={"ondelete": "CASCADE"})
    id_project:     int | None = Field(default=None, foreign_key="projects.id", sa_column_kwargs={"ondelete": "CASCADE"})
    id_role:        int | None = Field(default=0, foreign_key="roles.id", sa_column_kwargs={"ondelete": "SET NULL"})

    user:           Optional["Users"] = Relationship(back_populates="projects")
    project:        Optional["Projects"] = Relationship(back_populates="users")
    role:           Optional["Roles"] = Relationship(back_populates="project_users")
