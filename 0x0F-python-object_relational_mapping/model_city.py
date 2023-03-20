#!/usr/bin/python3

""" sqlalchemy model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from model_state import Base, State



class City(Base):
    """ State object """
    __tablename__ = "cities"
    id = Column(
         Integer, Sequence('my_sequence'), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
