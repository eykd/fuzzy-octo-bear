from unittest import TestCase
from ensure import ensure

from fuzzy.game import Game
from fuzzy.rooms import Room


class GameTests(TestCase):
    def setUp(self):
        self.start_room = Room("Here we are.")
        self.game = Game(self.start_room)

    def test_it_should_obtain_a_room(self):
        ensure(self.game.get_start_room).called_with().is_a(Room)

    def test_it_should_display_a_room(self):
        ensure(self.game.display_room).called_with(self.start_room).equals(self.start_room.description)
