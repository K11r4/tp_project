import pygame
from pygame.locals import *

class Sprite():
    def __init__(self, img):
        self.img = img
        self.img.set_colorkey((0, 0, 0))
