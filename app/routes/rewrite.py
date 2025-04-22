import os
from fastapi import FastAPI, APIRouter, HTTPException 
from app.models.prompt import PromptRequest
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Load .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

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
    except OpenAIError as e:
        raise HTTPException(status_code=502, detail="LLM service failed")
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Bad input")
    # fallback - catches any other exception and throws it as a 500 internal server error. JSON response returned with status code and detail message field
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))