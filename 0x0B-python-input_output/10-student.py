#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initiate a new Student

        Args:
            first_name (str): The first name of the Student.
            last_name (str): The last name of the Student.
            age (int): The age of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of Student.

        If attrs is a list of string, represents only those attributes
        included in the list.

        Args:
            attrs (str): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
