
from sqlalchemy import create_engine, inspect

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, 

Base = automap_base()
Session = sessionmaker()

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

def return_session(engine):
    Session.configure(bind=engine)
    return Session()




engine = create_engine('sqlite:///Chinook.db')
Base.prepare(engine=engine, reflect=True)
Employee, Album = Base.classes.Employee, Base.classes.Album
session = return_session(engine)