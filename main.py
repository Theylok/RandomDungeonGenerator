import random

from dungeon import Dungeon
from room_generator import RoomGenerator

random.seed("rngesus")

DUNGEON = Dungeon(51, 25)

ROOMS = RoomGenerator()
ROOMS.run(DUNGEON)

DUNGEON.draw()
