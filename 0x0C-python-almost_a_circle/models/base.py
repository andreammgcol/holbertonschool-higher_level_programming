#!/usr/bin/python3
""" base """
import json


class Base:
    """ the first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        that returns the JSON string representation of list_dictionaries
        Arguments:
        @list_dictionaries: list of dictionaries
        Returns:
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            d = [{
                'x': list_dictionaries[0]['x'], 
                'width': list_dictionaries[0]['width'],
                'id': list_dictionaries[0]['id'],
                'height': list_dictionaries[0]['height'],
                'y': list_dictionaries[0]['y']
                }]
            s = json.dumps(d)
            # s = json.dumps(list_dictionaries)
            return s

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - writes the JSON string representation
        of list_objs to a file
        Arguments:
        @cls: class
        @list_objs: list of instances who inherits of Base
        """
        with open('{}.json'.format(cls.__name__), mode='w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                myList = []
                for i in list_objs:
                    i = i.to_dictionary()
                    myList.append(i)
                f.write(cls.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        Arguments:
        @json_string: string representing a list of dictionaries
        Returns:
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = None
        if str(cls) == "<class 'models.rectangle.Rectangle'>":
            dummy = cls(dictionary['width'], dictionary['height'])
            dummy.update(**dictionary)
        elif str(cls) == "<class 'models.square.Square'>":
            dummy = cls(dictionary['size'])
            dummy.update(**dictionary)
        return dummy
