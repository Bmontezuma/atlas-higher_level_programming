#!/usr/bin/python3
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

    text = text.replace("\\t", " ").replace("\\n", " ").replace("\\r", " ")

    for char in text:
        current_line += char

        if char in separators:
            print(current_line.strip())
            print()
            current_line = ""
            prev_punct = True
        else:
            prev_punct = False

    if current_line and not prev_punct:
        print(current_line.strip())
