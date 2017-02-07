# Generates random field.


import random


def generate_field():
    """
    None -> list(list(str))

    Generates random field.
    """
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


def covered_area(coordinates1, coordinates2):
    """
    tuple(int, int), tuple(int, int) -> list(tuple(int, int)), set(tuple(int, int))

    Finds ship coordinates and area, which ship covers.
    """
    area = set()
    ship_coordinates = []
    if coordinates1 > coordinates2:
        coordinates1, coordinates2 = coordinates2, coordinates1

    for line in range(coordinates1[0], coordinates2[0] + 1):
        for column in range(coordinates1[1], coordinates2[1] + 1):
            ship_coordinates.append((line, column))

    for coordinates in ship_coordinates:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                area.add((coordinates[0] + i, coordinates[1] + j))
    return ship_coordinates, area
