import math


class Vector:
    def __init__(self, x=None, y=None):
        self.x = x or 0
        self.y = y or 0

    def __add__(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def __sub__(self, v):
        self.x -= v.x
        self.y -= v.y
        return self

    def __str__(self):
        return f"{self.x}, {self.y}"

    def add(self, v):
        if isinstance(v, Vector):
            self + v

    def set(self, x, y):
        self.x = x
        self.y = y

    def normalize(self):
        d = math.sqrt(self.x**2+self.y**2)
        self.div(d)

    def set_mag(self, mag):
        self.normalize()
        self.mult(mag)

    def mult(self, n):
        if isinstance(n, Vector):
            return self.x * n.x + self.y * n.y
        else:
            self.x *= n
            self.y *= n

    def copy(self):
        return Vector(self.x, self.y)

    def div(self, n):
        if type(n) == int or type(n) == float:
            self.x /= n
            self.y /= n

    @staticmethod
    def sub(v1, v2):
        x = v1.x - v2.x
        y = v1.y - v2.y

        return Vector(x, y)
