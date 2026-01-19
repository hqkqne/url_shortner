import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, MetaData, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo = True)

with engine.connect() as con:
    result = con.execute(text("select 'hello world!'"))
    print(result.all())
