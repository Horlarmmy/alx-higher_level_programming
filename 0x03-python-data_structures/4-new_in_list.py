#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list[:]
        if (idx < 0 or idx > len(my_list) - 1):               return my_list
        for i in range(len(my_list)):
            if my_list[i] == my_list[idx]:
                new_list[idx] = element
                return new_list