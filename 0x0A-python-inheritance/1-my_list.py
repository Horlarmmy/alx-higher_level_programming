#!/usr/bin/python3
"""
Module 1-my_list
Class Mylist
"""


class MyList(list):
    """ A class inheriting from the list class"""
    def print_sorted(self):
        """ Returns a sorted list"""
        print(sorted(self))
