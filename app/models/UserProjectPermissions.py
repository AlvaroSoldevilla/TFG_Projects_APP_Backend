from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class UserProjectPermissions(SQLModel, table=True):
    id:             int | None = Field(default=None, primary_key=True)
    id_permission:  int | None = Field(default=None, foreign_key="permissions.id")
    id_user:        int | None = Field(default=None, foreign_key="users.id")
    id_project:     int | None = Field(default=None, foreign_key="projects.id")

    permission:     Optional["Permissions"] = Relationship(back_populates="user_projects")
    user:           Optional["Users"] = Relationship(back_populates="project_permissions")
    project:        Optional["Projects"] = Relationship(back_populates="user_permissions")
