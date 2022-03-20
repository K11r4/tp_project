class Body:
    def __init__(self, shape, velocity, surface, collisionShape):
        self.shape = shape
        self.lastX, self.lastY = shape.x, shape.y
        self.velocity = velocity
        self.view = surface
        self.collisionShape = collisionShape
        
    def update(self):
        self.lastX, self.lastY = self.shape.x, self.shape.y
    

