import math

class Vector:
    def __init__(self, body, vx=0, vy=0):
        self.body = body
        self.vx = vx
        self.vy = vy
        self.abs = (vx ** 2 + vy ** 2) ** 0.5

    def setByDirection(self, dir):
        self.abs = (self.vx ** 2 + self.vy ** 2) ** 0.5
        self.vx, self.vy = 0, 0
        horDir, vertDir = dir
        self.vx = self.abs / ((vertDir ** 2 + horDir ** 2) ** 0.5) * horDir
        self.vy = self.abs / ((vertDir ** 2 + horDir ** 2) ** 0.5) * vertDir




    def setXY(self, x, y):
        self.vx = x
        self.vy = y

    def move(self):
        self.body.shape.x += math.trunc(self.vx)
        self.body.shape.y += math.trunc(self.vy)
        