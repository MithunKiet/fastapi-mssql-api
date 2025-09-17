from typing import List
from app.models.user_models import UserCreate, UserOut
from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def list_users() -> List[UserOut]:
        rows = UserRepository.fetch_all()
        return [UserOut(id=r["Id"], username=r["UserName"], email=r.get("Email")) for r in rows]

    @staticmethod
    def get_user(user_id: int) -> UserOut | None:
        row = UserRepository.fetch_by_id(user_id)
        if not row:
            return None
        return UserOut(id=row["Id"], username=row["UserName"], email=row.get("Email"))

    @staticmethod
    def create_user(payload: UserCreate) -> UserOut:
        new_id = UserRepository.create(payload.username, payload.email)
        return UserOut(id=new_id, username=payload.username, email=payload.email)
