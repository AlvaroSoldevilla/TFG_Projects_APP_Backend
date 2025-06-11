from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterConceptBoards import jwt_scheme
from app.schemas.ConceptBoard import ConceptBoardRead


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_get_all_concept_boards(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_board = ConceptBoardRead(id=1, id_concept=1, id_parent=None, name="Board 1")
    with patch("app.services.ServiceConceptBoards.get_all_concept_boards", return_value=[fake_board]):
        response = await client.get("/concept_boards")
        assert response.status_code == 200
        assert response.json() == [fake_board.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_get_concept_board_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_board = ConceptBoardRead(id=2, id_concept=1, id_parent=None, name="Board 2")
    with patch("app.services.ServiceConceptBoards.get_concept_board_by_id", return_value=fake_board):
        response = await client.get("/concept_boards/2")
        assert response.status_code == 200
        assert response.json() == fake_board.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_get_concept_board_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.get_concept_board_by_id", return_value=None):
        response = await client.get("/concept_boards/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_create_concept_board(mock_get_session, client):
    input_data = {"id_concept": 1, "id_parent": None, "name": "Board 3"}
    expected = ConceptBoardRead(id=3, **input_data)
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.create_concept_board", return_value=expected):
        response = await client.post("/concept_boards", json=input_data)
        assert response.status_code == 200
        assert response.json()["id"] == 3


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_create_concept_board_fail(mock_get_session, client):
    input_data = {"id_concept": 1, "id_parent": None, "name": "Board 4"}
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.create_concept_board", return_value=None):
        response = await client.post("/concept_boards", json=input_data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_update_concept_board(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.update_concept_board", return_value=True):
        response = await client.patch("/concept_boards/1", json={"name": "Updated Name"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Concept board updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_update_concept_board_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.update_concept_board", return_value=False):
        response = await client.patch("/concept_boards/999", json={"name": "Failing Update"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_delete_concept_board(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.delete_concept_board", return_value=True):
        response = await client.delete("/concept_boards/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Concept board deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_delete_concept_board_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConceptBoards.delete_concept_board", return_value=False):
        response = await client.delete("/concept_boards/999")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterConceptBoards.get_session")
async def test_get_concept_boards_by_concept(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_board = ConceptBoardRead(id=4, id_concept=2, id_parent=None, name="Board for Concept")
    with patch("app.services.ServiceConceptBoards.get_concept_boards_by_concept", return_value=[fake_board]):
        response = await client.get("/concept_boards/concept/2")
        assert response.status_code == 200
        assert response.json() == [fake_board.model_dump()]
