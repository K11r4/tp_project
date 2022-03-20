import pygame
from pygame.locals import *

class Screen:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.camera = None
        self.mainSurface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("DarkSoulOfElvenKnight_MVP")

    def setCamera(self, camera):
        self.camera = camera

    def fill(self, color):
        self.mainSurface.fill(Color(color))

    def draw(self, gameObject):
        x, y = gameObject.shape.x, gameObject.shape.y
        if self.camera:
            x -= self.camera.shape.x
            y -= self.camera.shape.y
        self.mainSurface.blit(gameObject.view, (x, y))


    def update(self):
        pygame.screen.update()

    
    