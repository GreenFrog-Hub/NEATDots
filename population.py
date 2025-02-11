from Dots import Dots
from random import random, uniform
import numpy as np

class Population:
    def  __init__(self, size, width, height, startPos,goal, max,change, walls):
        self.size = size
        self.width = width
        self.height = height
        self.goal = goal
        self.startPos = np.copy(startPos)
        self.dotArray = []
        self.gen = 0
        self.maxSteps = max
        self.change = change
        self.minStep=10000
        self.walls = walls
        self.timesNoDotMadeIt = 0
        for i in range(0, self.size):
            self.dotArray.append(Dots(width, height, self.startPos, goal, self.maxSteps, self.walls))
        
    def updateDots(self):
        for i in range(0, len(self.dotArray)):
            if self.dotArray[i].brain.step > self.minStep:
                self.dotArray[i].dead = True
            else:
                self.dotArray[i].update()
    

    def allDead(self):
        for i in range(0, len(self.dotArray)):
            if self.dotArray[i].dead == False and self.dotArray[i].reachedGoal == False:
                return False
        return True


    def clacFitness(self):
        for i in range(0, len(self.dotArray)):
            self.dotArray[i].calcFitness()
            if self.gen > 50 and self.dotArray[i].hitWall:
                self.dotArray[i].fitness = self.dotArray[i].fitness/5
    

    def naturalSelection(self):
        self.calcFitnessSum()
        self.newBrainArray = []

        self.gen += 1

        # if self.gen %20 == 0:
        #     self.maxSteps += self.change
        
        for i in range(0, len(self.dotArray)-1):
            
            #select parent
            self.parent = self.selectParent()

            #make baby
            self.newBrainArray.append(self.parent.breed())

        self.getBestDot()
        self.newBrainArray.append(self.bestDot.breed())
        
        if self.numberOfDotsMakingit() > 0:
            self.timesNoDotMadeIt = 0
        else:
            if self.gen > 50:
                if self.numberOfDotsMakingit() == 0:
                    self.timesNoDotMadeIt += 1
                if self.timesNoDotMadeIt > 5:
                    self.maxSteps += 5
        self.dotArray = []
        for i in range(0, self.size):
            self.dotArray.append(Dots(self.width, self.height, self.startPos, self.goal, self.maxSteps, self.walls))
            self.dotArray[i].brain = self.newBrainArray[i]
        self.dotArray[self.size-1].setBestDot()
            
        

    

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
        for i in range(0, len(self.dotArray)-1):
            self.dotArray[i].brain.mutate(self.change)
    

    def getBestDot(self):
        max = 0
        maxIndex = 0
        for i in range(0, len(self.dotArray)):
            currentDot = self.dotArray[i]
            if self.dotArray[i].fitness > max:
                max = self.dotArray[i].fitness
                maxIndex = i
        
        self.bestDot = self.dotArray[maxIndex]

        if self.bestDot.reachedGoal == True:
            self.minStep = self.bestDot.brain.step
        
    
    def numberOfDotsMakingit(self):
        numberMadeIt = 0
        for i in range(0, len(self.dotArray)):
            if self.dotArray[i].reachedGoal:
                numberMadeIt += 1
        return numberMadeIt
                
    
    