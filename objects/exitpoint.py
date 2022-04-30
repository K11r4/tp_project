import pygame
from pygame.locals import *
from body import Body

class ExitPoint(Body):
    def __init__(self, x, y):
        width, height = 256, 256
        super().__init__(
            pygame.Rect((x, y), (width, height)),
            None,
            None,
            pygame.Rect((108, 40), (width, height))
        )