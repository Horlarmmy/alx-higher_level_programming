#!/usr/bin/python3
read_file = __import__('2-append_write').append_write
chart = read_file("afile.txt", "THis school is so cool\n")
print(chart)
