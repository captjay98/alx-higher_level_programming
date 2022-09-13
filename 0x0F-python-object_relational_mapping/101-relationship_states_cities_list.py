#!/usr/bin/python3
"""
All states via SQLAlchemy
and corresponding City
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

    data = session.query(State).order_by(State.id).all()

    for row in data:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("    {}: {}".format(city.id, city.name))

    session.commit()
    session.close()
