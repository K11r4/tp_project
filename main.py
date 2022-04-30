import pygame, sys
from pygame.locals import *
from scenes.startScreen import StartScreen
from scenes.gameLevel import GameLevel
from scenes.gameOver import GameOver
from scenes.gameEnd import GameEnd
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
            "gameOver": GameOver(self.screen, self.controller),
            "gameEnd": GameEnd(self.screen, self.controller)
        }

        self.currentScene = self.scenes["startScreen"]
        self.clock = pygame.time.Clock()
        self.fps = fps
        

    def run(self):
        running = True
        self.currentScene.init()
        while running:
            for event in pygame.event.get():
                self.controller.notify(event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            if not self.currentScene.active:
                
                if self.currentScene.next == None:
                    pygame.quit()
                    sys.exit()
                else:
                    self.currentScene = self.scenes[self.currentScene.next]
                    self.currentScene.init()

            self.currentScene.render()
            self.clock.tick(self.fps)


DS_BudgetEdition = Game(30)
DS_BudgetEdition.run()
    


    