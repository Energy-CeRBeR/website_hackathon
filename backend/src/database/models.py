from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column()
    gender: Mapped[str] = mapped_column()
    residence: Mapped[str] = mapped_column()
    votes: Mapped[int] = mapped_column(default=100)
    donation: Mapped[int] = mapped_column(default=0)


class District(Base):
    __tablename__ = "districts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    subjects = relationship("Subject")


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    votes_count_1: Mapped[int] = mapped_column(default=0)
    votes_count_2: Mapped[int] = mapped_column(default=0)

    district_id: Mapped[int] = mapped_column(ForeignKey("districts.id"))


class VotePackages(Base):
    __tablename__ = "vote_packages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    coast: Mapped[int] = mapped_column(nullable=False)
    votes: Mapped[int] = mapped_column(default=0)
