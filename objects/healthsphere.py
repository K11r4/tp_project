import pygame
from pygame.locals import *
from body import Body
from sprite import Sprite

class HealthSphere(Body):
    def __init__(self, x, y):
        width, height = 30, 30
        view = pygame.Surface((width, height))
        pygame.draw.circle(view, (0, 80, 0), (15, 15), 15)
        pygame.draw.circle(view, (0, 140, 0), (15, 15), 13)
        pygame.draw.circle(view, (0, 200, 0), (15, 15), 10)
        super().__init__(
            pygame.Rect((x, y), (width, height)),
            None,
            Sprite(view),
            pygame.Rect((0, 0), (width, height))
        )