from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Components(SQLModel, table=True):
    __tablename__ = "components"

    id:             int | None = Field(default=None, primary_key=True)
    id_board:       int | None = Field(default=None, foreign_key="concept_boards.id", sa_column_kwargs={"ondelete": "CASCADE"})
    id_parent:      int | None = Field(default=None, foreign_key="components.id", sa_column_kwargs={"ondelete": "CASCADE"})
    id_type:        int | None = Field(default=None, foreign_key="types.id", sa_column_kwargs={"ondelete": "SET NULL"})
    pos_x:          int | None = None
    pos_y:          int | None = None
    title:          str | None = None
    content:        str | None = None

    board:          Optional["ConceptBoards"] = Relationship(back_populates="components")
    parent: Optional["Components"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "Components.id"},
    )
    children:       Optional[list["Components"]] = Relationship(back_populates="parent", cascade_delete=True)
    type:           Optional["Types"] = Relationship(back_populates="components")
