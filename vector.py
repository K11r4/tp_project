import math

class Vector:
    def __init__(self, body, speed, vx=0, vy=0):
        self.body = body
        self.vx = vx
        self.vy = vy
        self.abs = speed

    def setSpeed(self, vel):
        self.vx = self.vx * (vel / self.abs)
        self.vy = self.vy * (vel / self.abs)
        self.abs = vel

    def setDirection(self, dx, dy):
        if dx ** 2 + dy ** 2 == 0:
            self.vx, self.vy = 0, 0
        else: 
            self.vx = self.abs / ((dx ** 2 + dy ** 2) ** 0.5) * dx
            self.vy = self.abs / ((dx ** 2 + dy ** 2) ** 0.5) * dy

    def move(self):
        self.body.shape.x += math.trunc(self.vx)
        self.body.shape.y += math.trunc(self.vy)
        