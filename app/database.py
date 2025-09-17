import pyodbc
from contextlib import contextmanager
from app.config import settings
from typing import Iterator, List, Dict, Any

pyodbc.pooling = True


def _build_connection_string() -> str:
    # Windows Authentication only
    return (
        f"DRIVER={{{settings.DB_DRIVER}}};"
        f"SERVER={settings.DB_SERVER};"
        f"DATABASE={settings.DB_DATABASE};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )


@contextmanager
def get_connection() -> Iterator[pyodbc.Connection]:
    conn = pyodbc.connect(_build_connection_string(), autocommit=False)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def rows_to_dicts(cursor: pyodbc.Cursor, rows: List[pyodbc.Row]) -> List[Dict[str, Any]]:
    """Convert pyodbc rows to list of dictionaries."""
    if not rows:
        return []
    columns = [col[0] for col in cursor.description]
    result = []
    for row in rows:
        result.append({columns[i]: row[i] for i in range(len(columns))})
    return result
