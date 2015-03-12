

class Parser(object):
    def __init__(self, game):
        self.game = game

    def parse(self, input):
        for exit in self.game.current_room.exits:
            matches = (
                exit.description.lower().startswith(input.lower())
                or
                exit.description.lower().endswith(input.lower())
            )
            if matches:
                return ('follow_exit', exit)

        return ('invalid_input', None)
