#!/usr/bin/python3
""" Module for writing an Object to a file with JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dumps(my_obj, file)
