import pygame
import json
from pygame.locals import *
from sprite import Sprite
from spritesheet import SpriteSheet

class Map:
    def __init__(self, src):
        with open(src, 'r') as dirtyData:
            parseData = json.load(dirtyData)

        self.imageSource = SpriteSheet("./src/stone.png", parseData["tilewidth"], parseData["tileheight"])
        self.obstacles = list()
        self.enemies = list()
        self.healthpoints = list()
        self.shape = pygame.Rect((0, 0), (parseData["width"] * parseData["tilewidth"], parseData["height"] * parseData["tileheight"]))
        self.useCamera = True

        mapRender = pygame.Surface((parseData["width"] * parseData["tilewidth"], parseData["height"] * parseData["tileheight"]))
        mapRender.set_colorkey((0, 0, 0))

        norm = lambda x: int(round(x / parseData["tilewidth"])) * parseData["tilewidth"]

        for layer in parseData["layers"]:
            if layer["type"] == "tilelayer":
                idx = 0
                for spriteId in layer["data"]:
                    currentSprite = self.imageSource.getSprite(spriteId - 1)
                    y = (idx // parseData["width"]) * parseData["tilewidth"]
                    x = (idx % parseData["width"]) * parseData["tilewidth"]
                    mapRender.blit(currentSprite.img, (x, y))
                    idx += 1
            elif layer["name"] == "walls":
                for obj in layer["objects"]:
                    self.obstacles.append(pygame.Rect((norm(obj["x"]), norm(obj["y"])), (norm(obj["width"]), norm(obj["height"]))))
            elif layer["name"] == "enemies":
                for obj in layer["objects"]:
                    self.enemies.append(pygame.Rect((norm(obj["x"]), norm(obj["y"])), (norm(obj["width"]), norm(obj["height"]))))
            elif layer["name"] == "healthpoints":
                for obj in layer["objects"]:
                    self.healthpoints.append(pygame.Rect((norm(obj["x"]), norm(obj["y"])), (norm(obj["width"]), norm(obj["height"]))))

        
        self.view = Sprite(mapRender)
        
        
                

        
    

