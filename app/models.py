from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class URLShort(Base):
    __tablename__ = "short_urls"
    id: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    short_url: Mapped[str] = mapped_column(String(15), unique=True)
    original_url: Mapped[str] = mapped_column(String)