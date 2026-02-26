from fastapi import APIRouter, Depends, HTTPException, Response
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from app.db import get_db
from app.repository import UrlRepository
from app.service import ServiceUrl
from schemas import *


router = APIRouter(
    prefix= "/URl"
)

@router.post("", response_model= URLResponse)
async def append_url(
        data: URLCreate,
        session: AsyncSession = Depends(get_db())
):
    repo = UrlRepository(session)
    service = ServiceUrl(repo)
    
    slug = await service.create_short_url(str(data.url))
    return {"short_url": slug, "original url" : str(data.url)}

@router.get("/{short}")
async def redirect(
    slug: str,
    session: AsyncSession = Depends(get_db())
):
    repo = UrlRepository(session)
    service = ServiceUrl(repo)

    original_url = await service.get_original_url(slug)
    if not original_url:
        raise HTTPException(status_code= 404, detail= 'Not found')
    return RedirectResponse(url = original_url, status_code= 307)
