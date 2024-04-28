from pydantic import BaseModel


class UserModel(BaseModel):
    phone_number: str
    username: str
    password: str
    age: int
    gender: str
    residence: str
    votes: int
    donation: int
