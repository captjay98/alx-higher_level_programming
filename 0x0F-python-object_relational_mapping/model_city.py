#!/usr/bin/python3
"""contains the class definition of a City"""

from model_state import Base
from sqlalchemy .orm import declarative_base, relationship
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """State class:
    Inherits from base and maps table
    int primary key id
    string name
    state_id foreign key
    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
