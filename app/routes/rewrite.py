import os
from fastapi import FastAPI, APIRouter, HTTPException 
from app.models.prompt import PromptRequest
from openai import OpenAI, OpenAIError
from app.services.openai_client import client
from app.utils.error_handler import handle_exceptions

router = APIRouter(prefix="/rewrite")

@router.post("/")
async def rewrite_text(req: PromptRequest):
    # strips whitespace, then checks prompt isnt empty
    if not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Please rewrite this more professionally:\n\n{req.prompt}"}],
            temperature=0.6,
        )
        return {"rewritten": response.choices[0].message.content}
    except Exception as e:
        raise handle_exceptions(e)