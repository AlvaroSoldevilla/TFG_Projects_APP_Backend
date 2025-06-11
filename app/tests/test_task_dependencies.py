
from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.routes.RouterTaskDependencies import jwt_scheme
from app.main import app
from app.schemas.TaskDependency import TaskDependencyRead

VALID_TOKEN = "dummy-token"

@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_get_all_task_dependencies(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = TaskDependencyRead(id=1, id_task=2, id_depends_on=3, unlock_at=50)
    with patch("app.services.ServiceTaskDependencies.get_all_task_dependencies", return_value=[fake]):
        res = await client.get("/task_dependencies")
        assert res.status_code == 200
        assert res.json() == [fake.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_get_task_dependency_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = TaskDependencyRead(id=2, id_task=5, id_depends_on=4, unlock_at=75)
    with patch("app.services.ServiceTaskDependencies.get_task_dependency_by_id", return_value=fake):
        res = await client.get("/task_dependencies/2")
        assert res.status_code == 200
        assert res.json() == fake.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_create_task_dependency(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    data = {"id_task": 10, "id_depends_on": 9, "unlock_at": 20}
    expected = {"id": 3, **data}
    with patch("app.services.ServiceTaskDependencies.create_task_dependency", return_value=expected):
        res = await client.post("/task_dependencies", json=data)
        assert res.status_code == 200
        assert res.json()["id_task"] == 10


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_update_task_dependency(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskDependencies.update_task_dependency", return_value=True):
        res = await client.patch("/task_dependencies/1", json={"unlock_at": 99})
        assert res.status_code == 200
        assert res.json() == {"Message": "Task dependency updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_delete_task_dependency(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskDependencies.delete_task_dependency", return_value=True):
        res = await client.delete("/task_dependencies/1")
        assert res.status_code == 200
        assert res.json() == {"Message": "Task dependency deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_get_task_dependency_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskDependencies.get_task_dependency_by_id", return_value=None):
        res = await client.get("/task_dependencies/999")
        assert res.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_update_task_dependency_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskDependencies.update_task_dependency", return_value=False):
        res = await client.patch("/task_dependencies/999", json={"unlock_at": 1})
        assert res.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskDependencies.get_session")
async def test_delete_task_dependency_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskDependencies.delete_task_dependency", return_value=False):
        res = await client.delete("/task_dependencies/999")
        assert res.status_code == 400
