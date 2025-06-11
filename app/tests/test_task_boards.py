from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterTaskBoards import jwt_scheme
from app.schemas.TaskBoard import TaskBoardRead

@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_get_all_task_boards(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = TaskBoardRead(id=1, id_project=1, title="Sprint 1", description="First sprint")
    with patch("app.services.ServiceTaskBoards.get_all_task_boards", return_value=[fake]):
        response = await client.get("/task_boards")
        assert response.status_code == 200
        assert response.json() == [fake.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_get_task_board_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = TaskBoardRead(id=1, id_project=1, title="Sprint 1", description="First sprint")
    with patch("app.services.ServiceTaskBoards.get_task_board_by_id", return_value=fake):
        response = await client.get("/task_boards/1")
        assert response.status_code == 200
        assert response.json() == fake.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_get_task_board_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskBoards.get_task_board_by_id", return_value=None):
        response = await client.get("/task_boards/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_create_task_board(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    data = {"id_project": 1, "title": "New Board", "description": "Board description"}
    expected = TaskBoardRead(id=2, **data)
    with patch("app.services.ServiceTaskBoards.create_task_board", return_value=expected):
        response = await client.post("/task_boards", json=data)
        assert response.status_code == 200
        assert response.json()["id"] == 2


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_create_task_board_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    data = {"id_project": 1, "title": "Failing Board", "description": "x"}
    with patch("app.services.ServiceTaskBoards.create_task_board", return_value=None):
        response = await client.post("/task_boards", json=data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_update_task_board(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskBoards.update_task_board", return_value=True):
        response = await client.patch("/task_boards/1", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Task board updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_update_task_board_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskBoards.update_task_board", return_value=False):
        response = await client.patch("/task_boards/999", json={"title": "Fail"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_delete_task_board(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskBoards.delete_task_board", return_value=True):
        response = await client.delete("/task_boards/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Task board deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_delete_task_board_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceTaskBoards.delete_task_board", return_value=False):
        response = await client.delete("/task_boards/999")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTaskBoards.get_session")
async def test_get_task_boards_by_project(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = TaskBoardRead(id=1, id_project=1, title="Sprint X", description="Test sprint")
    with patch("app.services.ServiceTaskBoards.get_task_boards_by_project", return_value=[fake]):
        response = await client.get("/task_boards/project/1")
        assert response.status_code == 200
        assert response.json() == [fake.model_dump()]
