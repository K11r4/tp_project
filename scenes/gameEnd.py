import pygame, time
from pygame.locals import *

from scenes.scene import Scene
from sprite import Sprite
from clickController import ClickController

class GameEnd(Scene):
    def __init__(self, screen, controller):
        super().__init__(screen, controller)
        self.button = ClickController()
        self.controller.subscribe(KEYUP, self.button)
        self.controller.subscribe(KEYDOWN, self.button)
        self.image = pygame.image.load("./src/winning.jpg").convert()

    def init(self):
        self.startTime = time.time()
        super().init()
    
    def render(self):
        self.screen.drawImage(self.image)
        self.screen.fill("#ffffff", max(10 - ((time.time() - self.startTime) / 2) * 10, 0))

        if self.button.isPressed and (time.time() - self.startTime) > 5:
            
            self.active = False
            self.next = None
        
        super().render()

    

    

        