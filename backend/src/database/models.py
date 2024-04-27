import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base


class Gender(enum.Enum):
    male = "Мужчина",
    female = "Женщина",


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    age: Mapped[int] = mapped_column()
    gender: Mapped[Gender] = mapped_column()
    residence: Mapped[str] = mapped_column()
    votes: Mapped[int] = mapped_column(default=0)
    donation: Mapped[int] = mapped_column(default=0)

    phone_number: Mapped[str] = mapped_column(nullable=False)


class District(Base):
    __tablename__ = "districts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincement=True)
    name: Mapped[str] = mapped_column(unique=True)

    subjects = relationship("Subject")


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    votes_count: Mapped[int] = mapped_column(default=0)

    district_id: Mapped[int] = mapped_column(ForeignKey("districts.id"))


class VotePackages(Base):
    __tablename__ = "vote_packages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    coast: Mapped[int] = mapped_column(nullable=False)
    votes: Mapped[int] = mapped_column(default=0)
