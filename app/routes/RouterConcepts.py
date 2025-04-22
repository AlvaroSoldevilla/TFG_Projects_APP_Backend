from fastapi import APIRouter, HTTPException

from app.schemas.Concept import ConceptCreate, ConceptUpdate, ConceptRead
import app.services.ServiceConcepts as sc

router = APIRouter(prefix="/concepts", tags=["Concepts"])


# Generic endpoints
@router.get("/", response_model=list[ConceptRead], status_code=200)
async def get_all_concepts():
    return await sc.get_all_concepts()


@router.get("/{id}", response_model=ConceptRead, status_code=200)
async def get_concept_by_id(id: int):
    return await sc.get_concept_by_id(id)


@router.post("/", status_code=200)
async def create_concept(concept_data: ConceptCreate):
    if await sc.create_concept(concept_data):
        return {"Message": "Concept created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create concept")


@router.patch("/{id}", status_code=200)
async def update_concept(id: int, concept_update: ConceptUpdate):
    if await sc.update_concept(id, concept_update):
        return {"Message": "Concept updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update concept")


@router.delete("/{id}", status_code=200)
async def delete_concept(id: int):
    if await sc.delete_concept(id):
        return {"Message": "Concept deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete concept")


# Model Specific endpoints
@router.get("/project/{id}", response_model=list[ConceptRead], status_code=200)
async def get_concepts_by_project(id_project: int):
    return await sc.get_concept_boards_by_project(id_project)
