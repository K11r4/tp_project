import pygame
from pygame.locals import *

class Camera:
    def __init__(self, bodyToWatch, sizeOfScreen, sizeOfMap, scrollEdge=500):
        self.scrollEdge = scrollEdge
        self.limits = sizeOfMap
        self.body = bodyToWatch

        x = min(self.limits.right, max(self.body.shape.centerx - sizeOfScreen[0] // 2, self.limits.left))
        y = min(self.limits.bottom, max(self.body.shape.centery - sizeOfScreen[1] // 2, self.limits.top))

        self.shape = Rect((x, y), sizeOfScreen)

    def update(self):
        if self.body.shape.centerx < self.shape.left + self.scrollEdge:
            self.shape.left = max(self.body.shape.centerx - self.scrollEdge, self.limits.left)
        
        if  self.body.shape.centerx > self.shape.right - self.scrollEdge:
            self.shape.right = min(self.body.shape.centerx + self.scrollEdge, self.limits.right)

        if self.body.shape.centery < self.shape.top + self.scrollEdge:
            self.shape.top = max(self.body.shape.centery - self.scrollEdge, self.limits.top)
        
        if  self.body.shape.centery > self.shape.bottom - self.scrollEdge:
            self.shape.bottom = min(self.body.shape.centery + self.scrollEdge, self.limits.bottom)