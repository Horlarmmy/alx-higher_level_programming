#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        res = None
    else:
        res = c
    finally:
        print("Inside result: {}" .format(res))
    return res
