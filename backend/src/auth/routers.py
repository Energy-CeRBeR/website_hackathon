from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert

from src.auth.schemas import CreateUser
from src.database.database import async_session
from src.database.models import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

CURRENT_USER_ID = 0


@router.post("/register/")
async def register_user(user: CreateUser):
    async with async_session() as session:
        query = select(User).where(User.phone_number == user.phone_number)
        result = await session.execute(query)
        users = result.scalars().all()

        if users:
            raise HTTPException(
                status_code=400,
                detail="User with this phone number already exists"
            )

        stmt = insert(User).values(
            username=user.username,
            phone_number=user.phone_number,
            password=user.password,
            age=user.age,
            gender=user.gender,
            residence=user.residence
        )

        await session.execute(stmt)
        await session.commit()

        return {"message": "User created successfully"}


@router.post("/login/")
async def login(phone_number: str, password: str):
    global CURRENT_USER_ID
    async with async_session() as session:
        query = select(User).where(User.phone_number == phone_number)
        result = await session.execute(query)
        user = result.scalars().first()

        if not user:
            raise HTTPException(
                status_code=400,
                detail="Incorrect login or password"
            )

        if not user.password == password:
            raise HTTPException(
                status_code=400,
                detail="Incorrect login or password"
            )

        CURRENT_USER_ID = user.id

        return {"status": "User logged in successfully"}
