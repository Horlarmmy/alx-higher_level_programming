#!/usr/bin/python3
def raise_execution():
    raise TypeError

try:
    raise_execution()
except TypeError as te:
    print("Exception rasied")

