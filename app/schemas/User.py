from sqlmodel import SQLModel


class UserCreate(SQLModel):
    password:   str
    username:   str | None = None
    email:      str | None = None


class UserRead(UserCreate):
    id:         int


class UserUpdate(SQLModel):
    username:   str | None = None
    email:      str | None = None
    password:   str | None = None


class UserAuthenticate(SQLModel):
    password:   str
    username:   str
    email:      str
