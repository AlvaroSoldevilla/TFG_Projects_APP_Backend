from sqlalchemy import select
from sqlmodel import Session

from app.models.ProjectUsers import ProjectUsers
from app.schemas.ProjectUser import ProjectUserCreate, ProjectUserUpdate


def get_all_project_users(session: Session):
    query = select(ProjectUsers)
    project_users = session.exec(query).scalars().all()

    return [ProjectUsers.model_validate(pu) for pu in project_users]


def get_project_user_by_id(project_user_id: int, session: Session):
    return session.get(ProjectUsers, project_user_id)


def create_project_user(project_user_data: ProjectUserCreate, session: Session):
    project_user = ProjectUsers(**project_user_data.model_dump())
    session.add(project_user)
    session.commit()
    session.refresh(project_user)

    return True


def update_project_user(project_user_id: int, project_user_update: ProjectUserUpdate, session: Session):
    project_user = session.get(ProjectUsers, project_user_id)

    if not project_user:
        return False

    for k, v in project_user_update.model_dump(exclude_unset=True).items():
        setattr(project_user, k, v)

    session.add(project_user)
    session.commit()
    session.refresh(project_user)

    return True


def delete_project_user(project_user_id: int, session: Session):
    project_user = session.get(ProjectUsers, project_user_id)

    if not project_user:
        return False

    session.delete(project_user)
    session.commit()

    return True

