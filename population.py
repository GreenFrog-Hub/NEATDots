from Dots import Dots
from random import random, uniform

class Population:
    def  __init__(self, size, width, height, goal):
        self.size = size
        self.width = width
        self.height = height
        self.goal = goal
        self.dotArray = []
        self.gen = 0
        for i in range(0, self.size):
            self.dotArray.append(Dots(width, height, goal))
        
    def updateDots(self):
        for i in range(0, len(self.dotArray)):
            self.dotArray[i].update()
    

    def allDead(self):
        for i in range(0, len(self.dotArray)):
            if self.dotArray[i].dead == False and self.dotArray[i].readchGoal == False:
                return False
        return True


    def clacFitness(self):
        for i in range(0, len(self.dotArray)):
            self.dotArray[i].calcFitness()
    

    def naturalSelection(self):
        self.calcFitnessSum()
        self.newBrainArray = []
        for i in range(0, len(self.dotArray)):
            
            #select parent
            self.parent = self.selectParent()

            #make baby
            self.newBrainArray.append(self.parent.breed())

        self.dotArray = []
        for i in range(0, self.size):
            self.dotArray.append(Dots(self.width, self.height, self.goal))
            self.dotArray[i].brain = self.newBrainArray[i]
            
        self.gen += 1

    

    def calcFitnessSum(self):
        self.totalFitness = 0
        for i in range(0, len(self.dotArray)):
            self.totalFitness += self.dotArray[i].fitness * 100
    

    def selectParent(self):
        randomChoice = uniform(0, self.totalFitness)

        runningSum = 0
        for i in range(0, len(self.dotArray)):
            runningSum += self.dotArray[i].fitness*100
            if runningSum > randomChoice:
                return self.dotArray[i]
    

    def mutateDemBabies(self):
        for i in range(0, len(self.dotArray)):
            self.dotArray[i].brain.mutate()
    
    