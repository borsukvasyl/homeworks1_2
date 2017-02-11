import field, player


class Game():
    def __init__(self, name1, name2):
        self.fields = [field.Field(), field.Field()]
        self.players = [player.Player(name1), player.Player(name2)]
        self.current_player = 0

    def read_position(self, index, message):
        return self.players[index].read_position(message)

    def print_fields(self, index):
        def print_line(line_list, line):
            if line < 9:
                res = "| " + str(line + 1) + " |"
            else:
                res = "| " + str(line + 1) + "|"
            for i in line_list:
                res += " " + i + " |"
            return res

        field1 = self.fields[index].field_with_ships()
        if index == 0:
            field2 = self.fields[index + 1].field_without_ships()
        else:
            field2 = self.fields[index - 1].field_without_ships()

        field_str =  "+---" * 11 + "+" + " " * 5 +  "+---" * 11 + "+\n"
        field_str += print_line("ABCDEFGHIJ", -1) + " " * 5 + print_line("ABCDEFGHIJ", -1) + "\n"
        field_str += "+---" * 11 + "+" + " " * 5 + "+---" * 11 + "+\n"
        for line in range(10):
            field_str += print_line(field1[line], line) + " " * 5 + print_line(field2[line], line) + "\n"
            field_str += "+---" * 11 + "+" + " " * 5 + "+---" * 11 + "+\n"
        print(field_str, end="")
