from unittest import TestCase
from ensure import ensure

from fuzzy.parsers import Parser
from fuzzy.game import Game
from fuzzy.rooms import Room
from fuzzy.exits import Exit


class ParserTests(TestCase):
    def setUp(self):
        self.room1 = Room("Room 1")
        self.room2 = Room("Room 2")
        self.room3 = Room("Room 3")

        self.exit1_2 = Exit(self.room2, "North to room 2")
        self.room1.add_exit(self.exit1_2)

        self.exit1_3 = Exit(self.room3, "East to room 3")
        self.room1.add_exit(self.exit1_3)

        self.exit2_1 = Exit(self.room1, "South to room 1")
        self.room2.add_exit(self.exit2_1)

        self.exit2_3 = Exit(self.room3, "East to room 3")
        self.room2.add_exit(self.exit2_3)

        self.exit3_1 = Exit(self.room1, "West to room 1")
        self.room3.add_exit(self.exit3_1)

        self.exit3_2 = Exit(self.room2, "West to room 2")
        self.room3.add_exit(self.exit3_2)

        self.game = Game(self.room1)
        self.parser = Parser(self.game)

    def test_it_should_tell_what_to_do_when_accepting_directional_input(self):
        ensure(self.parser.parse).called_with('North to room 2').equals(('follow_exit', self.exit1_2))
        ensure(self.parser.parse).called_with('north').equals(('follow_exit', self.exit1_2))
        ensure(self.parser.parse).called_with('n').equals(('follow_exit', self.exit1_2))

        ensure(self.parser.parse).called_with('East to room 3').equals(('follow_exit', self.exit1_3))
        ensure(self.parser.parse).called_with('east').equals(('follow_exit', self.exit1_3))
        ensure(self.parser.parse).called_with('e').equals(('follow_exit', self.exit1_3))
