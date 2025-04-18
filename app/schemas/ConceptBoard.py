from sqlmodel import SQLModel


class ConceptBoardCreate(SQLModel):
    id_concept:         int
    id_parent:          int | None


class ConceptBoardRead(ConceptBoardCreate):
    id:                 int


class ConceptBoardReadExtended(ConceptBoardRead):
    parent_board:       ConceptBoardRead
    children_board:     [ConceptBoardRead]


class ConceptBoardUpdate(SQLModel):
    id_concept:         int | None
    id_parent:          int | None
