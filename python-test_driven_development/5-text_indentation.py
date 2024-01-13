#!/usr/bin/python3
"""
This module has function to print text with 2 new lines after each: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    current_line = ""
    prev_punct = False

    # replace all whitespace characters with spaces
    text = text.replace("\\t", " ").replace("\\n", " ").replace("\\r", " ")

    for char in text:
        current_line += char

        if char in separators:
            # print the current line without leading or trailing spaces
            print(current_line.strip())
            print()
            current_line = ""
            prev_punct = True
        else:
            # reset the flag if the character is not a punctuation mark
            prev_punct = False

    # print the remaining line if it is not empty or a punctuation mark
    if current_line and not prev_punct:
        print(current_line.strip())
