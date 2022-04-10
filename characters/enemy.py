from body import Body
from vector import Vector
from spritesheet import SpriteSheet
from ai.weakAi import WeakAI
from characters.weapon import Weapon
import pygame
from pygame.locals import *

class Enemy(Body):
    def __init__(self, x, y, target):
        width, height = 17 * 4, 26 * 4
        self.target = target
        self.imageSource = SpriteSheet("./src/enemy.png", 248, 160)
        self.animations = {
            "idleR": self.imageSource.getAnimation(0, 1),
            "idleL": self.imageSource.getAnimation(18, 1),
            "walkR": self.imageSource.getAnimation(0, 1),
            "walkL": self.imageSource.getAnimation(18, 1)
        }

        super().__init__(pygame.Rect((x, y), (width, height)),
                        Vector(self, 8),
                        self.imageSource.getAnimation(0, 1),
                        pygame.Rect((76, 52), (width, height))
        )

        self.ai = WeakAI(self, target)
        self.direction = "R"

    def walk(self, dx, dy):
        self.velocity.setDirection(dx, dy)
        self.direction = ("R" if dx >= 0 else "L")
        self.view = self.animations["walk" + self.direction]

    def stand(self, dir):
        self.direction = dir
        self.velocity.setDirection(0, 0)
        self.view = self.animations["idle" + self.direction]

    def attack(self):
        pass

    def update(self):
        super().update()
        self.velocity.move()

    
        self.ai.update()
        self.view.update()

    def onCollision(self, obj):
        if isinstance(obj, Weapon):
            self.alive = False
