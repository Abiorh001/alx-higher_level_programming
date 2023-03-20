#!/usr/bin/python3

""" script to list first state """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
         'mysql+mysqldb://{}:{}@localhost/{}'
         .format(sys.argv[1], sys.argv[2], sys.argv[3]),
         pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = State(name='Louisiana')
    session.add(states)
    session.commit()
    state = session.query(State).filter_by(name='Louisiana').first()
    print(f"{state.id}")
