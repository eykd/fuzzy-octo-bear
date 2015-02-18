from .rooms import Room
from .game import Game


def main():
    game = Game(Room("This is the first room."))

    print game.display_room(game.get_start_room())
    while True:
        input = raw_input('> ')
        print game.display_room(game.get_start_room())
        print input
