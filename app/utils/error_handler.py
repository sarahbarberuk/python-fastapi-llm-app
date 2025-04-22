from fastapi import HTTPException
from openai import OpenAIError

def handle_exceptions(e: Exception):
    if isinstance(e, OpenAIError):
        return HTTPException(status_code=502, detail="LLM service failed")
    if isinstance(e, ValueError):
        return HTTPException(status_code=400, detail="Bad input")
    return HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
