import pygame
from pygame.locals import *

class ClickController:
    def __init__(self):
        self._isPressed = False

    @property
    def isPressed(self):
        res = self._isPressed
        self._isPressed = False
        return res

    
    def update(self, event):
        if event.type == KEYDOWN:
            self._isPressed = True

    