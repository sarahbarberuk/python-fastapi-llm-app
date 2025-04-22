from fastapi import FastAPI
from app.routes import summarize, rewrite

app = FastAPI()

# Include routers
app.include_router(summarize.router)
app.include_router(rewrite.router)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
