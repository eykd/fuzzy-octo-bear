from unittest import TestCase
from ensure import ensure

from fuzzy import rooms, exits


class RoomTest(TestCase):
    def setUp(self):
        self.description = "This is a room"
        self.room = rooms.Room('room1', self.description)
        self.room2 = rooms.Room('room2', self.description * 2)

    def test_it_should_initialize_with_description(self):
        ensure(self.room.description).equals(self.description)

    def test_it_should_stringify_as_the_description(self):
        ensure(str).called_with(self.room).equals(self.description)

    def test_it_should_have_exits(self):
        ensure(self.room).has_attribute('exits').which.is_a(list)

    def test_it_should_be_able_to_add_new_exits(self):
        my_exit = exits.Exit(self.room2, "My shiny new exit.")
        ensure(self.room.add_exit).called_with(my_exit).is_none()
        ensure(self.room.exits).has_length(1)
        ensure(self.room.exits).contains(my_exit)
