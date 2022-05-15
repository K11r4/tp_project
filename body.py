class Body:
    def __init__(self, shape, velocity, view, collisionShape, healthPoints=1):
        self.shape = shape
        self.lastX, self.lastY = shape.x, shape.y
        self.velocity = velocity
        self.view = view
        self.collisionShape = collisionShape
        self.alive = True
        self.hp = healthPoints
        self.useCamera = True
        
        
    def update(self):
        self.lastX, self.lastY = self.shape.x, self.shape.y
        if self.hp <= 0:
            self.alive = False
            self.status = "died"
        
    def onCollision(self, obj):
        pass

    def kill(self):
        self.alive = False

