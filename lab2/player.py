class Player(object):
    """
    Player description.
    """
    def __init__(self, name):
        self._name = name

    def read_position(self, message):
        """
        int, str -> int, int

        Requests user to enter coordinates.
        """
        coordinates = input(message).split()
        chars = "ABCDEFGHIJ"
        return int(coordinates[1]) - 1, chars.index(coordinates[0])