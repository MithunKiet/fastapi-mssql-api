from fastapi import APIRouter
from app.database import get_connection
from app.config import settings

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check():
    """API is alive check."""
    return {"status": "ok"}


@router.get("/db")
def database_check():
    """MSSQL connection test."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT GETDATE()")
            row = cursor.fetchone()
            return {"connected": True, "server_time": str(row[0])}
    except Exception as ex:
        return {"connected": False, "error": str(ex)}


@router.get("/info")
def app_info():
    """Return API version and environment details."""
    return {
        "app_name": "MSSQL API",
        "version": "1.0.0",
        "environment": settings.DB_AUTH,   # e.g., windows / sql
        "database": settings.DB_DATABASE,
        "server": settings.DB_SERVER,
    }
