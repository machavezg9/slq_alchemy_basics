# insert your code here
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine('sqlite:///movies.db', echo=False)
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    genre = Column(String)
    