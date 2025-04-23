from fastapi import FastAPI
from app.routes import summarize, rewrite
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(summarize.router)
app.include_router(rewrite.router)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
