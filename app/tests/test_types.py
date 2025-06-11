import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, MagicMock
from app.main import app
from app.routes.RouterTypes import jwt_scheme
from app.schemas.Type import TypeRead


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_get_all_types(mock_session, client):
    mock_session.return_value = MagicMock()
    type_ = TypeRead(id=1, name="Note")
    with patch("app.services.ServiceTypes.get_all_types", return_value=[type_]):
        response = await client.get("/types")
        assert response.status_code == 200
        assert response.json() == [type_.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_get_type_by_id_success(mock_session, client):
    mock_session.return_value = MagicMock()
    type_ = TypeRead(id=1, name="Arrow")
    with patch("app.services.ServiceTypes.get_type_by_id", return_value=type_):
        response = await client.get("/types/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Arrow"


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_get_type_by_id_not_found(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTypes.get_type_by_id", return_value=None):
        response = await client.get("/types/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_create_type_success(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {"name": "Table"}
    created = {**payload, "id": 1}
    with patch("app.services.ServiceTypes.create_type", return_value=created):
        response = await client.post("/types", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "Table"


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_create_type_failure(mock_session, client):
    mock_session.return_value = MagicMock()
    payload = {"name": "Invalid"}
    with patch("app.services.ServiceTypes.create_type", return_value=None):
        response = await client.post("/types", json=payload)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_update_type_success(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTypes.update_type", return_value=True):
        response = await client.patch("/types/1", json={"name": "UpdatedType"})
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_update_type_failure(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTypes.update_type", return_value=False):
        response = await client.patch("/types/1", json={"name": "UpdatedType"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_delete_type_success(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTypes.delete_type", return_value=True):
        response = await client.delete("/types/1")
        assert response.status_code == 200


@pytest.mark.asyncio
@patch("app.routes.RouterTypes.get_session")
async def test_delete_type_failure(mock_session, client):
    mock_session.return_value = MagicMock()
    with patch("app.services.ServiceTypes.delete_type", return_value=False):
        response = await client.delete("/types/1")
        assert response.status_code == 400
