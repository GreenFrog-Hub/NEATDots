import numpy as np
from random import random
import math

class Brain:
    def __init__(self, size):
        self.size = size
        self.directions = []
        
        self.step = 0
        self.randomize()
    
    def randomize(self):
        for i in range(0, self.size-1):
            randAng= random()*2*math.pi
            self.direction = np.zeros(2)
            self.direction.put(0,math.cos(randAng))
            self.direction.put(1, math.sin(randAng))
            self.directions.append(self.direction)
        self.directions = np.asarray(self.directions)
    

    def clone(self):
        clone = Brain(len(self.directions))
        clone.directions = self.directions
        return clone

    def mutate(self):
        mutationRate = 0.25
        for i in range(0,len(self.directions)-1):
            rand = random()
            if rand < mutationRate:
                randAng= random()*2*math.pi
                self.direction = np.zeros(2)
                self.direction.put(0,math.cos(randAng))
                self.direction.put(1, math.sin(randAng))
                self.directions.put(i, self.direction)