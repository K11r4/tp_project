import pygame
from pygame.locals import *
from sprite import Sprite 
from body import Body

class HealthBar(Body):
    def __init__(self, body, maxVal):
        width, height = 150, 15
        self.body = body
        self.maxVal = maxVal

        super().__init__(pygame.Rect(15, 15, width, height),
                        None,
                        Sprite(pygame.Surface((width, height))),
                        pygame.Rect(15, 15, width, height)
        )

        self.useCamera = False
        
    def update(self):
        self.view.img.fill((1, 1, 1))
        pygame.draw.rect(
            self.view.img, 
            (180, 0, 20), 
            pygame.Rect(3, 3, int((self.shape.w - 6) * self.body.hp / self.maxVal), self.shape.h - 6)
        )
        

