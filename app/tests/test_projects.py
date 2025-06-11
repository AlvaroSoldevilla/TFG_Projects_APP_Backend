from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterProjects import jwt_scheme
from app.schemas.Project import ProjectRead

@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_get_all_projects(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_project = ProjectRead(id=1, title="TFG", description="My final project")
    with patch("app.services.ServiceProjects.get_all_projects", return_value=[fake_project]):
        response = await client.get("/projects")
        assert response.status_code == 200
        assert response.json() == [fake_project.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_get_project_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_project = ProjectRead(id=2, title="Side Project", description="A small tool")
    with patch("app.services.ServiceProjects.get_project_by_id", return_value=fake_project):
        response = await client.get("/projects/2")
        assert response.status_code == 200
        assert response.json() == fake_project.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_get_project_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.get_project_by_id", return_value=None):
        response = await client.get("/projects/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_create_project(mock_get_session, client):
    input_data = {
        "title": "New Project",
        "description": "With purpose"
    }
    expected = ProjectRead(id=3, **input_data)
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.create_project", return_value=expected):
        response = await client.post("/projects", json=input_data)
        assert response.status_code == 200
        assert response.json()["id"] == 3
        assert response.json()["title"] == "New Project"


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_create_project_fail(mock_get_session, client):
    input_data = {
        "title": "Invalid",
        "description": "This should fail"
    }
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.create_project", return_value=None):
        response = await client.post("/projects", json=input_data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_update_project(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.update_project", return_value=True):
        response = await client.patch("/projects/1", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Project updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_update_project_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.update_project", return_value=False):
        response = await client.patch("/projects/999", json={"title": "Fail"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_delete_project(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.delete_project", return_value=True):
        response = await client.delete("/projects/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Project deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_delete_project_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjects.delete_project", return_value=False):
        response = await client.delete("/projects/999")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterProjects.get_session")
async def test_get_projects_by_user(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_project = ProjectRead(id=4, title="Collab", description="Shared project")
    with patch("app.services.ServiceProjects.get_projects_by_user", return_value=[fake_project]):
        response = await client.get("/projects/user/1")
        assert response.status_code == 200
        assert response.json() == [fake_project.model_dump()]
