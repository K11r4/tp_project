import pygame, time
from pygame.locals import *
from sprite import Sprite

class Animation(Sprite):
    def __init__(self, frames, delay=0.1, autoplay=True, cicle=True):
        self.frames = frames
        self.delay = delay
        self.running = autoplay
        self.cicle = cicle
        self.lastTime = time.time()
        self.currentFrame = 0
        super().__init__(frames[0])
        

    def run(self):
        if not self.running:
            self.currentFrame = 0
            self.lastTime = time.time()
            self.running = True
    
    def stop(self):
        self.running = False

    def nextFrame(self):
        now = time.time()
        if(now - self.lastTime > self.delay):
            if(self.currentFrame + 1 >= len(self.frames)):
                if self.cicle:
                    self.currentFrame = 0
                else:
                    self.running = False
            else:
                self.currentFrame += 1
            self.lastTime = now

    def update(self):
        if self.running:
            self.nextFrame()
            self.img = self.frames[self.currentFrame]

            