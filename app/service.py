from repository import UrlRepository
from fastapi import Depends
from models import URLShort
from sqids import Sqids

from repository import get_repo

class ServiceUrl:
    def __init__(self, repo: UrlRepository):
        self.repo = repo
        self.sqids = Sqids(min_length= 5)

    async def create_short_url(self, original_url: str)-> str:
        db_url = await self.repo.add_one(
            original_url = original_url, short_url = 'pending'
        )
        short_url = self.sqids.encode([db_url.id])
        db_url.short_url = short_url
        await self.repo.session.commit()
        return short_url

    async def get_original_url(self, short_url: str)-> str:
        url = await self.repo.get_by_short(short_url)
        if url is None:
            return None
        return url.original_url

async def get_service(repo: UrlRepository = Depends(get_repo))-> ServiceUrl:
    return ServiceUrl(repo)