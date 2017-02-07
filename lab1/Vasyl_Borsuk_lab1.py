# Generates random field for battleship game and prints result on the desktop,
# or save it in file
# Created: 02.02.2017


def read_field(filename):
    """
    str -> list(list(str))

    Reads field from file.
    """
    with open(filename, "r") as field_txt:
        field = field_txt.readlines()
        for line in range(len(field)):
            field[line] = list(field[line])[0:10]
        return field


def convert_coordinates(field_coordinates):
    """
    tuple(str, int) -> tuple(int, int)

    Transforms coordinates from game format to list format.
    """
    chars = "ABCDEFGHIJ"
    return field_coordinates[1] - 1, chars.index(field_coordinates[0])


def has_ship(field, coordinates):
    """
    list(list(str)), tuple(int, int) -> bool

    Checks whether ship is in the given coordinats.
    """
    if field[coordinates[0]][coordinates[1]] == "*":
        return True
    return False


def ship_size(field, coordinates):
    """
    list(list(str)), tuple(int, int) -> tuple(int, list(tuple(int, int)))

    Finds the size of ship in the given coordinates.
    """
    if has_ship(field, coordinates):
        size = 1
        ship_coordinates = [coordinates]
        for i in range(1, 9):
            if (coordinates[0] - i) >= 0 and has_ship(field, (coordinates[0] - i, coordinates[1])):
                size += 1
                ship_coordinates.append((coordinates[0] - i, coordinates[1]))
            else:
                break
        for i in range(1, 9):
            if (coordinates[0] + i) <= 9 and has_ship(field, (coordinates[0] + i, coordinates[1])):
                size += 1
                ship_coordinates.append((coordinates[0] + i, coordinates[1]))
            else:
                break
        if size == 1:
            for i in range(1, 9):
                if (coordinates[1] - i) >= 0 and has_ship(field, (coordinates[0], coordinates[1] - i)):
                    size += 1
                    ship_coordinates.append((coordinates[0], coordinates[1] - i))
                else:
                    break
            for i in range(1, 9):
                if (coordinates[1] + i) <= 9 and has_ship(field, (coordinates[0], coordinates[1] + i)):
                    size += 1
                    ship_coordinates.append((coordinates[0], coordinates[1] + i))
                else:
                    break
        return size, ship_coordinates


def is_valid(field):
    """
    list(list(str)) -> bool

    Checks whether requested field is correct.
    """
    used_coordinates = []
    used_ships = [0 for i in range(4)]
    for line in range(len(field)):
        for column in range(len(field[line])):
            if (line, column) not in used_coordinates:
                ship_size_res = ship_size(field, (line, column))
                if ship_size_res:
                    used_coordinates += ship_size_res[1]
                    used_ships[ship_size_res[0] - 1] += 1

    for i in range(len(used_ships)):
        if 4 - i != used_ships[i]:
            return False
    return True


def field_to_str(field, filename=None):
    """
    list(list(str)), str -> None

    Prints field on the desktop or save in the file.
    """
    chars = "ABCDEFGHIJ"
    field_str = "+---" * 11 + "+\n|   |"
    for i in range(len(chars)):
        field_str += " " + chars[i] + " |"
    field_str += "\n" + "+---" * 11 + "+\n"
    for line in range(len(field)):
        if line == 9:
            field_str += "| " + str(line + 1)
        else:
            field_str += "| " + str(line + 1) + " "
        for column in range(len(field[line])):
            field_str += "| " + field[line][column] + " "
        field_str += "|\n" + "+---" * 11 + "+\n"
    print(field_str)

    if filename:
        with open(filename, "w") as field_txt:
            for line in range(len(field)):
                for column in range(len(field[line])):
                    field_txt.write(field[line][column])
                if line != 9:
                    field_txt.write("\n")


def generate_field():
    """
    None -> list(list(str))

    Generates random field.
    """
    import random

    def covered_area(coordinates1, coordinates2):
        """
        tuple(int, int), tuple(int, int) -> list(tuple(int, int)), set(tuple(int, int))

        Finds ship coordinates and area, which ship covers.
        """
        area = set()
        ship_coordinates = set()
        if coordinates1 > coordinates2:
            coordinates1, coordinates2 = coordinates2, coordinates1

        for line in range(coordinates1[0], coordinates2[0] + 1):
            for column in range(coordinates1[1], coordinates2[1] + 1):
                ship_coordinates.add((line, column))

        for coordinates in ship_coordinates:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    area.add((coordinates[0] + i, coordinates[1] + j))
        return ship_coordinates, area

    def generate_coordinates2(coordinates1, size):
        """
        tuple(int, int), int -> tuple(int, int)

        Finds second coordinates of the ship.
        """
        while True:
            x = random.choice([-size + 1, 0, size - 1])
            if x == 0:
                y = random.choice([-size + 1, size - 1])
            else:
                y = 0
            coordinates2 = (coordinates1[0] + x, coordinates1[1] + y)
            if coordinates2[0] in range(10) and coordinates2[1] in range(10):
                return coordinates2

    field = [[" " for i in range(10)] for i in range(10)]
    number_of_ships = [i for i in range(1, 5)]
    used_coordinates = [(i, j) for i in range(10) for j in range(10)]
    for ship_type in range(len(number_of_ships)):
        for ship in range(number_of_ships[ship_type]):
            while True:
                coordinates1 = random.choice(used_coordinates)
                size = 4 - ship_type
                coordinates2 = generate_coordinates2(coordinates1, size)
                ship_coordinates, area = covered_area(coordinates1, coordinates2)

                dermo = False
                for coordinates in ship_coordinates:
                    if (coordinates[0] in range(10) and coordinates[1] in range(10)) and\
                       coordinates not in used_coordinates:
                        dermo = True
                if dermo:
                    continue

                for coordinates in area:
                    if coordinates[0] in range(10) and coordinates[1] in range(10) and\
                            coordinates in used_coordinates:
                        used_coordinates.remove(coordinates)
                for coordinates in ship_coordinates:
                    field[coordinates[0]][coordinates[1]] = "*"
                break
    return field


correct = 0
incorrect = 0
import time
start = time.time()
for i in range(1000):
    field = generate_field()
    '''if is_valid(field):
        correct += 1
    else:
        incorrect += 0'''
finish = time.time()
print("correct: " + str(correct) + "\nincorrect: " + str(incorrect) + "\ntime: " + str(finish - start))
