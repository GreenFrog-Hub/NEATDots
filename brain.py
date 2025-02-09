import numpy as np
from random import random, uniform
import math

class Brain:
    def __init__(self, size):
        self.size = size
        self.directions = []
        
        self.step = 0
        self.randomize()
    
    def randomize(self):
        for i in range(0, self.size):
            randAng= uniform(0,2*math.pi)
            self.direction = np.zeros(2)
            self.direction.put(0,math.cos(randAng))
            self.direction.put(1, math.sin(randAng))
            self.directions.append(self.direction)
    

    def clone(self):
        clone = Brain(len(self.directions))
        clone.directions = self.directions
        return clone

    def mutate(self):
        mutationRate = 0.01
        for i in range(1,len(self.directions)):
            rand = uniform(0,1.1)
            if rand < mutationRate:
                randAng= uniform(0,2*math.pi)
                self.direction = np.zeros(2)
                self.direction.put(0,math.cos(randAng))
                self.direction.put(1, math.sin(randAng))
                self.directions[i] = self.direction