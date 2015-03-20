

class Parser(object):
    def __init__(self, game):
        self.game = game

    def parse(self, input):
        for exit in self.game.current_room.exits:
            matches = self._match_on(exit.description, input)
            if matches:
                return ('follow_exit', exit)

        if self._match_on('quit', input):
            return ('quit', None)

        return ('invalid_input', None)

    def _normalize(self, s):
        return s.lower()

    def _match_on(self, pattern, input):
        pattern = self._normalize(pattern)
        input = self._normalize(input)
        return any(p.startswith(input) for p in pattern.split())
