class Collider:
    def __init__(self):
        self.staticShapes = list()
        self.kinematicShapes = list()
        self.damageShapes = list()
    
    def update(self):
        for body in self.kinematicShapes:
            lastX, lastY = body.lastX + body.collisionShape.x, body.lastY + body.collisionShape.y
            x, y = body.shape.x + body.collisionShape.x, body.shape.y + body.collisionShape.y
            w, h = body.collisionShape.w, body.collisionShape.h
            for obst in self.staticShapes:
                if (lastX + w <= obst.left) and (x + w > obst.left) and (y + h > obst.y) and (y < obst.y + obst.h):
                    body.shape.x = obst.left - w - body.collisionShape.x

                if (lastX >= obst.right) and (x < obst.right) and (y + h > obst.y) and (y < obst.y + obst.h):
                    body.shape.x = obst.right - body.collisionShape.x

                if (lastY + h <= obst.top) and (y + h > obst.top) and (x + w > obst.x) and (x < obst.x + obst.w):
                    body.shape.y = obst.top - h - body.collisionShape.y

                if (lastY >= obst.bottom) and (y < obst.bottom) and (x + w > obst.x) and (x < obst.x + obst.w):
                    body.shape.y = obst.bottom - body.collisionShape.y

                 
    
    def addStaticShape(self, obst):
        self.staticShapes.append(obst)

    def addKinematicShape(self, body):
        self.kinematicShapes.append(body)

    def addDamageShape(self):
        pass