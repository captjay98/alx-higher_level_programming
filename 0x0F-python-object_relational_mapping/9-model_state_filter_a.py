#!/usr/bin/python3
"""
Write a script that lists all State objects that 
contain the letter a from the database
"""

from sys import argv
from sqlalchemy .orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.like("%a")).all()
    for state in data:
        print(state.id, ':', state.name)
