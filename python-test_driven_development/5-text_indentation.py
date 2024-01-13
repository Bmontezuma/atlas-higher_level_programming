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
    # Check if the text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace all whitespace characters with spaces
    text = text.replace("\t", " ").replace("\n", " ").replace("\r", " ")

    # Initialize a flag variable
    prev_punct = False

    # Loop through each character in the text
    for char in text:
        # Print the character
        print(char, end="")

        # Check if the character is a punctuation mark
        if char in [".", "?", ":"]:
            # Print two new lines
            print("\n\n", end="")
            # Set the flag to True
            prev_punct = True
        else:
            # Reset the flag to False
            prev_punct = False

    # Print a new line if the last character was not a punctuation mark
    if not prev_punct:
        print()
