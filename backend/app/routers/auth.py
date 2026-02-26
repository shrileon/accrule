from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get("/login/")
def login_jwt():
    return {"message": "Auth work"}


@router.get("/refresh/")
def refresh_jwt():
    return {"message": "Auth work"}