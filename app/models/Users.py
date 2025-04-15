from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Users(SQLModel, table=True):
    id:                     int | None = Field(default=None, primary_key=True)
    username:               str | None = None
    email:                  str | None = None
    password:               str | None = None

    project_permissions:    Optional[list["UserProjectPermissions"]] = Relationship(back_populates="user")
    projects:               Optional[list["ProjectUsers"]] = Relationship(back_populates="user")
    tasks_created:           Optional[list["Tasks"]] = Relationship(back_populates="user_created")
    tasks_assigned:          Optional[list["Tasks"]] = Relationship(back_populates="user_assigned")
