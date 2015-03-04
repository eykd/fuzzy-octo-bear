from unittest import TestCase
from ensure import ensure

from fuzzy.game import Game
from fuzzy.rooms import Room
from fuzzy.exits import Exit


class GameTests(TestCase):
    def setUp(self):
        self.room1 = Room("Room 1")
        self.room2 = Room("Room 2")
        self.room1.add_exit(Exit(self.room2, "North to room 2"))
        self.room2.add_exit(Exit(self.room1, "South to room 1"))
        self.start_room = self.room1
        self.game = Game(self.start_room)

    def test_it_should_obtain_a_room(self):
        ensure(self.game.start_room).is_(self.start_room)

    def test_it_should_display_a_room(self):
        ensure(self.game.display_room).called_with(self.start_room).equals(self.start_room.description)

    def test_it_should_initialize_with_location_as_start_room(self):
        ensure(self.game.current_room).equals(self.game.start_room)

    def test_it_should_follow_an_exit(self):
        ensure(self.game.current_room).equals(self.room1)
        ensure(self.game.follow_exit).called_with(self.room1.exits[0]).is_(self.room2)
        ensure(self.game.current_room).equals(self.room2)
