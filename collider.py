import pygame
from pygame.locals import *

class Collider:
    def __init__(self):
        self.staticShapes = list()
        self.kinematicShapes = list()
        self.activeShapes = list()
    
    def update(self):
        self.kinematicShapes = list(filter(lambda body: body.alive, self.kinematicShapes))
        self.activeShapes = list(filter(lambda body: body.alive, self.activeShapes))

        for body in self.kinematicShapes:
            lastX, lastY = body.lastX + body.collisionShape.x, body.lastY + body.collisionShape.y
            x, y = body.shape.x + body.collisionShape.x, body.shape.y + body.collisionShape.y
            w, h = body.collisionShape.w, body.collisionShape.h
            for obst in self.staticShapes:
                if (lastX + w <= obst.left) and (x + w > obst.left) and (y + h > obst.y) and (y < obst.y + obst.h):
                    body.shape.x = obst.left - w - body.collisionShape.x

                if (lastX >= obst.right) and (x < obst.right) and (y + h > obst.y) and (y < obst.y + obst.h):
                    body.shape.x = obst.right - body.collisionShape.x

                if (lastY + h <= obst.top) and (y + h > obst.top) and (x + w > obst.x) and (x < obst.x + obst.w):
                    body.shape.y = obst.top - h - body.collisionShape.y

                if (lastY >= obst.bottom) and (y < obst.bottom) and (x + w > obst.x) and (x < obst.x + obst.w):
                    body.shape.y = obst.bottom - body.collisionShape.y
                    
        for body in self.kinematicShapes:
            for obj in self.activeShapes:
                if self.collide(body, obj):
                    body.onCollision(obj)

    def collide(self, obj1, obj2):
        collideShape1 = pygame.Rect((obj1.collisionShape.x + obj1.shape.x, obj1.collisionShape.y + obj1.shape.y),
                                    (obj1.collisionShape.w, obj1.collisionShape.h))
        collideShape2 = pygame.Rect((obj2.collisionShape.x + obj2.shape.x, obj2.collisionShape.y + obj2.shape.y),
                                    (obj2.collisionShape.w, obj2.collisionShape.h))
        res = pygame.Rect.colliderect(collideShape1, collideShape2)
        
        return res
    
    def addStaticShape(self, obst):
        self.staticShapes.append(obst)

    def addKinematicShape(self, body):
        self.kinematicShapes.append(body)

    def addActiveShape(self, body):
        self.activeShapes.append(body)