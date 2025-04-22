from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Roles(SQLModel, table=True):
    __tablename__ = "roles"

    id:             int | None = Field(default=None, primary_key=True)
    name:           str | None = None
    description:    str | None = None

    project_users:  Optional[list["ProjectUsers"]] = Relationship(back_populates="role")
