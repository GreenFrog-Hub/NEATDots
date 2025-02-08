from Dots import Dots
from random import random


class Population:
    def  __init__(self, size, width, height, goal):
        self.size = size
        self.width = width
        self.height = height
        self.goal = goal
        self.dotArray = []
        self.gen = 0
        for i in range(0, self.size-1):
            self.dotArray.append(Dots(width, height, goal))
        
    def updateDots(self):
        for i in range(0, self.size-1):
            self.dotArray[i].update()
    

    def allDead(self):
        for i in range(0, self.size-1):
            if self.dotArray[i].dead == False and self.dotArray[i].readchGoal == False:
                return False
        return True


    def clacFitness(self):
        for i in range(0, self.size-1):
            self.dotArray[i].calcFitness()
    

    def naturalSelection(self):
        self.newDotArray = []
        self.calcFitnessSum()
        for i in range(0, self.size-1):
            
            #select parent
            parent = self.selectParent()

            #make baby
            self.newDotArray.append(parent.breed())
        
        self.dotArray = self.newDotArray
        self.newDotArray = []
        self.gen += 1

    

    def calcFitnessSum(self):
        self.totalFitness = 0
        for i in range(0, self.size-1):
            self.totalFitness += self.dotArray[i].fitness
    

    def selectParent(self):
        randomChoice = random()*self.totalFitness

        runningSum = 0
        for i in range(0, self.size-1):
            runningSum += self.dotArray[i].fitness
            if runningSum > randomChoice:
                return self.dotArray[i]
    

    def mutateDemBabies(self):
        for i in range(0, len(self.dotArray)-1):
            self.dotArray[i].brain.mutate()
    
    