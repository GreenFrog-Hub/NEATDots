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
            self.randAng= uniform(0,2*math.pi)
            self.direction = []
            self.direction.append(math.cos(self.randAng))
            self.direction.append(math.sin(self.randAng))
            self.directions.append(self.direction.copy())
    

    def clone(self):
        self.clone = Brain(len(self.directions))
        self.clone.directions = self.directions
        return self.clone

    def mutate(self):
        self.mutationRate = 0.01
        for i in range(0,len(self.directions)):
            self.rand = uniform(0,1)
            if self.rand < self.mutationRate:
                self.randAng= uniform(0,2*math.pi)
                self.direction = []
                self.direction.append(math.cos(self.randAng))
                self.direction.append(math.sin(self.randAng))   
                self.directions[i] = self.direction.copy()