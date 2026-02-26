from fastapi import APIRouter


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/")
def test():
    return {"message": "Categories work"}