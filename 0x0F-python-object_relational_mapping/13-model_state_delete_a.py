#!/usr/bin/python3
"""
script that deletes all State objects
with a name containing the letter a
from the database hbtn_0e_6_usa
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

    data = session.query(State).filter(State.name.like("%a")).\
        delete(synchronize_session='fetch')
    session.commit()
