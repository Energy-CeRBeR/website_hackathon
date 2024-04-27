from dataclasses import dataclass
from environs import Env


@dataclass
class Database:
    URL: str


@dataclass
class Config:
    database: Database


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(database=Database(URL=env('DATABASE_URL')))
