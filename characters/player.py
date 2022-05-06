from body import Body
from vector import Vector
from controllers.directionController import DirController
from controllers.keyController import KeyContoller
from spritesheet import SpriteSheet
from objects.exitpoint import ExitPoint
from objects.weapon import Weapon
from objects.healthsphere import HealthSphere
import pygame
from pygame.locals import *
import time

class Player(Body):
    def __init__(self, x, y, controller, scene):
        width, height = 8 * 4, 29 * 4
        self.imageSource = SpriteSheet("./src/knight.png", 248, 160)
        self.animations = {
            "idleR": self.imageSource.getAnimation(0, 6),
            "idleL": self.imageSource.getAnimation(18, 6),
            "walkR": self.imageSource.getAnimation(6, 6),
            "walkL": self.imageSource.getAnimation(24, 6),
            "strikeR": self.imageSource.getAnimation(12, 6, autoplay=False, cicle=False),
            "strikeL": self.imageSource.getAnimation(30, 6, autoplay=False, cicle=False),
        }

        self.scene = scene

        self.commands = KeyContoller(K_SPACE)
        self.direction = DirController()
        controller.subscribe(KEYUP, self.direction)
        controller.subscribe(KEYDOWN, self.direction)
        controller.subscribe(KEYUP, self.commands)
        controller.subscribe(KEYDOWN, self.commands)

        self.isFighting = False
        self.fightingDir = "R"
        self.appliedWeapons = set()

        super().__init__(pygame.Rect((x, y), (width, height)),
                        Vector(self, 10),
                        self.imageSource.getAnimation(0, 6),
                        pygame.Rect((108, 40), (width, height)),
                        90
        )

    def update(self):
        super().update()
        self.velocity.setDirection(self.direction.horDir, self.direction.vertDir)

        if self.commands.keys[K_SPACE] and not self.isFighting:
            self.isFighting = True
            self.fightingDir = ("R" if self.direction.lastHorDir >= 0 else "L")
            self.view = self.animations["strike" + self.fightingDir]
            self.view.run()
            hit = Weapon(self.shape.x, self.shape.y, self)
            self.scene.objects.append(hit)
            self.scene.collider.addActiveShape(hit)

        if self.isFighting:
            self.isFighting = self.view.running
            self.velocity.setDirection(0, 0)
        elif self.direction.isActive:
            self.view = self.animations["walk" + ("R" if self.direction.lastHorDir >= 0 else "L")]
        else:
            self.view = self.animations["idle" + ("R" if self.direction.lastHorDir >= 0 else "L")]


        self.velocity.move()
        self.view.update()
    
    def onCollision(self, obj):
        if isinstance(obj, Weapon):
            if (obj.body != self) and (obj not in self.appliedWeapons):
                self.hp -= 60
                self.appliedWeapons.add(obj)
                print(self.hp, time.time())
        elif isinstance(obj, ExitPoint):
            self.alive = False
            self.status = "winned"
        elif isinstance(obj, HealthSphere):
            print("Yeeees")
            obj.kill()
            self.hp = min(self.hp + 30, 90)
        
    
