import pygame
from pygame.locals import *

class DirController:
    def __init__(self):
        self.vertDir = 0
        self.horDir = 0
    
    def update(self, event):
        if event.type == KEYDOWN and event.key == K_UP:
            self.vertDir -= 1

        if event.type == KEYDOWN and event.key == K_DOWN:
            self.vertDir += 1

        if event.type == KEYDOWN and event.key == K_LEFT:
            self.horDir -= 1
        
        if event.type == KEYDOWN and event.key == K_RIGHT:
            self.horDir += 1
        
        if event.type == KEYUP and event.key == K_UP:
            self.vertDir += 1

        if event.type == KEYUP and event.key == K_DOWN:
            self.vertDir -= 1

        if event.type == KEYUP and event.key == K_LEFT:
            self.horDir += 1
        
        if event.type == KEYUP and event.key == K_RIGHT:
            self.horDir -= 1