#!/usr/bin/python3
"""
creates the State “California” with 
the City “San Francisco” 
from the database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)

    session = Session(engine)
    s = State(name='California')

    c = City(name='San Francisco')
    s.cities.append(c)

    session.add(s)
    session.commit()
    session.close()
