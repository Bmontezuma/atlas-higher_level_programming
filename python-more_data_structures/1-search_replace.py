#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_list = [replace if element == search else element
                   for element in my_list]
    return result_list
