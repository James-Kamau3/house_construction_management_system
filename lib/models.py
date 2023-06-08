# models.py
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref


from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///house.db')

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    name_of_house = Column(String, nullable=False)
    license_id = Column(Integer, ForeignKey('licenses.id'))
    license = relationship('License', backref=backref('houses'))

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name_of_worker = Column(String, nullable=False)
    age = Column(Integer)
    phone_number = Column(Integer)
    role = Column(String)
    pay = Column(Integer)
    house_id = Column(Integer, ForeignKey('houses.id'))
    house = relationship('House', backref=backref('workers'))

class Tool(Base):
    __tablename__ = 'tools'
    id = Column(Integer, primary_key=True)
    name_of_tool = Column(String, nullable=False)
    cost = Column(Integer)
    worker_id = Column(Integer, ForeignKey('workers.id'))
    worker = relationship('Worker', backref=backref('tools'))

class License(Base):
    __tablename__ = 'licenses'
    id = Column(Integer, primary_key=True)
    name_of_license = Column(String, nullable=False)
    description = Column(String)
    

Base.metadata.create_all(engine)


