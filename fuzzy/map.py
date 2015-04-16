from copy import deepcopy

import yaml
from .rooms import Room
from .exits import Exit

def _load_room(rooms, room_id, room_data):
    rooms[room_id] = Room(room_id, room_data['description'])


def _load_exits(rooms, room_id, room_data):
    room = rooms[room_id]
    for target_room_id, exit_description in room_data['exits'].items():
        target_room = rooms[target_room_id]
        room.add_exit(Exit(target_room, exit_description))


def _is_room(data):
    return 'description' in data


def _has_exits(data):
    return 'exits' in data


def _has_grid_map(data):
    return 'map' in data


def _load_grid_map(rooms, room_id, room_data):
    grid_map = []
    for line in room_data['map']['grid'].splitlines():
        if line.strip():
            row = line.strip().split()
            grid_map.append(row)

    legend = room_data['map']['legend']

    room_map = []
    for row in grid_map:
        room_row = []
        for key in row:
            directive = legend[key]
            name = directive[1:]
            if directive.startswith('-'):
                # make a copy
                room = deepcopy(rooms[name])
            elif directive.startswith('='):
                # get a reference from rooms
                room = rooms[name]
            room_row.append(room)
        room_map.append(room_row)

    for row, row_of_rooms in enumerate(grid_map):
        for col, room in enumerate(row_of_rooms):
            for row_delta, col_delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                try:
                    target_room = room_map[row + row_delta][col + col_delta]
                except IndexError:
                    pass
                else:
                    # Set up the exits
                    pass




def load_game_map(path):
    with open(path) as fi:
        data = yaml.load(fi)

    rooms = {}

    # First pass, load rooms
    for room_id, room_data in data.items():
        if _is_room(room_data):
            _load_room(rooms, room_id, room_data)

    # Second pass, load exits
    for room_id, room_data in data.items():
        if _is_room(room_data) and _has_exits(room_data):
            _load_exits(rooms, room_id, room_data)

    # Third pass, handle maps.
    for room_id, room_data in data.items():
        if _has_grid_map(room_data):
            _load_grid_map(rooms, room_id, room_data)

    return rooms['start']
