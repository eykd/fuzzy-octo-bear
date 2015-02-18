from unittest import TestCase
from ensure import ensure

from fuzzy import rooms


class RoomTest(TestCase):
    def setUp(self):
        self.description = "This is a room"
        self.room = rooms.Room(self.description)

    def test_it_should_initialize_with_description(self):
        ensure(self.room.description).equals(self.description)

    def test_it_should_stringify_as_the_description(self):
        ensure(str).called_with(self.room).equals(self.description)

    def test_it_should_have_exits(self):
        ensure(self.room).has_attribute('exits').which.is_a(list)
