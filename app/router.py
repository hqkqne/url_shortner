from fastapi import APIRouter, Depends, HTTPException, Response
from typing import Annotated

from starlette.responses import RedirectResponse

from service import get_service
from app.service import ServiceUrl
from schemas import *


router = APIRouter(
    prefix= "/URl"
)

@router.post("", response_model= URLResponse)
async def append_url(
        data: URLCreate,
        service: ServiceUrl = Depends(get_service)
):
    slug = await service.create_short_url(str(data.url))
    return {"short_url": slug, "original url" : str(data.url)}

@router.get("/{short}")
async def redirect(
    slug: str,
    service: ServiceUrl = Depends(get_service)
):

    original_url = await service.get_original_url(slug)
    if not original_url:
        raise HTTPException(status_code= 404, detail= 'Not found')
    return RedirectResponse(url = original_url, status_code= 307)
