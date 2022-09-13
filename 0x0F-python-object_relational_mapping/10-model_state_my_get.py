#!/usr/bin/python3
"""
script that prints the State object with the name 
passed as argument from the database hbtn_0e_6_usa
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

    data = session.query(State).filter(State.name == argv[4]).first()
    if data is not None:
        print(str(data.id))
    else:
        print("Not found")
