from pydantic import BaseModel


class CreateUser(BaseModel):
    phone_number: str
    username: str
    password: str
    age: int
    gender: str
    residence: str
