import pygame
from pygame.locals import *

class DirController:
    def __init__(self):
        self.vertDir = 0
        self.horDir = 0
        self.isActive = False
        self.lastHorDir = 0
        self.lastVertDir = 0
    
    def update(self, event):
        if event.type == KEYDOWN and (event.key == K_UP or event.key == K_w):
            self.vertDir = -1
            self.lastVertDir = -1

        if event.type == KEYDOWN and (event.key == K_DOWN or event.key == K_s):
            self.vertDir = 1
            self.lastVertDir = 1

        if event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_a):
            self.horDir = -1
            self.lastHorDir = -1
        
        if event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_d):
            self.horDir = 1
            self.lastHorDir = 1
        
        if event.type == KEYUP and (event.key == K_UP or event.key == K_w):
            self.vertDir = max(self.vertDir, 0)

        if event.type == KEYUP and (event.key == K_DOWN or event.key == K_s):
            self.vertDir = min(self.vertDir, 0)

        if event.type == KEYUP and (event.key == K_LEFT or event.key == K_a):
            self.horDir = max(self.horDir, 0)
        
        if event.type == KEYUP and (event.key == K_RIGHT or event.key == K_d):
            self.horDir = min(self.horDir, 0)

        self.isActive = (self.vertDir != 0 or self.horDir != 0)
    