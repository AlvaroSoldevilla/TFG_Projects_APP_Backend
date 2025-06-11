from unittest.mock import patch, MagicMock

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.routes.RouterRoles import jwt_scheme
from app.main import app

from app.schemas.Role import RoleRead

# Replace with a valid token if needed
VALID_TOKEN = "test-token"


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

    print("Overrides:", app.dependency_overrides)
    app.dependency_overrides.clear()



@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_get_all_roles(mock_get_session, client):
    fake_role = RoleRead(id=1, name="Admin", description="Administrator")
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.get_all_roles", return_value=[fake_role]):
        response = await client.get("/roles")
        assert response.status_code == 200
        assert response.json() == [fake_role.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_get_role_by_id(mock_get_session, client):
    fake_role = RoleRead(id=2, name="Editor", description="Can edit")
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.get_role_by_id", return_value=fake_role):
        response = await client.get("/roles/2")
        assert response.status_code == 200
        assert response.json() == fake_role.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_create_role(mock_get_session, client):
    role_data = {"name": "Writer", "description": "Can write"}
    expected_role = {"id": 3, **role_data}
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.create_role", return_value=expected_role):
        response = await client.post("/roles", json=role_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Writer"


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_update_role(mock_get_session, client):
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.update_role", return_value=True):
        response = await client.patch("/roles/1", json={"description": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Role updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_delete_role(mock_get_session, client):
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.delete_role", return_value=True):
        response = await client.delete("/roles/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Role deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_get_role_by_id_fail(mock_get_session, client):
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.get_role_by_id", return_value=None):
        response = await client.get("/roles/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_update_role_fail(mock_get_session, client):
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.update_role", return_value=False):
        response = await client.patch("/roles/999", json={"description": "Updated"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterRoles.get_session")
async def test_delete_role_fail(mock_get_session, client):
    mock_session = MagicMock()
    mock_get_session.return_value = mock_session
    with patch("app.services.ServiceRoles.delete_role", return_value=False):
        response = await client.delete("/roles/999")
        assert response.status_code == 400