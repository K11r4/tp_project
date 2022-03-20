import pygame
from pygame.locals import *

class Scene:
    def __init__(self, screen, controller):
        self.screen = screen
        self.controller = controller
        self.status = True
        self.objects = list()
    
    def render(self):
        pygame.display.update()

