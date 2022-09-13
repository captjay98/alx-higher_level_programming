#!/usr/bin/python3
"""contains the class definition of a State"""


from sqlalchemy .orm import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class State(Base):
    """State class:
    Inherits from base and maps table
    int primary key id v
    string name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
