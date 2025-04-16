from sqlmodel import SQLModel


class ComponentCreate(SQLModel):
    id_board:   int
    id_type:    int
    title:      str

    id_parent:  int | None = None
    pos_x:      int | None = 0
    pos_y:      int | None = 0
    content:    str | None = ""


class ComponentRead(ComponentCreate):
    id:         int


class ComponentUpdate(SQLModel):
    id_board:   int | None = None
    id_type:    int | None = None
    title:      str | None = None

    id_parent:  int | None = None
    pos_x:      int | None = None
    pos_y:      int | None = None
    content:    str | None = None
