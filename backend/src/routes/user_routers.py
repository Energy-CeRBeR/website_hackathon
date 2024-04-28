from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update

from src.database.database import async_session
from src.database.models import Subject, District, User

from src.database.data import data
from src.database.user_states import user_states_dict

from src.routes.schemas import UserModel

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)


@router.get("/")
async def get_user():
    async with async_session() as session:
        if not user_states_dict["current_user_id"]:
            raise HTTPException(
                status_code=403,
                detail="Unauthorized"
            )

        query = select(User).where(User.id == user_states_dict["current_user_id"])
        result = await session.execute(query)
        user = result.scalars().first()

        response = {
            "username": user.username,
            "phone_number": user.phone_number,
            "age": user.age,
            "gender": user.gender,
            "residence": user.residence,
            "votes": user.votes,
            "donation": user.donation
        }

        return response
