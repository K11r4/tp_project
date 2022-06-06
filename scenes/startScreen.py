import pygame, time
from pygame.locals import *

from scenes.scene import Scene
from sprite import Sprite
from controllers.clickController import ClickController

class StartScreen(Scene):
    def __init__(self, screen, controller):
        super().__init__(screen, controller)
        self.button = ClickController()
        self.controller.subscribe(KEYUP, self.button)
        self.controller.subscribe(KEYDOWN, self.button)
        self.image = pygame.image.load("./src/newTitle.jpg").convert()
        self.musicTheme = pygame.mixer.Sound("./src/loadingTheme.mp3")

    def init(self):
        self.musicTheme.play()
        self.startTime = time.time()
        super().init()
    
    def render(self):
        #self.screen.fill("#30C864")
        self.screen.drawImage(self.image)
        self.screen.fill("#010101", max(255 - (time.time() - self.startTime) / 5 * 255, 0))

        if self.button.isPressed:
            self.musicTheme.stop()
            self.active = False
            self.next = "gameLevel"
        
        super().render()

        