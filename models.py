from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=False) #where my database is going to accessed and created
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base() #B is capitalized bcause it calls a class and classes are upper case
#User Model below used to create entry with requirements below
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

    #_______________OLD CODE___________________

    # mig_user = User(name='Miguel', fullname='Miguel Chavez', nickname='chikles')
    # print(mig_user.name)
    # print(mig_user.id)
    # session.add(mig_user)
    # session.commit()
    # print(mig_user.id)
    # new_users = [
    #     User(name='Grace', fullname='Grace Hopper', nickname='Pioneer'), 
    #     User(name='Alan', fullname='Alan Turing', nickname='Computer Scientist'),  
    #     User(name='Katherine', fullname='Katherine Johnson', nickname='') 
    # ]

    # session.add_all(new_users)
    # session.commit()
    
    # for user in new_users:
    #     print(user.id)