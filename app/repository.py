from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import select

from db import get_db
from models import URLShort

class UrlRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, original_url: str, short_url: str)->URLShort:
        db_url = URLShort(original_url = original_url, short_url = short_url)
        self.session.add(db_url)
        await self.session.flush()
        await self.session.refresh(db_url)
        return db_url

    async def get_by_short(self, short_url: str)-> URLShort| None:
        result = await self.session.execute(
            select(URLShort).where(URLShort.short_url == short_url)
        )
        return result.scalar_one_or_none()

async def get_repo(session: AsyncSession = Depends(get_db))-> UrlRepository:
    return UrlRepository(session)