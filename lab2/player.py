class Player(object):
    """
    Represents player in Battleship game.
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
