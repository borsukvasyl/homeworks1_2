import os
import game

print("""
                 _           _   _   _           _     _
                | |         | | | | | |         | |   (_)
                | |__   __ _| |_| |_| | ___  ___| |__  _ _ __
                | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \\
                | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
                |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/
                                                        | |
                                     |__                |_|
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                  by Vasiko/
 \_________________________________________________________________________|""")


name1, name2 = input("Enter your name: "), input("Enter your name: ")
battle_ships = game.Game(name1, name2)
os.system("CLS")

next_message = "Enter coordinates: "
while True:
    current_player = battle_ships.current_player
    if current_player:
        next_player = 0
    else:
        next_player = 1
    battle_ships.print_fields(current_player)
    coordinates = battle_ships.read_position(current_player, next_message)
    landed = battle_ships.fields[next_player].shoot_at(coordinates)
    if landed:
        if battle_ships.fields[next_player].check_ship_killed(coordinates):
            next_message = "Killed!!! Enter next coordinates: "
        else:
            next_message = "Landed! Enter next coordinates: "
    else:
        next_message = "Enter coordinates: "
    if not landed:
        battle_ships.current_player = next_player
    os.system("CLS")
