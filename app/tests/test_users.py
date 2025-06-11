import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, MagicMock
from app.main import app
from app.schemas.User import UserRead


@pytest_asyncio.fixture
async def client():
    from app.routes.RouterUsers import jwt_scheme
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_get_all_users(mock_session, client):
    mock_session.return_value = MagicMock()
    mock_data = UserRead(id=1, username="test", email="test@example.com")
    with patch("app.services.ServiceUsers.get_all_users", return_value=[mock_data]):
        response = await client.get("/users")
        assert response.status_code == 200
        assert response.json() == [mock_data.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_get_user_by_id(mock_session, client):
    mock_session.return_value = MagicMock()
    user = UserRead(id=1, username="john", email="john@example.com")
    with patch("app.services.ServiceUsers.get_user_by_id", return_value=user):
        response = await client.get("/users/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_get_user_by_id_not_found(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.get_user_by_id", return_value=None):
        response = await client.get("/users/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_create_user(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {"username": "newuser", "email": "new@example.com", "password": "1234"}
    mock_result = UserRead(id=1, username="newuser", email="new@example.com")
    with patch("app.services.ServiceUsers.create_user", return_value=mock_result):
        response = await client.post("/users", json=payload)
        assert response.status_code == 200
        assert response.json()["id"] == 1


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_create_user_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {"username": "failuser", "email": "fail@example.com", "password": "1234"}
    with patch("app.services.ServiceUsers.create_user", return_value=None):
        response = await client.post("/users", json=payload)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_update_user_success(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.update_user", return_value=True):
        response = await client.patch("/users/1", json={"email": "updated@example.com"})
        assert response.status_code == 200
        assert response.json()["Message"] == "User updated"


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_update_user_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.update_user", return_value=False):
        response = await client.patch("/users/1", json={"email": "updated@example.com"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_delete_user_success(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.delete_user", return_value=True):
        response = await client.delete("/users/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_delete_user_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.delete_user", return_value=False):
        response = await client.delete("/users/1")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_get_users_by_project(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.get_users_by_project", return_value=[]):
        response = await client.get("/users/project/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_get_user_by_email_success(mock_session, client):
    mock_session.return_value = MagicMock()
    email_payload = {"email": "test@example.com"}
    mock_user = UserRead(id=5, username="testuser", email="test@example.com")
    with patch("app.services.ServiceUsers.get_user_by_email", return_value=mock_user):
        response = await client.post("/users/email", json=email_payload)
        assert response.status_code == 200
        assert response.json()["email"] == "test@example.com"


@pytest.mark.asyncio
@patch("app.routes.RouterUsers.get_session")
async def test_get_user_by_email_fail(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceUsers.get_user_by_email", return_value=None):
        response = await client.post("/users/email", json={"email": "none@example.com"})
        assert response.status_code == 400
