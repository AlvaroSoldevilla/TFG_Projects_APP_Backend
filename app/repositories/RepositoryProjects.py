from sqlalchemy import select
from sqlmodel import Session

from app.models.Projects import Projects
from app.schemas.Project import ProjectCreate, ProjectUpdate


async def get_all_projects(session: Session):
    query = select(Projects)
    projects = session.exec(query).scalar().all()

    return [Projects.model_validate(p) for p in projects]


async def get_project_by_id(project_id: int, session: Session):
    return session.get(Projects, project_id)


async def create_project(project_data: ProjectCreate, session: Session):
    project = Projects(**project_data.model_dump())
    session.add(project)
    session.commit()
    session.refresh(project)

    return True


async def update_project(project_id: int, project_update: ProjectUpdate, session: Session):
    project = session.get(Projects, project_id)

    if not project:
        return False

    for k, v in project_update.model_dump(exclude_unset=True).items():
        setattr(project, k, v)

    session.add(project)
    session.commit()
    session.refresh(project)

    return True


async def delete_project(project_id: int, session: Session):
    project = session.get(Projects, project_id)

    if not project:
        return False

    session.delete(project)
    session.commit()

    return True
