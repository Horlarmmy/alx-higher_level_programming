#!/usr/bin/python3
Base = __import__('6-base_geometry').BaseGeometry

bg = Base()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}" .format(e.__class__.__name__, e))
