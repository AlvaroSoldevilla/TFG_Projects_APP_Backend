import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, MagicMock
from app.main import app
from app.routes.RouterTasks import jwt_scheme
from app.schemas.Task import TaskRead
from app.schemas.User import UserRead
from pydantic import TypeAdapter
from datetime import date


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_all_tasks(mock_session, client):
    mock_session.return_value = MagicMock()
    task = TaskRead(id=1, id_section=1, id_progress_section=2, id_user_created=1, title="Task A",
                    id_user_assigned=None, id_parent_task=None, id_priority=None, description="desc",
                    progress=50, creation_date=date.today(), limit_date=None, completion_date=None,
                    finished=False, is_parent=False)
    with patch("app.services.ServiceTasks.get_all_tasks", return_value=[task]):
        response = await client.get("/tasks")
        assert response.status_code == 200
        expected = TypeAdapter(list[TaskRead]).dump_python([task], mode="json")
        assert response.json() == expected


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_task_by_id(mock_session, client):
    mock_session.return_value = MagicMock()
    task = TaskRead(id=1, id_section=1, id_progress_section=2, id_user_created=1, title="Task A",
                    id_user_assigned=None, id_parent_task=None, id_priority=None, description="desc",
                    progress=50, creation_date=date.today(), limit_date=None, completion_date=None,
                    finished=False, is_parent=False)
    with patch("app.services.ServiceTasks.get_task_by_id", return_value=task):
        response = await client.get("/tasks/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_task_by_id_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTasks.get_task_by_id", return_value=None):
        response = await client.get("/tasks/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_create_task(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {
        "id_section": 1,
        "id_progress_section": 2,
        "id_user_created": 1,
        "title": "New Task",
        "id_user_assigned": None,
        "id_parent_task": None,
        "id_priority": None,
        "description": "Test desc",
        "progress": 0,
        "creation_date": str(date.today()),
        "limit_date": None,
        "completion_date": None,
        "finished": False,
        "is_parent": False
    }
    returned = {**payload, "id": 1}
    with patch("app.services.ServiceTasks.create_task", return_value=returned):
        response = await client.post("/tasks", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "New Task"


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_create_task_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {
        "id_section": 1,
        "id_progress_section": 2,
        "id_user_created": 1,
        "title": "New Task",
        "id_user_assigned": None,
        "id_parent_task": None,
        "id_priority": None,
        "description": "Test desc",
        "progress": 0,
        "creation_date": str(date.today()),
        "limit_date": None,
        "completion_date": None,
        "finished": False,
        "is_parent": False
    }
    with patch("app.services.ServiceTasks.create_task", return_value=None):
        response = await client.post("/tasks", json=payload)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_update_task(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTasks.update_task", return_value=True):
        response = await client.patch("/tasks/1", json={"title": "Updated Title"})
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_update_task_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTasks.update_task", return_value=False):
        response = await client.patch("/tasks/1", json={"title": "Updated Title"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_delete_task(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTasks.delete_task", return_value=True):
        response = await client.delete("/tasks/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_delete_task_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTasks.delete_task", return_value=False):
        response = await client.delete("/tasks/1")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_tasks_by_section(mock_session, client):
    mock_session.return_value = MagicMock()
    task = TaskRead(id=1, id_section=2, id_progress_section=2, id_user_created=1, title="By Section",
                    id_user_assigned=None, id_parent_task=None, id_priority=None, description="",
                    progress=0, creation_date=None, limit_date=None, completion_date=None, finished=False, is_parent=False)
    with patch("app.services.ServiceTasks.get_tasks_by_task_section", return_value=[task]):
        response = await client.get("/tasks/section/2")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_tasks_by_progress(mock_session, client):
    mock_session.return_value = MagicMock()
    task = TaskRead(id=1, id_section=2, id_progress_section=3, id_user_created=1, title="By Progress",
                    id_user_assigned=None, id_parent_task=None, id_priority=None, description="",
                    progress=0, creation_date=None, limit_date=None, completion_date=None, finished=False, is_parent=False)
    with patch("app.services.ServiceTasks.get_tasks_by_task_progress", return_value=[task]):
        response = await client.get("/tasks/progress/3")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_tasks_by_parent(mock_session, client):
    mock_session.return_value = MagicMock()
    task = TaskRead(id=1, id_section=2, id_progress_section=3, id_user_created=1, title="Child",
                    id_user_assigned=None, id_parent_task=5, id_priority=None, description="",
                    progress=0, creation_date=None, limit_date=None, completion_date=None, finished=False, is_parent=False)
    with patch("app.services.ServiceTasks.get_tasks_by_parent", return_value=[task]):
        response = await client.get("/tasks/parent/5")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_user_created_task(mock_session, client):
    mock_session.return_value = MagicMock()
    user = UserRead(id=1, username="creator", email="x@example.com", full_name=None)
    with patch("app.services.ServiceTasks.get_user_created_by_task_id", return_value=user):
        response = await client.get("/tasks/user/created/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTasks.get_session")
async def test_get_user_assigned_to_task(mock_session, client):
    mock_session.return_value = MagicMock()
    user = UserRead(id=2, username="assignee", email="y@example.com", full_name=None)
    with patch("app.services.ServiceTasks.get_user_assigned_by_task_id", return_value=user):
        response = await client.get("/tasks/user/assigned/1")
        assert response.status_code == 200
