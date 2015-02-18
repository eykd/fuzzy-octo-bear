from unittest import TestCase
from ensure import ensure

from fuzzy import exits
from fuzzy import rooms


class ExitTest(TestCase):
    def setUp(self):
        self.description = "This is an exit"
        self.room = rooms.Room("Somewhere else")
        self.exit = exits.Exit(self.room, self.description)

    def test_it_should_initialize_with_description(self):
        ensure(self.exit.description).equals(self.description)

    def test_it_should_stringify_as_the_description(self):
        ensure(str).called_with(self.exit).equals(self.description)

    def test_it_should_have_a_torget_room(self):
        ensure(self.exit).has_attribute('target').which.is_(self.room)
