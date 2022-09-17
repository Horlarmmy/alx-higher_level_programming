#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""

from os import stat
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    states = session.query(State).order_by(State.id).filter(State.name.like(s))
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
