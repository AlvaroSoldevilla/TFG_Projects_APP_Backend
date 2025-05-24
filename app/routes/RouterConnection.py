from fastapi import APIRouter


router = APIRouter(prefix="/connection", tags=["Connection"])


@router.get("/test", response_model=bool, status_code=200)
def test_connection():
    return True
