import textwrap
from unittest import TestCase
from ensure import ensure

from fuzzy.game import Game
from fuzzy.rooms import Room
from fuzzy.exits import Exit


class GameTests(TestCase):
    def setUp(self):
        self.room1 = Room("room1", "Room 1")
        self.room2 = Room("room2", "Room 2")
        self.room1.add_exit(Exit(self.room2, "North to room 2"))
        self.room2.add_exit(Exit(self.room1, "South to room 1"))
        self.start_room = self.room1
        self.game = Game(self.start_room)

    def test_it_should_obtain_a_room(self):
        ensure(self.game.start_room).is_(self.start_room)

    def test_it_should_display_a_room(self):
        ensure(self.game.display_room).called_with(self.start_room).equals(
            textwrap.dedent(
                """\
                Room 1

                Paths:
                  North to room 2
                """)
        )

    def test_it_should_initialize_with_location_as_start_room(self):
        ensure(self.game.current_room).equals(self.game.start_room)

    def test_it_should_follow_an_exit(self):
        ensure(self.game.current_room).equals(self.room1)
        ensure(self.game.follow_exit).called_with(self.room1.exits[0]).is_(None)
        ensure(self.game.current_room).equals(self.room2)

    def test_it_should_handle_invalid_input(self):
        ensure(self.game.invalid_input).called_with(None).equals("I'm sorry, what?")
