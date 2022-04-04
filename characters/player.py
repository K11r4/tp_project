from body import Body
from vector import Vector
from directionController import DirController
import pygame
from pygame.locals import *

class Player(Body):
    def __init__(self, x, y, controller):
        width, height = 32, 32
        self.maxVel = 4
        image = pygame.Surface((width, height))
        image.fill(Color("#3064C8"))

        self.direction = DirController()
        controller.subscribe(KEYUP, self.direction)
        controller.subscribe(KEYDOWN, self.direction)
        super().__init__(pygame.Rect((x, y), (width, height)),
                        Vector(self, 0, 0),
                        image,
                        pygame.Rect((0, 0), (width, height))
        )

    def update(self):
        super().update()
        self.velocity.setXY(self.maxVel * self.direction.horDir, self.maxVel * self.direction.vertDir)
        self.velocity.move()
        
    
