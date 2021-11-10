from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Employee(Base):
    __tablename__ = 'Employee'
    EmployeeId = Column(Integer, primary_key=True)
    FirstName = Column(Text, nullable=False)
    LastName = Column(Text, nullable=False)
    HireDate = Column(Date)

