#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
    finall:
        print("inside result: {}".format(result))
    return result
