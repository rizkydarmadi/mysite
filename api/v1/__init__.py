from fastapi import APIRouter
from api.v1.jenisContent import router as jenis_content

v1_router = APIRouter(
    prefix='/v1'
)

v1_router.include_router(jenis_content)