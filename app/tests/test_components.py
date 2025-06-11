from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterComponents import jwt_scheme
from app.schemas.Component import ComponentRead


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_get_all_components(mock_get_session, client):
    fake_component = ComponentRead(
        id=1, id_board=1, id_type=1, title="Note",
        id_parent=None, pos_x=0.0, pos_y=0.0, content="Text"
    )
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.get_all_components", return_value=[fake_component]):
        response = await client.get("/components")
        assert response.status_code == 200
        assert response.json() == [fake_component.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_get_component_by_id(mock_get_session, client):
    fake_component = ComponentRead(
        id=2, id_board=1, id_type=2, title="Box",
        id_parent=None, pos_x=100.0, pos_y=150.0, content=None
    )
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.get_component_by_id", return_value=fake_component):
        response = await client.get("/components/2")
        assert response.status_code == 200
        assert response.json() == fake_component.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_get_component_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.get_component_by_id", return_value=None):
        response = await client.get("/components/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_create_component(mock_get_session, client):
    input_data = {
        "id_board": 1, "id_type": 1, "title": "Note",
        "id_parent": None, "pos_x": 0.0, "pos_y": 0.0, "content": "Text"
    }
    expected = ComponentRead(id=3, **input_data)

    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.create_component", return_value=expected):
        response = await client.post("/components", json=input_data)
        assert response.status_code == 200
        assert response.json()["id"] == 3
        assert response.json()["title"] == "Note"


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_create_component_fail(mock_get_session, client):
    input_data = {
        "id_board": 1, "id_type": 1, "title": "Note",
        "id_parent": None, "pos_x": 0.0, "pos_y": 0.0, "content": "Text"
    }
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.create_component", return_value=None):
        response = await client.post("/components", json=input_data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_update_component(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.update_component", return_value=True):
        response = await client.patch("/components/1", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Component updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_update_component_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.update_component", return_value=False):
        response = await client.patch("/components/999", json={"title": "Updated"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_delete_component(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.delete_component", return_value=True):
        response = await client.delete("/components/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Component deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_delete_component_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.delete_component", return_value=False):
        response = await client.delete("/components/999")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterComponents.get_session")
async def test_get_components_by_board(mock_get_session, client):
    fake_component = ComponentRead(
        id=4, id_board=2, id_type=3, title="Container",
        id_parent=None, pos_x=10.0, pos_y=20.0, content=""
    )
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceComponents.get_components_by_board", return_value=[fake_component]):
        response = await client.get("/components/board/2")
        assert response.status_code == 200
        assert response.json() == [fake_component.model_dump()]
