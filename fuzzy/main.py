from .rooms import Room
from .exits import Exit
from .game import Game
from .parsers import Parser


def main():
    room1 = Room("This is the first room.")
    room2 = Room("This is the second room.")
    room1 = Room("Room 1")
    room2 = Room("Room 2")
    exit1 = Exit(room2, "North to room 2")
    room1.add_exit(exit1)
    exit2 = Exit(room1, "South to room 1")
    room2.add_exit(exit2)

    game = Game(room1)
    parser = Parser(game)

    print game.display_room(game.current_room)

    while True:
        input = raw_input('> ')
        command, arg = parser.parse(input)
        getattr(game, command)(arg)
        print game.display_room(game.current_room)
