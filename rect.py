class Rect(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def overlap(self, other) -> bool:
        if ((self.x + self.w < other.x)
                or (self.x > other.x + other.w)
                or (self.y + self.h < other.y)
                or (self.y > other.y + other.h)):
            return False
        else:
            return True

    def contain(self, other) -> bool:
        if ((self.x < other.x)
                and (self.x + self.w > other.x + other.w)
                and (self.y < other.y)
                and (self.y + self.h > other.y + other.h)):
            return True
        else:
            return False
