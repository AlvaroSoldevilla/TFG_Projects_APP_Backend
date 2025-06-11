from unittest.mock import patch, MagicMock

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterTaskSections import jwt_scheme
from app.schemas.TaskSection import TaskSectionRead


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_get_all_task_sections(mock_session, client):
    mock_session.return_value = MagicMock()
    task_section = TaskSectionRead(id=1, id_board=1, title="Section A", id_default_progress=2, order=0)
    with patch("app.services.ServiceTaskSections.get_all_task_sections", return_value=[task_section]):
        response = await client.get("/task_sections")
        assert response.status_code == 200
        assert response.json() == [task_section.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_get_task_section_by_id(mock_session, client):
    mock_session.return_value = MagicMock()
    task_section = TaskSectionRead(id=1, id_board=1, title="Section A", id_default_progress=2, order=0)
    with patch("app.services.ServiceTaskSections.get_task_section_by_id", return_value=task_section):
        response = await client.get("/task_sections/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_get_task_section_by_id_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskSections.get_task_section_by_id", return_value=None):
        response = await client.get("/task_sections/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_create_task_section(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {
        "id_board": 1,
        "title": "New Section",
        "id_default_progress": 2,
        "order": 0
    }
    returned = {**payload, "id": 1}
    with patch("app.services.ServiceTaskSections.create_task_section", return_value=returned):
        response = await client.post("/task_sections", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "New Section"


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_create_task_section_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {
        "id_board": 1,
        "title": "New Section",
        "id_default_progress": 2,
        "order": 0
    }
    with patch("app.services.ServiceTaskSections.create_task_section", return_value=None):
        response = await client.post("/task_sections", json=payload)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_update_task_section(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskSections.update_task_section", return_value=True):
        response = await client.patch("/task_sections/1", json={"title": "Updated Title"})
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_update_task_section_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskSections.update_task_section", return_value=False):
        response = await client.patch("/task_sections/1", json={"title": "Updated Title"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_delete_task_section(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskSections.delete_task_section", return_value=True):
        response = await client.delete("/task_sections/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_delete_task_section_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskSections.delete_task_section", return_value=False):
        response = await client.delete("/task_sections/1")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskSections.get_session")
async def test_get_task_sections_by_task_board(mock_session, client):
    mock_session.return_value = MagicMock()
    task_section = TaskSectionRead(id=1, id_board=3, title="Board Section", id_default_progress=2, order=0)
    with patch("app.services.ServiceTaskSections.get_task_sections_by_task_board", return_value=[task_section]):
        response = await client.get("/task_sections/board/3")
        assert response.status_code == 200
        assert response.json()[0]["id_board"] == 3
