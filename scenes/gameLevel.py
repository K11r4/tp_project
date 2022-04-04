from scenes.scene import Scene
from collider import Collider
from characters.player import Player
from camera import Camera
from map import Map

class GameLevel(Scene):
    def __init__(self, screen, controller):
        super().__init__(screen, controller)
        self.map = Map("./src/level.txt")

        player = Player(64, 64, controller)
        self.objects.append(player)

        self.collider = Collider()
        self.collider.addKinematicShape(player)
        for obst in self.map.obstacles:
            self.collider.addStaticShape(obst)

        self.camera = Camera(player, (screen.width, screen.height), self.map.shape)
        self.screen.setCamera(self.camera)
        

    def render(self):
        for obj in self.objects:
            obj.update()

        self.collider.update()

        self.screen.draw(self.map)

        self.camera.update()
        
        for obj in self.objects:
            self.screen.draw(obj)
        
        super().render()
