from fastapi import APIRouter


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.get("/")
def test():
    return {"message": "Transactions work"}