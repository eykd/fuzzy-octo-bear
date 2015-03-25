class Parser(object):
    def __init__(self, game):
        self.game = game

    def parse(self, input):
        for exit in self.game.current_room.exits:
            matches_desc = self._match_on(exit.description, input)
            matches_alias = self._match_on(exit.aliases, input)
            if matches_desc or matches_alias:
                return ('follow_exit', exit)

        if self._match_on('quit', input):
            return ('quit', None)

        return ('invalid_input', None)

    def _normalize(self, s):
        return s.lower()

    def _match_on(self, pattern, input):
        pattern = self._normalize(pattern)
        input = self._normalize(input)
        return (
            input == pattern
            or
            any(input == p for p in pattern.split())
        )
