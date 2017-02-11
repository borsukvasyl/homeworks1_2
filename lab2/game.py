import field, player


class Game():
    def __init__(self):
        self.fields = [field.Field(), field.Field()]
        self.players = [player.Player(), player.Player()]
        self.current_player = 0
