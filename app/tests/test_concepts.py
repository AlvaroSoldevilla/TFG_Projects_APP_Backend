from unittest.mock import patch, MagicMock
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.routes.RouterConcepts import jwt_scheme
from app.schemas.Concept import ConceptRead


@pytest_asyncio.fixture
async def client():
    app.dependency_overrides[jwt_scheme] = lambda: True
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_get_all_concepts(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_concept = ConceptRead(id=1, id_project=1, id_first_board=1, title="Concept 1", description="Test")
    with patch("app.services.ServiceConcepts.get_all_concepts", return_value=[fake_concept]):
        response = await client.get("/concepts")
        assert response.status_code == 200
        assert response.json() == [fake_concept.model_dump()]


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_get_concept_by_id(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_concept = ConceptRead(id=2, id_project=1, id_first_board=2, title="Concept 2", description="")
    with patch("app.services.ServiceConcepts.get_concept_by_id", return_value=fake_concept):
        response = await client.get("/concepts/2")
        assert response.status_code == 200
        assert response.json() == fake_concept.model_dump()


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_get_concept_by_id_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.get_concept_by_id", return_value=None):
        response = await client.get("/concepts/999")
        assert response.status_code == 404


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_create_concept(mock_get_session, client):
    input_data = {
        "id_project": 1,
        "id_first_board": 1,
        "title": "Concept 3",
        "description": "Desc"
    }
    expected = ConceptRead(id=3, **input_data)
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.create_concept", return_value=expected):
        response = await client.post("/concepts", json=input_data)
        assert response.status_code == 200
        assert response.json()["id"] == 3


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_create_concept_fail(mock_get_session, client):
    input_data = {
        "id_project": 1,
        "id_first_board": 1,
        "title": "Failing Concept",
        "description": "Error"
    }
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.create_concept", return_value=None):
        response = await client.post("/concepts", json=input_data)
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_update_concept(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.update_concept", return_value=True):
        response = await client.patch("/concepts/1", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.json() == {"Message": "Concept updated"}


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_update_concept_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.update_concept", return_value=False):
        response = await client.patch("/concepts/999", json={"title": "Should Fail"})
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_delete_concept(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.delete_concept", return_value=True):
        response = await client.delete("/concepts/1")
        assert response.status_code == 200
        assert response.json() == {"Message": "Concept deleted"}


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_delete_concept_fail(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    with patch("app.services.ServiceConcepts.delete_concept", return_value=False):
        response = await client.delete("/concepts/999")
        assert response.status_code == 400


@pytest.mark.asyncio
@patch("app.routes.RouterConcepts.get_session")
async def test_get_concepts_by_project(mock_get_session, client):
    mock_get_session.return_value = MagicMock()
    fake_concept = ConceptRead(id=4, id_project=5, id_first_board=2, title="Concept Project", description="")
    with patch("app.services.ServiceConcepts.get_concept_boards_by_project", return_value=[fake_concept]):
        response = await client.get("/concepts/project/5")
        assert response.status_code == 200
        assert response.json() == [fake_concept.model_dump()]
