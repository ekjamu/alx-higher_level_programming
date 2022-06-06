#!/usr/bin/python3
def print_list_integer(my_list):
    s = "{integer:d}"
    for i in my_list:
        print(s.format(integer = i))
