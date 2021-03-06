from body import Body
from vector import Vector
from spritesheet import SpriteSheet
from ai.weakAi import WeakAI
from objects.weapon import Weapon
import pygame
from pygame.locals import *
import time

class Enemy(Body):
    def __init__(self, x, y, target, scene):
        width, height = 17 * 4, 26 * 4
        self.target = target
        self.scene = scene
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
                        pygame.Rect((76, 52), (width, height)),
                        90
        )

        self.ai = WeakAI(self, target)
        self.direction = "R"
        self.appliedWeapons = set()
        self.timeToFreeze = 0


    def walk(self, dx, dy):
        self.velocity.setDirection(dx, dy)
        self.direction = ("R" if dx >= 0 else "L")
        self.view = self.animations["walk" + self.direction]

    def stand(self, dir):
        self.direction = dir
        self.velocity.setDirection(0, 0)
        self.view = self.animations["idle" + self.direction]

    def attack(self):
        if self.timeToFreeze > time.time():
            return
        hit = Weapon(self.shape.x, self.shape.y, self, 0, 0.3)
        self.scene.objects.append(hit)
        self.scene.collider.addActiveShape(hit)
        self.freeze(1)

    def freeze(self, dt):
        self.timeToFreeze = time.time() + dt


    def update(self):
        super().update()
        if time.time() > self.timeToFreeze:
            self.velocity.move()

    
        self.ai.update()
        self.view.update()

    def onCollision(self, obj):
        if isinstance(obj, Weapon):
            if (obj.body != self) and (obj not in self.appliedWeapons):
                self.hp -= 30
                self.appliedWeapons.add(obj)
                self.freeze(1)

        
