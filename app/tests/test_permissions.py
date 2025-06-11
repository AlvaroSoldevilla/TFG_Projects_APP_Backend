from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterPermissions import jwt_scheme
from app.schemas.Permission import PermissionRead

@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_get_all_permissions(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_permission = PermissionRead(id=1, name="read_tasks_boards")
    with patch("app.services.ServicePermissions.get_all_permissions", return_value=[fake_permission]):
        response = await client.get("/permissions")
        assert response.status_code == 200
        assert response.json() == [fake_permission.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_get_permission_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_permission = PermissionRead(id=2, name="create_components")
    with patch("app.services.ServicePermissions.get_permission_by_id", return_value=fake_permission):
        response = await client.get("/permissions/2")
        assert response.status_code == 200
        assert response.json() == fake_permission.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_get_permission_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.get_permission_by_id", return_value=None):
        response = await client.get("/permissions/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_create_permission(mock_get_session, client):
    input_data = {"name": "edit_tasks"}
    expected = PermissionRead(id=3, **input_data)
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.create_permission", return_value=expected):
        response = await client.post("/permissions", json=input_data)
        assert response.status_code == 200
        assert response.json()["id"] == 3
        assert response.json()["name"] == "edit_tasks"


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_create_permission_fail(mock_get_session, client):
    input_data = {"name": "invalid"}
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.create_permission", return_value=None):
        response = await client.post("/permissions", json=input_data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_update_permission(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.update_permission", return_value=True):
        response = await client.patch("/permissions/1", json={"name": "updated_name"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Permission updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_update_permission_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.update_permission", return_value=False):
        response = await client.patch("/permissions/999", json={"name": "fail"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_delete_permission(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.delete_permission", return_value=True):
        response = await client.delete("/permissions/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Permission deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterPermissions.get_session")
async def test_delete_permission_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServicePermissions.delete_permission", return_value=False):
        response = await client.delete("/permissions/999")
        assert response.status_code == 400
