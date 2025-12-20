from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token


class AuthService:
    def __init__(self, session: AsyncSession):
        self.user_repo = UserRepository(session)

    async def register_user(self, email: str, password: str, role: str) -> User:
        existing_user = await self.user_repo.get_by_email(email)
        if existing_user:
            raise ValueError("User already exists")

        user = User(
            email=email,
            hashed_password=hash_password(password),
            role=role,
        )
        return await self.user_repo.create(user)

    async def authenticate_user(self, email: str, password: str) -> str:
        user = await self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        token = create_access_token(data={"sub": str(user.id), "role": user.role})
        return token
