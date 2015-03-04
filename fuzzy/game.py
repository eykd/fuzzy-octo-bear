

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
        return self.current_room
