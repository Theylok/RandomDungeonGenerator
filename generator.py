"""Simple dungeon generator"""
import random

class Rect(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    """
    Check wether if 2 rect overlap or touch
    """
    def overlap(self, other) -> bool:
        if ((self.x + self.w < other.x)
                or (self.x > other.x + other.w)
                or (self.y + self.h < other.y)
                or (self.y > other.y + other.h)):
            return False
        else:
            return True

    """
    Check if rect A fully contains rect B
    """
    def contain(self, other) -> bool:
        if ((self.x < other.x)
                and (self.x + self.w > other.x + other.w)
                and (self.y < other.y)
                and (self.y + self.h > other.y + other.h)):
            return True
        else:
            return False

"""
Simple dungeon generator
"""
class Generator(object):
    WALL = "#"
    ROOM = " "
    CORRIDOR = "0"
    DOOR = "+"

    def __init__(self, seed, size):
        self.seed = seed
        random.seed(seed)

        self.size = self.width, self.height = size
        self.rect = Rect(0, 0, self.width, self.height)
        self.map = []

        self.min_room_size = 3
        self.max_room_size = 7
        self.max_rooms = 30
        self.max_room_retries = 100

        self.rooms = []

    def run(self):
        # Initially fill map with all walls
        for x in range(self.width):
            self.map.insert(x, [])
            for y in range(self.height):
                self.map[x].insert(y, self.WALL)

        # Create rooms
        num_rooms = 0
        for i in range(self.max_room_retries):
            room_size = self._get_random_room()
            room_pos = self._get_random_position()
            rect = Rect(room_pos[0], room_pos[1], room_size[0], room_size[1])

            if not self.rect.contain(rect):
                continue

            room_okay = True
            for other_room in self.rooms:
                if rect.overlap(other_room):
                    room_okay = False
                    break

            if not room_okay:
                continue

            self.rooms.append(rect)
            num_rooms = len(self.rooms)

            if num_rooms >= self.max_rooms:
                break

        # Add rooms to map
        for room in self.rooms:
            for x in range(room.x, room.x + room.w):
                for y in range(room.y, room.y + room.h):
                    self.map[x][y] = self.ROOM

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.map[x][y], end="")

            print("")

    def print_stats(self):
        print("Number of rooms: {}".format(len(self.rooms)))

    def _get_random_room(self):
        width = random.randint(self.min_room_size, self.max_room_size)
        height = random.randint(self.min_room_size, self.max_room_size)
        return width, height

    def _get_random_position(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return x, y


if __name__ == "__main__":
    gen = Generator("rngesus", [91, 45])
    gen.run()
    gen.draw()
    gen.print_stats()
