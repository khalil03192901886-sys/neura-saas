from fastapi import APIRouter
from database import create_user, verify_user
from auth import create_token

router = APIRouter()

@router.post("/register")
def register(data: dict):
    ok = create_user(data["username"], data["password"])
    return {"success": ok}

@router.post("/login")
def login(data: dict):
    user = verify_user(data["username"], data["password"])

    if user:
        token = create_token({"user": data["username"]})
        return {"token": token}

    return {"error": "Invalid credentials"}
