from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Types(SQLModel, table=True):
    __tablename__ = "types"

    id:             int | None = Field(default=None, primary_key=True)
    name:           str | None = None

    components:  Optional[list["Components"]] = Relationship(back_populates="type")
