from repository import UrlRepository
from models import URLShort
from sqids import Sqids

class ServiceUrl():
    def __init__(self, repo: UrlRepository):
        self.repo = repo
        self.sqids = Sqids(min_length= 5)

    async def create_short_url(self, long: str):
        #generate slug
        url = URLShort(short_url = ... ,original_url= long)
        await self.repo.add_one(url)
        return url

    async def get_long_url(self, short: str)-> str:
        url = await self.repo.get_by_short(short)
        return short