from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Priorities(SQLModel, table=True):
    __tablename__ = "priorities"

    id:             int | None = Field(default=None, primary_key=True)
    name:           str

    tasks:          Optional[list["Tasks"]] = Relationship(back_populates="priority")
