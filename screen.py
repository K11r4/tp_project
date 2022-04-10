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

    def fill(self, color, appacity=255):
        mask = pygame.Surface((self.width, self.height))
        mask.fill(Color(color))
        mask.set_alpha(appacity)
        self.mainSurface.blit(mask, (0, 0))

    def draw(self, gameObject):
        if not gameObject.view:
            return
        x, y = gameObject.shape.x, gameObject.shape.y
        if self.camera:
            x -= self.camera.shape.x
            y -= self.camera.shape.y
        self.mainSurface.blit(gameObject.view.img, (x, y))
    

    def drawImage(self, image):
        self.mainSurface.blit(image, (0, 0))

    def update(self):
        pygame.screen.update()

    
    