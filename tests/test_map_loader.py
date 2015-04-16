from unittest import TestCase
from ensure import ensure

from path import path

from fuzzy.map import load_game_map
from fuzzy.rooms import Room
from fuzzy.exits import Exit


PATH = path(__file__).abspath().dirname()


class MapLoaderTests(TestCase):
    def setUp(self):
        self.filename = PATH / 'rooms.yaml'

    def test_it_should_construct_a_map_from_the_yaml_file(self):
        start_room = load_game_map(self.filename)
        ensure(start_room).is_a(Room)
        ensure(start_room.exits).has_length(2)
        ensure(start_room.exits).is_a(list).of(Exit)
        ensure(start_room.exits[0].target).is_a(Room)
        ensure(start_room.exits[0].target).is_not(start_room)

        room_3 = start_room.exits[1].target
        ensure(room_3.exits).has_length(4)
        ensure(room_3.exits).is_a(list).of(Exit)

        room_6 = room_3.exits[2].target
        ensure(room_6).is_a(Room)
        ensure(room_6.exits).has_length(2)
        ensure(room_6.description).equals("A nondescript room")

        room_7 = room_3.exits[3].target
        ensure(room_7).is_a(Room)
        ensure(room_7.exits).has_length(2)
        ensure(room_7.description).equals("A nondescript room")

        ensure(room_6).is_not(room_7)
