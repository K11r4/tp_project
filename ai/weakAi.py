import random, time

class WeakAI:
    def __init__(self, body, target, minDist = 350, delay=4):
        self.body = body
        self.target = target
        self.lastTime = time.time()
        self.minDist = minDist
        self.body.velocity.setDirection(0, 0)
        self.agression = False
        self.delay = delay

   

    def update(self):
        dx = self.target.shape.centerx - self.body.shape.centerx
        dy = self.target.shape.centery - self.body.shape.centery

        if (self.body.direction == "R" and dx > 0 or self.body.direction == "L" and dx < 0) \
                and dx ** 2 + dy ** 2 < self.minDist ** 2:
            self.agression = self.agression or True

        if self.agression:
            if self.agression and 60 ** 2 < dx ** 2 + dy ** 2:
                self.body.walk(dx, dy)
            else:
                self.body.attack()
        else:
            now = time.time()
            if now - self.lastTime > self.delay:
                Dir =  ("R" if self.body.direction == "L" else "L")
                self.body.stand(Dir)
                self.lastTime = now
        """
       
        if (self.direction == "R" and dx > 0 or self.direction == "L" and dx < 0):

        if  32 ** 2 < dx ** 2 + dy ** 2 < self.minDist ** 2:
            self.body.walk(dx, dy)
        else:
            self.body.stand()
        """