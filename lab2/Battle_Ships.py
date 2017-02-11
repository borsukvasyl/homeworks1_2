import os
import game


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
        if battle_ships.fields[next_player].check_killed(coordinates):
            next_message = "Killed!!! Enter next coordinates: "
        else:
            next_message = "Landed! Enter next coordinates: "
    else:
        next_message = "Enter coordinates: "
    if not landed:
        battle_ships.current_player = next_player
    os.system("CLS")
