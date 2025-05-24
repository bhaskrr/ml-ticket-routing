from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints import router
from fastapi.exceptions import HTTPException, RequestValidationError
from utils.error_handlers import (
    validation_exception_handler,
    http_exception_handler,
    unhandled_exception_handler,
)

app = FastAPI()

# Register custom exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

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