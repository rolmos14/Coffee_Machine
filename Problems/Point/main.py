import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point_b):
        return math.sqrt((self.x - point_b.x) ** 2 + (self.y - point_b.y) ** 2)

