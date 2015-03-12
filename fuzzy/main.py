from .rooms import Room
from .exits import Exit
from .game import Game, load_game_map
from .parsers import Parser


def main():
    start_room = load_game_map('./rooms.yaml')

    game = Game(start_room)
    parser = Parser(game)

    while True:
        print game.display_room(game.current_room)
        print
        print "Paths:"
        for exit in game.current_room.exits:
            print '  ' + exit.description
        print

        input = raw_input('> ')
        command, arg = parser.parse(input)
        result = getattr(game, command)(arg)
        if result is not None:
            print result
        print
