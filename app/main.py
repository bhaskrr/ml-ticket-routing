from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints import router

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1", tags=["v1"])

@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    """Helath check endpoint to verify if the API is running"""
    return {"status": "ok", "message": "API is running"}