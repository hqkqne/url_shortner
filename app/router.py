from fastapi import APIRouter, Depends
from typing import Annotated

from schemas import *


router = APIRouter(
    prefix= "/URl"
)

@router.post("")
async def get_original_URL(url: Annotated[URLCreate, Depends()]):
    return {"ok": True}

@router.get("/{short}")
async def redirect(

):
    ...
