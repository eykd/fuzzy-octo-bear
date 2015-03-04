

class Room(object):
    def __init__(self, description):
        self.description = description
        self.exits = []

    def __str__(self):
        return self.description

    def __repr__(self):
        return "<Room: %s>" % self

    def add_exit(self, exit):
        self.exits.append(exit)
