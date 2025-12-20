from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user: UserCreate, session: AsyncSession = Depends(get_db)):
    service = AuthService(session)
    try:
        created_user = await service.register_user(user.email, user.password, user.role)
        return {"id": created_user.id, "email": created_user.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(
    email: str,
    password: str,
    session: AsyncSession = Depends(get_db),
):
    service = AuthService(session)
    try:
        token = await service.authenticate_user(email, password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")
