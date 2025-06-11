from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterProjectUsers import jwt_scheme
from app.schemas.ProjectUser import ProjectUserRead

@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_get_all_project_users(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_user = ProjectUserRead(id=1, id_user=1, id_project=2, id_role=3)
    with patch("app.services.ServiceProjectUsers.get_all_project_users", return_value=[fake_user]):
        response = await client.get("/project_users")
        assert response.status_code == 200
        assert response.json() == [fake_user.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_get_project_user_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_user = ProjectUserRead(id=1, id_user=1, id_project=2, id_role=3)
    with patch("app.services.ServiceProjectUsers.get_project_user_by_id", return_value=fake_user):
        response = await client.get("/project_users/1")
        assert response.status_code == 200
        assert response.json() == fake_user.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_get_project_user_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjectUsers.get_project_user_by_id", return_value=None):
        response = await client.get("/project_users/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_create_project_user(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    data = {"id_user": 1, "id_project": 2, "id_role": 3}
    expected = ProjectUserRead(id=1, **data)
    with patch("app.services.ServiceProjectUsers.create_project_user", return_value=expected):
        response = await client.post("/project_users", json=data)
        assert response.status_code == 200
        assert response.json()["id"] == 1


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_create_project_user_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    data = {"id_user": 1, "id_project": 2, "id_role": 3}
    with patch("app.services.ServiceProjectUsers.create_project_user", return_value=None):
        response = await client.post("/project_users", json=data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_update_project_user(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjectUsers.update_project_user", return_value=True):
        response = await client.patch("/project_users/1", json={"id_role": 4})
        assert response.status_code == 200
        assert response.json() == {"Message": "Project user updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_update_project_user_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjectUsers.update_project_user", return_value=False):
        response = await client.patch("/project_users/999", json={"id_role": 5})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_delete_project_user(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjectUsers.delete_project_user", return_value=True):
        response = await client.delete("/project_users/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Project user deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_delete_project_user_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceProjectUsers.delete_project_user", return_value=False):
        response = await client.delete("/project_users/999")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_get_project_users_by_user(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = ProjectUserRead(id=1, id_user=1, id_project=2, id_role=3)
    with patch("app.services.ServiceProjectUsers.get_project_user_by_user", return_value=[fake]):
        response = await client.get("/project_users/user/1")
        assert response.status_code == 200
        assert response.json() == [fake.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_get_project_users_by_project(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = ProjectUserRead(id=2, id_user=4, id_project=7, id_role=1)
    with patch("app.services.ServiceProjectUsers.get_project_user_by_project", return_value=[fake]):
        response = await client.get("/project_users/project/7")
        assert response.status_code == 200
        assert response.json() == [fake.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterProjectUsers.get_session")
async def test_get_project_user_by_project_and_user(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake = ProjectUserRead(id=3, id_user=5, id_project=9, id_role=2)
    with patch("app.services.ServiceProjectUsers.get_project_user_by_project_and_user", return_value=fake):
        response = await client.get("/project_users/project/9/user/5")
        assert response.status_code == 200
        assert response.json() == fake.model_dump()
