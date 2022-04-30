import pygame
from pygame.locals import *
from sprite import Sprite
from animation import Animation

class SpriteSheet:
    def __init__(self, src, spriteWidth, spriteHeight):
        self.image = pygame.image.load(src).convert_alpha()
        self.spriteWidth, self.spriteHeight = spriteWidth, spriteHeight
        self.width, self.height = self.image.get_size()
        self.columnsCount = self.width // self.spriteWidth
        self.rowsCount = self.height // self.spriteHeight

        self.sprites = dict()
        index = 0
        for row in range(self.rowsCount):
            for col in range(self.columnsCount):
                spriteView = pygame.Surface((self.spriteWidth, self.spriteHeight))
                spriteView.blit(self.image, (-col * self.spriteWidth, -row * self.spriteHeight))
                spriteView.set_colorkey((0, 0, 0))
                self.sprites[index] = spriteView
                index += 1

    def getSprite(self, n):
        return Sprite(self.sprites[n])

    def getAnimation(self, start, framesCount, delay=0.1, autoplay=True, cicle=True):
        frames = [self.sprites[start + idx] for idx in range(framesCount)]
        return Animation(frames, delay, autoplay, cicle)
