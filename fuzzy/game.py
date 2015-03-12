import yaml

from .rooms import Room
from .exits import Exit


class Game(object):
    def __init__(self, start_room):
        self.start_room = start_room
        self.current_room = start_room

    def display_room(self, room):
        return str(room)

    def get_start_room(self):
        return self.start_room

    def follow_exit(self, exit):
        self.current_room = exit.target

    def invalid_input(self, _):
        return "I'm sorry, what?"


def load_game_map(path):
    with open(path) as fi:
        data = yaml.load(fi)

    rooms = {}

    for room_id, room_data in data.items():
        rooms[room_id] = Room(room_id, room_data['description'])

    for room_id, room_data in data.items():
        room = rooms[room_id]
        for target_room_id, exit_description in room_data['exits'].items():
            target_room = rooms[target_room_id]
            room.add_exit(Exit(target_room, exit_description))

    return rooms['start']
