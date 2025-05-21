from fastapi import FastAPI
from api.v1.endpoints import router

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["v1"])

@app.get("/")
def index():
    return {"message": "Hello, World!"}

