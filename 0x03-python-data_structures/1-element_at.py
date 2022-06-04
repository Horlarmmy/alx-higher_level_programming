#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list) - 1):
        return None
    for i in range(len(my_list)):
        if my_list[i] == my_list[idx]:
            return my_list[idx]
