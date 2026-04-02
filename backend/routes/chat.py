from fastapi import APIRouter
from pydantic import BaseModel
from ai_engine import get_ai_response
from db import save_chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    reply = get_ai_response(req.message)

    save_chat(req.message, reply)

    return {
        "user": req.message,
        "ai": reply
    }
