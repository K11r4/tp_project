from scenes.scene import Scene
from collider import Collider
from characters.player import Player
from characters.enemy import Enemy
from objects.exitpoint import ExitPoint
from camera import Camera
from map import Map

class GameLevel(Scene):
    def __init__(self, screen, controller):
        super().__init__(screen, controller)
        self.map = Map("./src/map.json")

        

        
    def init(self):
        self.objects.clear()
        player = Player(80, 80, self.controller, self)
        self.player = player
        self.objects.append(player)

        #enemy1 = Enemy(400, 80, player)
        #self.objects.append(enemy1)

        self.collider = Collider()
        self.collider.addKinematicShape(player)

        for obj in self.map.obstacles:
            self.collider.addStaticShape(obj)
        
        for obj in self.map.enemies:
            newEnemy = Enemy(obj.x, obj.y, player)
            self.objects.append(newEnemy)
            self.collider.addKinematicShape(newEnemy)
            self.collider.addActiveShape(newEnemy)

        self.collider.addActiveShape(ExitPoint(3972, 2692))

        self.camera = Camera(player, (self.screen.width, self.screen.height), self.map.shape)
        self.screen.setCamera(self.camera)

        super().init()
        

    def render(self):
        self.objects = list(filter(lambda body: body.alive, self.objects))
        for obj in self.objects:
            obj.update()

        self.collider.update()

        if not self.player.alive:
            if self.player.status == "died":
                self.active = False
                self.next = "gameOver"
            elif self.player.status == "winned":
                self.active = False
                self.next = "gameEnd"

        self.screen.fill("#104040")

        self.screen.draw(self.map)

        self.camera.update()
        
        for obj in self.objects:
            self.screen.draw(obj)
        
        super().render()
