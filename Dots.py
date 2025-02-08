import pyglet as pg
import numpy as np
import brain
import math

class Dots:
    def __init__(self, width, height, goal):
        self.width = width
        self.height = height
        self.pos = np.zeros(2)
        self.vel = np.zeros(2)
        self.acc = np.zeros(2)
        self.pos[0] = width//2
        self.pos[1] = 75
        self.sprite = pg.shapes.Circle(self.pos[0], self.pos[1], 2, color=(255,255,255))
        self.brain = brain.Brain(400)

        self.readchGoal = False
        self.dead = False

        self.goal = goal

        self.fitness = 0
    

    def calcFitness(self):
        distanceToGoal = math.sqrt((self.goal[0]-self.sprite.x)**2 + (self.goal[1]-self.sprite.y)**2)
        self.fitness = 1/(distanceToGoal**2)

    def move(self):
        if len(self.brain.directions) >self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        self.vel += self.acc
        mag = np.linalg.norm(self.vel)
        if mag > 5:
            for i in range(0, len(self.vel)):
                self.vel[i] = self.vel[i]/(mag/5)
        self.pos += self.vel

    def update(self):
        if (self.sprite.x < 2 or self.sprite.y < 2 or self.sprite.x > self.width-2 or self.sprite.y > self.height-2):
            self.dead = True
        elif math.sqrt((self.goal[0]-self.sprite.x)**2 + (self.goal[1]-self.sprite.y)**2) < 5:
            self.readchGoal = True
        if self.dead != True and self.readchGoal != True:
            self.move()
        self.sprite.position = self.pos
        self.sprite.draw()
    

    def breed(self):
        baby = Dots(self.width, self.height, self.goal)
        baby.brain = self.brain.clone()
        return baby