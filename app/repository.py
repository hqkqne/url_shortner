from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from schemas import URLCreate, URLResponse
from models import URLShort

class UrlRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, url: URLShort)->URLShort:
        self.session.add(url)
        await self.session.commit()
        await self.session.refresh(url)
        return url

    async def get_by_short(self, short_url: str)-> URLShort| None:
        result = await self.session.execute(
            select(URLShort).where(URLShort.short_url == short_url)
        )
        return result.scalar_one_or_none()