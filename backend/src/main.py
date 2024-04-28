from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import requests

from src.auth.routers import router as auth_router
from src.routes.rating_routers import router as rating_router
from src.routes.user_routers import router as user_router

app = FastAPI(
    title="Tracker Service"
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:5173",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(rating_router)
app.include_router(user_router)

if __name__ == "__main__":
    res = requests.get("http://127.0.0.1:8000/ratings/")
    print(res.json())
