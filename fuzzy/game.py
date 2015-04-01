import sys


class Game(object):
    def __init__(self, start_room):
        self.start_room = start_room
        self.current_room = start_room

    def display_room(self, room):
        display = [str(room)]
        if room.exits:
            display.append('\n\nPaths:\n')
            for exit in room.exits:
                display.extend(('  ', str(exit), '\n'))
        return ''.join(display)

    def get_start_room(self):
        return self.start_room

    def follow_exit(self, exit):
        self.current_room = exit.target

    def invalid_input(self, _):
        return "I'm sorry, what?"

    def quit(self, _):
        sys.exit()
