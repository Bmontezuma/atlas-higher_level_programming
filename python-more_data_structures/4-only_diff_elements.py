#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_diff_set = set()

    only_diff_set.update(set_1 - set_2)
    only_diff_set.update(set_2 - set_1)

    return only_diff_set
