# Reads field from file and checks whether it is correct.


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


def is_valid(field):
    """
    list(list(str)) -> bool

    Checks whether requested field is correct.
    """
    import ship_info
    from generate_field import covered_area

    used_coordinates = set()
    used_area = set()
    used_ships = [0 for i in range(4)]
    for line in range(len(field)):
        for column in range(len(field[line])):
            if (line, column) not in used_coordinates:
                if ship_info.has_ship(field, (line, column)) and (line, column) in used_area:
                    return False

                ship_size_res = ship_info.ship_size(field, (line, column))
                if ship_size_res:
                    ship_coordinates = sorted(ship_size_res[1])
                    ship_area = covered_area(ship_coordinates[0], ship_coordinates[-1])[1]
                    used_area = used_area|ship_area
                    used_coordinates = used_coordinates|set(ship_coordinates)
                    used_ships[ship_size_res[0] - 1] += 1

    for i in range(len(used_ships)):
        if 4 - i != used_ships[i]:
            return False
    return True
