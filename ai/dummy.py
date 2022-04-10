import random, time

class Dummy:
    def __init__(self, body, delay = 5):
        self.body = body
        self.delay = delay
        self.lastTime = time.time()

    def changeDirection(self):
        self.body.velocity.setDirection(random.randint(-10, 10), random.randint(-10, 10))

    def update(self):
        now = time.time()
        if now - self.lastTime > self.delay:
            self.lastTime = now
            self.changeDirection()