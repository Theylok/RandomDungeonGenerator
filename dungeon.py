from rect import Rect

class Dungeon(object):
    def __init__(self, width: int, height: int, wall_char="#"):
        self._width = width
        self._height = height
        self._wall_char = wall_char

        self.map = []
        for x in range(self.width):
            self.map.append([])

            for y in range(self.height):
                self.map[x].append(self._wall_char)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def rect(self) -> Rect:
        return Rect(0, 0, self.width, self.height)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print("{}".format(self.map[x][y]), end="")

            print()
