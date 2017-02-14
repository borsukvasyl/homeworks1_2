class Player(object):
    """
    Player description.
    """
    def __init__(self, name):
        self._name = name

    def read_position(self, message):
        """
        bool, bool -> int, int

        Requests user to enter coordinates.
        """
        coordinates = input(message + "Enter next coordinates: ")
        return int(coordinates[1:]) - 1, "ABCDEFGHIJ".index(coordinates[0].upper())
