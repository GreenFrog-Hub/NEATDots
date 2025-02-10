import pyglet as pg
import numpy as np
import brain
import math
from random import uniform

class Dots:
    def __init__(self, width, height, goal):
        self.width = width
        self.height = height
        self.pos = np.zeros(2)
        self.vel = np.zeros(2)
        self.acc = np.zeros(2)
        self.pos[0] = 400
        self.pos[1] = 150
        
        self.sprite = pg.shapes.Circle(self.pos[0], self.pos[1], 2, color=(255,255,255))
        self.brain = brain.Brain(400)

        self.readchGoal = False
        self.dead = False

        self.goal = goal

        self.fitness = 0
    

    def calcFitness(self):
        self.distanceToGoal = math.sqrt((self.goal[0]-self.pos[0])**2 + (self.goal[1]-self.pos[1])**2)
        self.fitness = 1/(self.distanceToGoal**2)
        if self.readchGoal == True:
            self.fitness += 1/self.brain.step**2

    def move(self):
        if len(self.brain.directions) >self.brain.step:
            self.acc = self.direction = np.asarray(self.brain.directions[self.brain.step])
            self.brain.step += 1
        self.vel += self.acc
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
            self.readchGoal = True
        if self.dead != True and self.readchGoal != True:
            self.move()
        
        self.sprite.draw()

    

    def breed(self):
        self.babyBrain = brain.Brain(len(self.brain.directions))
        self.babyBrain.directions = self.brain.directions.copy()
        return self.babyBrain

    def reset(self):
        self.pos[0] = 400
        self.pos[1] = 150
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]
        self.brain.step = 0
        self.readchGoal = False
        self.dead = False
    
