#!/usr/bin/python3
def element_at(my_list,idx):
    if (idx<0):
        return None
    if (idx > len(my_list)):
        return None
    n = 0

    for item in range(my_list)):
        if n == idx:
            print("Element at index {:d} is {}".format(idx,item))
        n = n + 1
