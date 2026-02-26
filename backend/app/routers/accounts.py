from fastapi import APIRouter


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)

@router.get("/")
def test():
    return {"message": "Accounts work"}