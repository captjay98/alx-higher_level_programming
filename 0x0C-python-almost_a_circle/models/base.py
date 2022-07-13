#!/usr/bin/python3
""" Base Class for all other objects in this Project"""
import json


class Base:
    """A base class to manage other classes created
    @id: The id for a specific instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """new  id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__),
                      "r", encoding="utf-8") as f:
                return [cls.create(**o)
                        for o in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of instances to a csv file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.csv".format(cls.__name__), "w", encoding="utf-8") as f:
            if cls.__name__ == "Rectangle":
                f.write("[Rectangle]\n")
            elif cls.__name__ == "Square":
                f.write("[Square]\n")
            for o in list_objs:
                f.write(str(o) + "\n")

    @staticmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        try:
            with open("{}.csv".format(cls.__name__),
                      "r", encoding="utf-8") as f:
                return [cls.create(**o)
                        for o in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
