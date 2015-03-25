class Exit(object):
    def __init__(self, target_room, description, aliases=''):
        self.target = target_room
        self.description = description
        self.aliases = aliases

    def __str__(self):
        return self.description

    def __repr__(self):
        return "<Exit: %s>" % self
