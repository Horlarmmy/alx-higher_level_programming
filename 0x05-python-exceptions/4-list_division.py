#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            new_list[i] = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            new_list[i] = 0
            pass
        except IndexError:
            print("out of range")
            new_list[i] = 0
            pass
        finally:
            new_list.append(result)
        return new_list
