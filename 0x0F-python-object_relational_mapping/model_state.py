#!/usr/bin/python3
""" SQLACHEMY MODEL """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(
         Integer, Sequence('my_sequence'), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
