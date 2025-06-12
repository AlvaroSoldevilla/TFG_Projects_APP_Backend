from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Components(SQLModel, table=True):
    __tablename__ = "components"

    id:             int | None = Field(default=None, primary_key=True)
    id_board:       int | None = Field(default=None, foreign_key="concept_boards.id")
    id_parent:      int | None = None
    id_type:        int | None = Field(default=None, foreign_key="types.id")
    pos_x:          float | None = None
    pos_y:          float | None = None
    title:          str | None = None
    content:        str | None = None

    board:          Optional["ConceptBoards"] = Relationship(back_populates="components")
    type:           Optional["Types"] = Relationship(back_populates="components")
