import auth


class BattleshipAuth:
    def __init__(self, authorizor):
        """
        Construct Battleship game authorizor with
        one admin (can add new users).
        :param authorizor: Authorizor object
        """
        self.__authorizor = authorizor
        self.__authorizor.authenticator.add_user("VasikoBestProgrammer", "11111111")
        self.__authorizor.add_permission("admin")
        self.__authorizor.permit_user("admin", "VasikoBestProgrammer")
        self.__authorizor.add_permission("play")
        self.__authorizor.permit_user("play", "VasikoBestProgrammer")

    def login(self):
        """
        Login user to the system.
        :return: None
        """
        self.__authorizor.authenticator.login(input("Enter username: "),
                                              input("Enter password: "))

    def logout(self):
        """
        Logout user.
        :return: None
        """
        self.__authorizor.authenticator.logout()

    def add_user(self):
        """
        Add new user.
        :return: None
        """
        if self.__authorizor.authenticator.logged_in_user in\
           self.__authorizor.permissions["admin"]:
            self.__authorizor.authenticator.add_user(input("Enter username: "),
                                                     input("Enter password: "))
        else:
            raise auth.NotPermittedError(self.__authorizor.authenticator.logged_in_user)

    def permit_user(self):
        if self.__authorizor.authenticator.logged_in_user in\
           self.__authorizor.permissions["admin"]:
            self.__authorizor.permit_user(input("Enter permission: "),
                                          input("Enter username: "))
        else:
            raise auth.NotPermittedError(self.__authorizor.authenticator.logged_in_user)

    def play_battleship(self):
        if self.__authorizor.authenticator.logged_in_user in\
           self.__authorizor.permissions["play"]:
            print("(\/)_(^-^)_(\/)")
        else:
            raise auth.NotPermittedError(self.__authorizor.authenticator.logged_in_user)

    def menu(self):
        while True:
            command = input(">>> Enter command: ")
            if command == "help()":
                print("login()           - login\n"
                      "logout()          - logout\n"
                      "add_user()        - add user\n"
                      "permit_user()     - permit user\n"
                      "play_battleship() - play game\n"
                      "exit()            - exit")
            elif command == "exit()":
                break
            else:
                try:
                    eval("self.{}".format(command))
                except (AttributeError, SyntaxError, TypeError):
                    print("No such command!")
                except auth.UsernameAlreadyExists as e:
                    print("Sorry, username {} already exist".format(e))
                except auth.PasswordTooShort:
                    print("Sorry, that password is too short")
                except auth.InvalidUsername as e:
                    print("Sorry, username {} does not exist".format(e))
                except auth.InvalidPassword:
                    print("Sorry, incorrect password")
                except auth.NotPermittedError as e:
                    print("Sorry, {} have not permission".format(e))
                except auth.AlreadyLoggedIn:
                    print("Sorry, you are already logged in")
                except auth.PermissionError:
                    print("Sorry, permission already exist")


authenticator = auth.Authenticator()
authorizor = auth.Authorizor(authenticator)
game = BattleshipAuth(authorizor)
game.menu()
