from .rooms import Room
from .exits import Exit
from .game import Game
from .parsers import Parser
from . import map


def main():
    start_room = map.load_game_map('./rooms.yaml')

    game = Game(start_room)
    parser = Parser(game)

    while True:
        print game.display_room(game.current_room)

        input = raw_input('> ')
        command, arg = parser.parse(input)
        result = getattr(game, command)(arg)
        if result is not None:
            print result
        print
