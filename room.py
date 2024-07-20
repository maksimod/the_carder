class Room:
    def __init__(self, index):
        # Doors dictionary with default values indicating no passage (-1 means no connection)
        self.doors = {'l': -1, 'r': -1, 'u': -1, 'd': -1}
        self.index = index

    def __repr__(self):
        return f"Room(index={self.index}, doors={self.doors})"
