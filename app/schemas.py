from pydantic import BaseModel,HttpUrl

class URLCreate(BaseModel):
    url: HttpUrl    #could be optional if I needed

class URLResponse(BaseModel):
    id: int
    short_url: str
    original_url: str
