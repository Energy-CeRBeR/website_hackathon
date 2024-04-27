from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update

from src.database.database import async_session
from src.database.models import Subject, District

router = APIRouter(
    prefix="/ratings",
    tags=["ratings"],
)


@router.get("/")
async def get_ratings_list():
    async with async_session() as session:
        data = dict()
        query = select(District)
        result = await session.execute(query)
        districts = result.scalars().all()
        for district in districts:
            data[district.name] = dict()
            query = select(Subject).where(Subject.district_id == district.id)
            result = await session.execute(query)
            subjects = result.scalars().all()
            for subject in subjects:
                data[district.name][subject.name] = subject.votes_count

        return data


@router.put("/{subject_name}")
async def update_subject_rating(subject_name: str):
    async with async_session() as session:
        query = select(Subject.votes_count).where(Subject.name == subject_name)
        result = await session.execute(query)
        votes_count = result.scalars().first()

        new_votes_count = votes_count + 1
        stmt = update(Subject).where(Subject.name == subject_name).values(votes_count=new_votes_count)
        await session.execute(stmt)
        await session.commit()

    return {"status": "ok"}


@router.get("/{subject_name}")
async def get_subject(subject_name: str):
    async with async_session() as session:
        query = select(Subject).where(Subject.name == subject_name)
        result = await session.execute(query)
        subject = result.scalars().first()
        return subject


if __name__ == "__main__":
    ...
