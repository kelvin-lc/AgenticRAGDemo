from fastapi import APIRouter

from src.api.api_v1 import agent

api_router = APIRouter()

api_router.include_router(agent.router, prefix="/agent", tags=["agent"])
