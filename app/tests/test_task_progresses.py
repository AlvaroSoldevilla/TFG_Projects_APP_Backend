from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.routes.RouterTaskProgress import jwt_scheme
from app.main import app
from app.schemas.TaskProgress import TaskProgressRead

VALID_TOKEN = "test-token"


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_get_all_task_progress(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    mock_result = TaskProgressRead(id=1, id_section=1, title="Do stuff", modifies_progress=True, progress_value=50, order=1)
    with patch("app.services.ServiceTaskProgress.get_all_task_progress", return_value=[mock_result]):
        response = await client.get("/task_progress")
        assert response.status_code == 200
        assert response.json() == [mock_result.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_get_task_progress_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    mock_result = TaskProgressRead(id=1, id_section=1, title="Do stuff", modifies_progress=True, progress_value=50, order=1)
    with patch("app.services.ServiceTaskProgress.get_task_progress_by_id", return_value=mock_result):
        response = await client.get("/task_progress/1")
        assert response.status_code == 200
        assert response.json() == mock_result.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_get_task_progress_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskProgress.get_task_progress_by_id", return_value=None):
        response = await client.get("/task_progress/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_create_task_progress(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    payload = {
        "id_section": 1,
        "title": "Step A",
        "modifies_progress": True,
        "progress_value": 10,
        "order": 0
    }
    returned = {**payload, "id": 1}
    with patch("app.services.ServiceTaskProgress.create_task_progress", return_value=returned):
        response = await client.post("/task_progress", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "Step A"


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_create_task_progress_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    payload = {
        "id_section": 1,
        "title": "Step A",
        "modifies_progress": True,
        "progress_value": 10,
        "order": 0
    }
    with patch("app.services.ServiceTaskProgress.create_task_progress", return_value=None):
        response = await client.post("/task_progress", json=payload)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_update_task_progress(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskProgress.update_task_progress", return_value=True):
        response = await client.patch("/task_progress/1", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Task progress updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_update_task_progress_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskProgress.update_task_progress", return_value=False):
        response = await client.patch("/task_progress/1", json={"title": "Updated"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_delete_task_progress(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskProgress.delete_task_progress", return_value=True):
        response = await client.delete("/task_progress/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Task progress deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_delete_task_progress_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskProgress.delete_task_progress", return_value=False):
        response = await client.delete("/task_progress/1")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskProgress.get_session")
async def test_get_task_progress_by_task_section(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    result = TaskProgressRead(id=1, id_section=1, title="Task Step", modifies_progress=True, progress_value=25, order=0)
    with patch("app.services.ServiceTaskProgress.get_task_progress_by_task_section", return_value=[result]):
        response = await client.get("/task_progress/section/1")
        assert response.status_code == 200
        assert response.json() == [result.model_dump()]
