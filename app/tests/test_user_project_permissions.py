import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, MagicMock
from app.main import app
from app.schemas.UserProjectPermission import UserProjectPermissionRead


@pytest_asyncio.fixture
async def client():
    from app.routes.RouterUserProjectPermissions import jwt_scheme
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_all_user_project_permissions(mock_session, client):
    mock_session.return_value = MagicMock()
    mock_data = UserProjectPermissionRead(id=1, id_permission=1, id_user=1, id_project=1)
    with patch("app.services.ServiceUserProjectPermissions.get_all_user_project_permissions", return_value=[mock_data]):
        response = await client.get("/user_project_permissions")
        assert response.status_code == 200
        assert response.json() == [mock_data.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_user_project_permission_by_id(mock_session, client):
    mock_session.return_value = MagicMock()
    mock_data = UserProjectPermissionRead(id=1, id_permission=1, id_user=1, id_project=1)
    with patch("app.services.ServiceUserProjectPermissions.get_user_project_permission_by_id", return_value=mock_data):
        response = await client.get("/user_project_permissions/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_user_project_permission_by_id_not_found(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.get_user_project_permission_by_id", return_value=None):
        response = await client.get("/user_project_permissions/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_create_user_project_permission(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {"id_permission": 1, "id_user": 2, "id_project": 3}
    with patch("app.services.ServiceUserProjectPermissions.create_user_project_permission", return_value={**payload, "id": 10}):
        response = await client.post("/user_project_permissions", json=payload)
        assert response.status_code == 200
        assert response.json()["id"] == 10


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_create_user_project_permission_failure(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {"id_permission": 1, "id_user": 2, "id_project": 3}
    with patch("app.services.ServiceUserProjectPermissions.create_user_project_permission", return_value=None):
        response = await client.post("/user_project_permissions", json=payload)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_update_user_project_permission(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.update_user_project_permission", return_value=True):
        response = await client.patch("/user_project_permissions/1", json={"id_user": 99})
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_update_user_project_permission_failure(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.update_user_project_permission", return_value=False):
        response = await client.patch("/user_project_permissions/1", json={"id_user": 99})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_delete_user_project_permission(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.delete_user_project_permission", return_value=True):
        response = await client.delete("/user_project_permissions/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_delete_user_project_permission_failure(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.delete_user_project_permission", return_value=False):
        response = await client.delete("/user_project_permissions/1")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_by_user(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.get_user_project_permissions_by_user", return_value=[]):
        response = await client.get("/user_project_permissions/user/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_by_project(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.get_user_project_permissions_by_project", return_value=[]):
        response = await client.get("/user_project_permissions/project/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_by_permission(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.get_user_project_permissions_by_permission", return_value=[]):
        response = await client.get("/user_project_permissions/permission/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUserProjectPermissions.get_session")
async def test_get_by_user_and_project(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUserProjectPermissions.get_user_project_permissions_by_user_and_project", return_value=[]):
        response = await client.get("/user_project_permissions/user/1/project/2")
        assert response.status_code == 200
