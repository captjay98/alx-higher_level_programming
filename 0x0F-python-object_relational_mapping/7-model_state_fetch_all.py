#!/usr/bin/python3
"""lists all states object from database"""

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

    data = session.query(State).order_by(State.id)
    for state in data:
        print(state.id, ':', state.name)
