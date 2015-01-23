class Point:
    "A class implementation of 2-Dimensional point."

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '( % d, % d)' % (self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.x

    def __sub__(self, other):
        return self.x - other.x, self.y - other.x


point1 = Point(8, 5)
point2 = Point(-6, 1)

print(point1 + point2)  # (2, 6)
print(point1 - point2)  # (14, 4)a