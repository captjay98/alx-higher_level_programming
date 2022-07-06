#!/usr/bin/python3
"""Defines a class Representing Student"""


class Student():
    """defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary description of the Student"""
        return self.__dict__
