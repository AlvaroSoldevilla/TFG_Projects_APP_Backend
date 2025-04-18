from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Components(SQLModel, table=True):
    id:             int | None = Field(default=None, primary_key=True)
    id_board:       int | None = Field(default=None, foreign_key="concept_boards.id")
    id_parent:      int | None = Field(default=None, foreign_key="components.id")
    id_type:        int | None = Field(default=None, foreign_key="types.id")
    pos_x:          int | None = None
    pos_y:          int | None = None
    title:          str | None = None
    content:        str | None = None

    board:          Optional[list["ConceptBoards"]] = Relationship(back_populates="components")
    parent:         Optional["Components"] = Relationship(back_populates="children")
    children:       Optional[list["Components"]] = Relationship(back_populates="parent")
    type:           Optional["Types"] = Relationship(back_populates="components")
