from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update

from src.database.database import async_session
from src.database.models import Subject, District

from src.database.data import data

router = APIRouter(
    prefix="/ratings",
    tags=["ratings"],
)


@router.get("/")
async def get_ratings_list():
    async with async_session() as session:
        new_data = dict()
        query = select(District)
        result = await session.execute(query)
        districts = result.scalars().all()
        for district in districts:
            new_data[district.name] = dict()
            query = select(Subject).where(Subject.district_id == district.id)
            result = await session.execute(query)
            subjects = result.scalars().all()
            for subject in subjects:
                new_data[district.name][subject.name] = subject.votes_count_1

        return new_data


@router.post("/{subject_name}_1")
async def update_subject_rating_1(subject_name: str):
    async with async_session() as session:
        query = select(Subject.votes_count_1).where(Subject.name == subject_name)
        result = await session.execute(query)
        votes_count = result.scalars().first()

        new_votes_count = votes_count + 1
        stmt = update(Subject).where(Subject.name == subject_name).values(votes_count_1=new_votes_count)
        await session.execute(stmt)
        await session.commit()

    return {"status": "ok"}


@router.post("/{subject_name}_2")
async def update_subject_rating_2(subject_name: str):
    async with async_session() as session:
        query = select(Subject.votes_count_2).where(Subject.name == subject_name)
        result = await session.execute(query)
        votes_count = result.scalars().first()

        new_votes_count = votes_count + 1
        stmt = update(Subject).where(Subject.name == subject_name).values(votes_count_2=new_votes_count)
        await session.execute(stmt)
        await session.commit()

    return {"status": "ok"}


@router.post("/fill_subjects")
async def fill_subjects():
    async with async_session() as session:
        k = 0
        for district in data:
            k += 1
            for subject in data[district]:
                print(subject, k)
                stmt = insert(Subject).values(name=subject, district_id=k)
                await session.execute(stmt)
                await session.commit()

    return {"status": "ok"}


@router.post("/fill_districts")
async def fill_districts():
    async with async_session() as session:
        for district in data:
            stmt = insert(District).values(name=district)
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
