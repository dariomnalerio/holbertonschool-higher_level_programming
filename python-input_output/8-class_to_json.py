#!/usr/bin/python3
""" Module for adding Python arguments to a list and saving them to a file """


import json


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object """
    return obj.__dict__
