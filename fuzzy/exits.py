

class Exit(object):
    def __init__(self, target_room, description):
        self.target = target_room
        self.description = description

    def __str__(self):
        return self.description

    def __repr__(self):
        return "<Exit: %s>" % self
