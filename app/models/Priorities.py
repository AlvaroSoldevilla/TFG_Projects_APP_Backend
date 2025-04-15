from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Priorities(SQLModel, table=True):
    id:             int | None = Field(default=None, primary_key=True)
    name:           str | None = None

    tasks:  Optional[list["Tasks"]] = Relationship(back_populates="priority")
