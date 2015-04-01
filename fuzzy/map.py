import yaml
from .rooms import Room
from .exits import Exit

def load_room(rooms, room_id, room_data):
    rooms[room_id] = Room(room_id, room_data['description'])


def load_exits(rooms, room_id, room_data):
    room = rooms[room_id]
    for target_room_id, exit_description in room_data['exits'].items():
        target_room = rooms[target_room_id]
        room.add_exit(Exit(target_room, exit_description))


def is_room(data):
    return 'description' in data


def has_exits(data):
    return 'exits' in data


def has_map(data):
    return 'map' in data


def load_game_map(path):
    with open(path) as fi:
        data = yaml.load(fi)

    rooms = {}

    # First pass, load rooms
    for room_id, room_data in data.items():
        if is_room(room_data):
            load_room(rooms, room_id, room_data)

    # Second pass, load exits
    for room_id, room_data in data.items():
        if is_room(room_data) and has_exits(room_data):
            load_exits(rooms, room_id, room_data)

    # Third pass, handle maps.
    for room_id, room_data in data.items():
        if has_map(room_data):
            load_map(rooms, room_id, room_data)

    return rooms['start']
