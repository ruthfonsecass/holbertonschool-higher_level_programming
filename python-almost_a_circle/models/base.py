#!/usr/bin/python3
"""A module with a simple class"""
import json


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            This is a constructor function that assigns an ID to
            an object either
            based on a given ID or by incrementing a counter
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        my_dict = []
        for obj in list_objs:
            my_dict.append(obj.to_dictionary())
        obj = cls.to_json_string(my_dict)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            jsonfile.write(obj)