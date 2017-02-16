class Ship(object):
    """
    Represents ship for Battleship game.
    """
    def __init__(self, coordinates, length):
        self.bow = coordinates
        if length[0] != 1:
            self.horizontal = True
        else:
            self.horizontal = False
        self._length = length
        self._hit = [False for i in range(max(length))]

    def shoot_at(self, coordinates):
        """
        tuple(int, int) -> None

        Makes ship hitted in the given coordinates.
        """
        self._hit[abs(self.bow[0] - coordinates[0]) + abs(self.bow[1] - coordinates[1])] = True

    def is_valid(self, possible_coordinates):
        """
        list(tuple(int, int)) -> bool

        Checks whether ship is situated correctly.
        """
        for line in range(self.bow[0], self.bow[0] + self._length[0]):
            for column in range(self.bow[1], self.bow[1] + self._length[1]):
                if (line, column) not in possible_coordinates:
                    return False
        return True

    def covered_area(self):
        """
        tuple(int, int), tuple(int, int) -> set(tuple(int, int))

        Finds ship coordinates and area, which ship covers.
        """
        area = set()
        for line in range(self.bow[0] - 1, self.bow[0] + self._length[0] + 1):
            for column in range(self.bow[1] - 1, self.bow[1] + self._length[1] + 1):
                if line >= 0 and line <= 9 and column >= 0 and column <= 9:
                    area.add((line, column))
        return area

    def print_point(self, coordinates):
        """
        tuple(int, int) -> str

        Returns ship view in the field.
        """
        if self._hit[abs(self.bow[0] - coordinates[0]) + abs(self.bow[1] - coordinates[1])]:
            return "X"
        return "*"
