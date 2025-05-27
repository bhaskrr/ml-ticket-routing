from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.utils.logger import get_logger

logger = get_logger(__name__)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Cusatom handler for validation errors.
    """
    logger.error(f"Validation error: {exc.errors()}")
    body = exc.body
    if isinstance(body, bytes):
        try:
            body = body.decode("utf-8")
        except Exception:
            body = str(body)

    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": body,
        }
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Custom handler for HTTP exceptions.
    """
    logger.error(f"HTTP error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail,}
    )

async def unhandled_exception_handler(request: Request, exc: Exception):
    """
    Custom handler for unhandled exceptions.
    """
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error."}
    )