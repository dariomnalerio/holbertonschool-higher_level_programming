#!/usr/bin/python3
""" Module containing class Base """
import json
from os import path


class Base:
    """ Class base with attribute and class constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation
            of a list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation
            of list_objs to a file """
        if list_objs is None:
            new_list = []
        else:
            new_list = [lists.to_dictionary() for lists in list_objs]
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list
            of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
