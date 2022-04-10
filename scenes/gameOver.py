import pygame, time
from pygame.locals import *

from scenes.scene import Scene
from sprite import Sprite
from clickController import ClickController

class GameOver(Scene):
    def __init__(self, screen, controller):
        super().__init__(screen, controller)
        self.button = ClickController()
        self.controller.subscribe(KEYUP, self.button)
        self.controller.subscribe(KEYDOWN, self.button)
        self.image = pygame.image.load("./src/youDied.jpg").convert()

    def init(self):
        self.startTime = time.time()
        super().init()
    
    def render(self):
        #self.screen.fill("#30C864")
        self.screen.drawImage(self.image)
        self.screen.fill("#a00101", max(255 - ((time.time() - self.startTime) / 4) ** 3 * 255, 0))

        if self.button.isPressed and (time.time() - self.startTime) > 5:
            
            self.active = False
            self.next = "gameLevel"
        
        super().render()

    

    

        