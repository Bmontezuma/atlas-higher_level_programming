import json

class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes Rectangle instance.
        area(self): Calculate and return the area of the rectangle.
        display(self): Print the rectangle with '#' characters.
        update(self, *args, **kwargs): Update attributes with arguments.
        to_dictionary(self): Returns dictionary representation of rectangle.
        to_json_string(list_dictionaries): Returns JSON representation of list_dictionaries.
        __str__(self): Return the string representation of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The identifier of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#' characters."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update attributes with arguments."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    setattr(self, key, value)
                elif key in ["width", "height", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

