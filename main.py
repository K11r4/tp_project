import pygame, sys
from pygame.locals import *
from scenes.startScreen import StartScreen
from scenes.gameLevel import GameLevel
from scenes.gameOver import GameOver
from screen import Screen
from controller import Controller


class Game:
    def __init__(self, fps):
        pygame.init()

        self.controller = Controller()
        self.screen = Screen(1080, 720)

        self.scenes = {
            "startScreen": StartScreen(self.screen, self.controller),
            "gameLevel": GameLevel(self.screen, self.controller),
            "gameOver": GameOver(self.screen, self.controller)
        }

        self.currentScene = self.scenes["gameLevel"]
        self.clock = pygame.time.Clock()
        self.fps = fps
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.controller.notify(event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.currentScene.render()
            self.clock.tick(self.fps)


darkSoulOfElvenKnight_MVP = Game(30)
darkSoulOfElvenKnight_MVP.run()
    


    