

class Parser(object):
    def __init__(self, game):
        self.game = game

    def parse(self, input):
        return ('follow_exit', self.game.current_room.exits[0])
