from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Permissions(SQLModel, table=True):
    __tablename__ = "permissions"

    id:             int | None = Field(default=None, primary_key=True)
    name:           str | None = None

    user_projects:  Optional[list["UserProjectPermissions"]] = Relationship(back_populates="permission")
