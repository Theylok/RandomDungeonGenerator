import random
from dungeon import Dungeon
from base_generator import BaseGenerator
from rect import Rect

class RoomGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

        self.min_size = 3
        self.max_size = 7
        self.max_rooms = 30
        self.max_tries = 100

        self._rooms = []

    def run(self, dungeon: Dungeon):
        num_rooms = 0
        for i in range(self.max_tries):
            room_size = self._get_random_room()
            room_pos = self._get_random_position(dungeon)
            rect = Rect(room_pos[0], room_pos[1], room_size[0], room_size[1])

            if not dungeon.rect.contain(rect):
                continue

            room_okay = True
            for other_room in self._rooms:
                if rect.overlap(other_room):
                    room_okay = False
                    break

            if not room_okay:
                continue

            self._rooms.append(rect)
            num_rooms = len(self._rooms)

            if num_rooms >= self.max_rooms:
                break

        for room in self._rooms:
            for x in range(room.x, room.x + room.w):
                for y in range(room.y, room.y + room.h):
                    dungeon.map[x][y] = " "

    def _get_random_room(self):
        width = random.randint(self.min_size, self.max_size)
        height = random.randint(self.min_size, self.max_size)
        return width, height

    def _get_random_position(self, dungeon: Dungeon):
        x = random.randint(0, dungeon.width)
        y = random.randint(0, dungeon.height)
        return x, y
