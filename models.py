from sqlalchemy import create_engine
from sqlalchemy.sql.expression import true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine('sqlite:///users.db', echo=True) #where my database is going to accessed and created
Base = declarative_base() #B is capitalized bcause it calls a class and classes are upper case

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)