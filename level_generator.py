from room import Room

class LevelGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rooms = []
        self.generate_rooms()

    def generate_rooms(self):
        room_index = 0
        # Create rooms
        for y in range(self.height):
            row = []
            for x in range(self.width):
                room = Room(room_index)
                row.append(room)
                room_index += 1
            self.rooms.append(row)
        
        # Connect rooms
        for y in range(self.height):
            for x in range(self.width):
                current_room = self.rooms[y][x]
                if x > 0:  # Connect left
                    current_room.doors['l'] = self.rooms[y][x - 1].index
                if x < self.width - 1:  # Connect right
                    current_room.doors['r'] = self.rooms[y][x + 1].index
                if y > 0:  # Connect up
                    current_room.doors['u'] = self.rooms[y - 1][x].index
                if y < self.height - 1:  # Connect down
                    current_room.doors['d'] = self.rooms[y + 1][x].index

    def get_rooms(self):
        return [room for row in self.rooms for room in row]

# # Example usage
# if __name__ == "__main__":
#     level_generator = LevelGenerator(3, 3)
#     rooms = level_generator.get_rooms()
#     for room in rooms:
#         print(room)
