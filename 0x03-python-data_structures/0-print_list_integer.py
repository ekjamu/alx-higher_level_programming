#!/usr/bin/python3
def print_list_integer(alist):
    s = '{integer:d}'
    for i in alist:
        print(s.format(integer = i))
