class Body:
    def __init__(self, shape, velocity, view, collisionShape):
        self.shape = shape
        self.lastX, self.lastY = shape.x, shape.y
        self.velocity = velocity
        self.view = view
        self.collisionShape = collisionShape
        self.alive = True
        
    def update(self):
        self.lastX, self.lastY = self.shape.x, self.shape.y
        
    def onCollision(self, obj):
        pass

