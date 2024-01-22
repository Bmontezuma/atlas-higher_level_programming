#!/usr/bin/python3
"""
Script adds all arguments to Python list, and then saves to a file.
"""

import sys
import json
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if add_item.json exists, and load the existing list
filename = "add_item.json"
my_list = []
if exists(filename):
    my_list = load_from_json_file(filename)

# Append command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to add_item.json
save_to_json_file(my_list, filename)
