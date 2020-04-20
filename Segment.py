from Vector import Vector
import math, random


class Segment:
    def __init__(self, initial, length):
        self.length = length
        self.angle = 0
        self.a = Vector()
        self.b = Vector()
        self.calculate_b()

        if isinstance(initial, Segment):
            self.child = initial
            self.follow(self.child)
        else:
            self.a = Vector(initial[0], initial[1])
            self.calculate_b()
            self.child = None

        self.color = "#{0:02X}{1:02X}{2:02X}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def update(self):
        self.calculate_b()

    def calculate_b(self):
        x = self.a.x + math.cos(self.angle) * self.length
        y = self.a.y + math.sin(self.angle) * self.length

        self.b.set(x, y)

    def show(self, canvas):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=self.color)

    def follow(self, tx, ty=None):
        if ty:
            t = Vector.sub(Vector(tx, ty), self.a)
            self.b.set(tx, ty)
        else:
            t = Vector.sub(Vector(tx.a.x, tx.a.y), self.a)
            self.b.set(tx.a.x, tx.a.y)
        t.set_mag(self.length)
        t.mult(-1)

        self.a = self.b.copy()
        self.a.add(t)


        # print(f"a = ({self.a}), b = ({self.b})")