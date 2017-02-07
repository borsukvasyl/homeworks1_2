# Calculates size of ship in requested coordinates.


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
