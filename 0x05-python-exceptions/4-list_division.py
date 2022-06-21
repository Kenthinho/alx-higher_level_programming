#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp = 0
    for x in range(list_length):
        try:
            temp = my_list_1[x] / my_list_2[x]
        except TypeError:
            temp = 0
            print("wrong type")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            temp = 0
            print("out of range")
        finally:
            pass
        new_list.append(temp)
        return new_list
