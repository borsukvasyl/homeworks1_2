class Player(object):
    """
    Player description.
    """
    def __init__(self, name):
        self._name = name

    def read_position(self, landed, killed):
        """
        bool, bool -> int, int

        Requests user to enter coordinates.
        """
        if killed:
            message = "Killed!!!"
        elif landed:
            message = "Landed!"
        else:
            message = ""
        coordinates = input(message + "Enter next coordinates: ").split()
        chars = "ABCDEFGHIJ"
        return int(coordinates[1]) - 1, chars.index(coordinates[0])
