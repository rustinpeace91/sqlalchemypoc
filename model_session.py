import datetime as dt
from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Employee, Base

Session = sessionmaker()

def return_session(engine):
    Base.metadata.create_all(bind=engine)
    Session.configure(bind=engine)
    return Session()

def object_as_dict(obj):
    return {
        c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs
    }


engine = create_engine('sqlite:///Chinook.db')
session = return_session(engine)