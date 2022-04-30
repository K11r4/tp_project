import pygame, time
from pygame.locals import *
from body import Body
from sprite import Sprite

class Weapon(Body):
    def __init__(self, x, y, start=0.3, end=0.5):
        self.start = start
        self.end = end
        width, height = 248, 160
        super().__init__(
            pygame.Rect((x, y), (width, height)),
            None,
            None, 
            pygame.Rect((0, 0), (0, 0))
        )
        self.startTime = time.time()
    
    def update(self):
        if time.time() - self.startTime > self.start:
            self.collisionShape.w = self.shape.w
            self.collisionShape.h = self.shape.height
            
        if time.time() - self.startTime > self.end:
            self.alive = False
    
