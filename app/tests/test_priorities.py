from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterPriorities import jwt_scheme
from app.schemas.Priority import PriorityRead

@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_get_all_priorities(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_priority = PriorityRead(id=1, name="High", color="#FF0000", priority_value=10)
    with patch("app.services.ServicePriorities.get_all_priorities", return_value=[fake_priority]):
        response = await client.get("/priorities")
        assert response.status_code == 200
        assert response.json() == [fake_priority.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_get_priority_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_priority = PriorityRead(id=2, name="Medium", color="#FFA500", priority_value=5)
    with patch("app.services.ServicePriorities.get_priority_by_id", return_value=fake_priority):
        response = await client.get("/priorities/2")
        assert response.status_code == 200
        assert response.json() == fake_priority.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_get_priority_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.get_priority_by_id", return_value=None):
        response = await client.get("/priorities/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_create_priority(mock_get_session, client):
    input_data = {
        "name": "Low",
        "color": "#00FF00",
        "priority_value": 1
    }
    expected = PriorityRead(id=3, **input_data)
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.create_priority", return_value=expected):
        response = await client.post("/priorities/", json=input_data)
        assert response.status_code == 200
        assert response.json()["id"] == 3
        assert response.json()["name"] == "Low"


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_create_priority_fail(mock_get_session, client):
    input_data = {
        "name": "Invalid",
        "color": "#000000",
        "priority_value": 0
    }
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.create_priority", return_value=None):
        response = await client.post("/priorities/", json=input_data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_update_priority(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.update_priority", return_value=True):
        response = await client.patch("/priorities/1", json={"name": "Critical"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Priority updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_update_priority_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.update_priority", return_value=False):
        response = await client.patch("/priorities/999", json={"name": "Broken"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_delete_priority(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.delete_priority", return_value=True):
        response = await client.delete("/priorities/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Priority deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterPriorities.get_session")
async def test_delete_priority_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePriorities.delete_priority", return_value=False):
        response = await client.delete("/priorities/999")
        assert response.status_code == 400
