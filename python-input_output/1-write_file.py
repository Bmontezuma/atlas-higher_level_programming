#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    This function writes string to file and returns number characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = len(text)
        file.write(text)
        return nb_characters
