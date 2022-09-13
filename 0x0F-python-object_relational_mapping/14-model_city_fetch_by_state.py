#!/usr/bin/python3
"""prints the first state object from database"""

from sys import argv
from sqlalchemy .orm import sessionmaker, relationship
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State, City).\
        filter(City.state_id == State.id).all()
    for item in data:
        print("{}: ({}) {}".format(item[0].name, item[1].id, item[1].name))
