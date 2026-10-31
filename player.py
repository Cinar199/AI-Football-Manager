class Player:
    def __init__(self, name, position, ovr):
        self.name = name
        self.position = position
        self.ovr = max(1, min(99, int(ovr)))

    def info(self):
        return {
            "name": self.name,
            "position": self.position,
            "OVR": self.ovr
        }
