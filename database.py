
from sqlalchemy import create_engine, Column, Integer, String, 
#from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

from sqlalchemy.sql import text

Base = declarative_base()

engine = create_engine('sqlite+pysqlite:///data.db', echo=True, future=True)
#session = Session(engine)

class ToDo(Base):
    __tablename__ = 'todolist'

    id = Column(Integer, nullable= False, unique= True, primary_key=True)
    title = Column(String, nullable = False)
    task_description = Column(String, nullable = False)
    state = Column(String, nullable= False)
    due_date = Column(Integer, nullable= False)   


def create_tables(engine):
    Base.metadata.create_all(engine)


create_tables(engine)