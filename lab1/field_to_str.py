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
