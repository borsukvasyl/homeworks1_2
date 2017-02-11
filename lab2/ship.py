class Ship(object):
    """
    Ship description.
    """
    def __init__(self, coordinates, length):
        self.bow = coordinates
        if length[0] != 1:
            self.horizontal = True
        else:
            self.horizontal = False
        self.length = length
        self.hit = [False for i in range(max(length))]

    def shoot_at(self, coordinates):
        """
        tuple(int, int) -> None

        Makes ship hitted in the given coordinates.
        """
        self.hit[abs(self.bow[0] - coordinates[0]) + abs(self.bow[1] - coordinates[1])] = True

    def is_valid(self, possible_coordinates):
        """
        list(tuple(int, int)) -> bool

        Checks whether ship is situated correctly.
        """
        for line in range(self.bow[0], self.bow[0] + self.length[0]):
            for column in range(self.bow[1], self.bow[1] + self.length[1]):
                if (line, column) not in possible_coordinates:
                    return False
        return True

    def covered_area(self):
        """
        tuple(int, int), tuple(int, int) -> list(tuple(int, int)), set(tuple(int, int))

        Finds ship coordinates and area, which ship covers.
        """
        area = set()
        for coordinates in\
            [(self.bow[0] + i, self.bow[1] + j) for i in range(self.length[0]) for j in range(self.length[1])]:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    area.add((coordinates[0] + i, coordinates[1] + j))
        return area

    def print_point(self, coordinates):
        if self.hit[abs(self.bow[0] - coordinates[0]) + abs(self.bow[1] - coordinates[1])]:
            return "X"
        return "*"
