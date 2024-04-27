from fastapi import FastAPI

from src.auth.routers import router as auth_router
from src.routes.rating_routers import router as rating_router

app = FastAPI(
    title="Tracker Service"
)

app.include_router(auth_router)
app.include_router(rating_router)
