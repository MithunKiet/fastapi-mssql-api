from typing import List, Dict, Any, Optional
from app.database import get_connection, rows_to_dicts

class UserRepository:
    TABLE = "Users"

    @staticmethod
    def fetch_all() -> List[Dict[str, Any]]:
        query = f"SELECT Id, UserName, Email FROM {UserRepository.TABLE} ORDER BY Id"
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows_to_dicts(cur, rows)

    @staticmethod
    def fetch_by_id(user_id: int) -> Optional[Dict[str, Any]]:
        query = f"SELECT Id, UserName, Email FROM {UserRepository.TABLE} WHERE Id = ?"
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(query, (user_id,))
            row = cur.fetchone()
            return rows_to_dicts(cur, [row])[0] if row else None

    @staticmethod
    def create(username: str, email: Optional[str]) -> int:
        # parameterized query to avoid SQL injection
        query = f"INSERT INTO {UserRepository.TABLE} (UserName, Email) VALUES (?, ?); SELECT SCOPE_IDENTITY()"
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(query, (username, email))
            # fetch identity
            new_id_row = cur.fetchone()
            # sometimes SCOPE_IDENTITY() returns decimal - cast to int
            new_id = int(new_id_row[0])
            return new_id
