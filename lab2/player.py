class Player():
    def __init__(self, name):
        self._name = name

    def read_position(self, message):
        coordinates = input(message).split()
        chars = "ABCDEFGHIJ"
        return int(coordinates[1]) - 1, chars.index(coordinates[0])