import pygame
from pygame.locals import *

class KeyContoller:
    def __init__(self, *keys):
        self.keys = dict()
        for key in keys:
            self.keys[key] = False

    def update(self, event):
        if event.key in self.keys:
            self.keys[event.key] = True if event.type == KEYDOWN else False
