import pyglet as pg


class Wall:
    def __init__(self, x,y):
        self.width = 800
        self.height = 20
        self.sprite = pg.shapes.BorderedRectangle(x-self.width//2, y-self.height//2, self.width, self.height, 5, (204, 0, 255), (138, 6, 6))
        self.left = x-self.width//2
        self.right = x+self.width//2
        self.bottom = y-self.height//2
        self.top = y+self.height//2

    def checkCollision(self, dotX, dotY):
        if dotX > self.left and dotX < self.right and dotY > self.bottom and dotY < self.top:
            return True
        else:
            return False

    def update(self):
        self.sprite.draw()