from Vasyl_Borsuk_lab3 import *


agent = Agent()
while True:
    action = input(">>> ")
    if action == "add":
        agent.add_property()
    elif action == "display":
        agent.display_properties()
    elif action == "remove":
        agent.remove_properties_by_key(input("Enter a key: "),
                                       input("Enter a value: "),
                                       input("Enter a percentage: "))
    elif action == "display by key":
        agent.display_properties_by_key(input("Enter a key: "),
                                       input("Enter a value: "),
                                       input("Enter a percentage: "))
    elif action == "exit":
        break
