import pyglet as pg
import numpy as np
import brain
import math
from random import uniform

class Dots:
    def __init__(self, width, height, startPos, goal, maxSteps, walls):
        self.width = width
        self.height = height
        self.pos = np.copy(startPos)
        self.vel = np.zeros(2)
        self.acc = np.zeros(2)
        self.maxSteps = 400
        
        self.sprite = pg.shapes.Circle(self.pos[0], self.pos[1], 2, color=(255,255,255))
        self.brain = brain.Brain(self.maxSteps)

        self.reachedGoal = False
        self.dead = False

        self.goal = goal

        self.fitness = 0

        self.walls = walls
    

    def calcFitness(self):
        self.distanceToGoal = math.sqrt((self.goal[0]-self.pos[0])**2 + (self.goal[1]-self.pos[1])**2)
        self.fitness = 1/(self.distanceToGoal**2)
        if self.reachedGoal == True:
            self.fitness += (1000/self.brain.step**16)

    def move(self):
        if len(self.brain.directions) >self.brain.step:
            self.acc = self.direction = np.asarray(self.brain.directions[self.brain.step])
            self.brain.step += 1
            self.vel += self.acc
        else:
            self.vel = 0
        self.mag = np.linalg.norm(self.vel)
        if self.mag > 5:
            for i in range(0, len(self.vel)):
                self.vel[i] = self.vel[i]/(self.mag/5)
        self.pos += self.vel
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]

    def update(self):
        if (self.pos[0] < 2 or self.pos[1] < 2 or self.pos[0] > self.width-2 or self.pos[1] > self.height-2):
            self.dead = True
        elif math.sqrt((self.goal[0]-self.pos[0])**2 + (self.goal[1]-self.pos[1])**2) < 5:
            self.reachedGoal = True
        elif len(self.brain.directions) <= self.brain.step:
            self.dead = True
        for i in self.walls:
            if i.checkCollision(self.pos[0], self.pos[1]):
                self.dead = True
                break
        if self.dead != True and self.reachedGoal != True:
            self.move()
        
        self.sprite.draw()

    def breed(self):
        self.babyBrain = brain.Brain(self.maxSteps)
        for i in range(0, len(self.brain.directions)):
            self.babyBrain.directions[i] = self.brain.directions[i]
        return self.babyBrain

    def setBestDot(self):
        self.sprite.color = (255,255,0)
        self.sprite.radius = 6
