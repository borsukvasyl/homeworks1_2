class Player():
    def __init__(self, name):
        self._name = name

    def read_position(self):
        coordinates = input("Enter coordinates: ").split()
        chars = "ABCDEFGHIJ"
        return coordinates[1] - 1, chars.index(coordinates[0])