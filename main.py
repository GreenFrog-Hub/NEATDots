import pyglet as pg
from Dots import Dots
from population import Population
import numpy as np
from obsticals import Wall


window = pg.window.Window(width = 1200, height = 1200)

global press
press = 0
goal = np.zeros(2)
startPos = np.zeros(2)
# goal.put(0,800)
# goal.put(1,1000)
global start
start = False
textLabel = pg.text.Label(text="Press to choose start location", x=window.width//2, y= window.height//2, color=(255,255,255,255), anchor_x="center")
startSprite = pg.shapes.Circle(x=1600, y=1600, radius=4, color=(0,255,0))
goalSprite = pg.shapes.Circle(x=1600, y=1600, radius=4, color=(255,0,0))
walls = []
@window.event
def on_mouse_press(x, y, button, modifiers):
    global press
    global start
    global peopleOfLemanburg
    global genLabel
    global minStepsLabel
    global maxStepsLabel
    press += 1
    if press == 1:
        global startSprite
        startPos.put(0, x)
        startPos.put(1, y)
        startSprite.x = x
        startSprite.y = y
        textLabel.text = "Click to choose end location"
    elif press == 2:
        global goalSprite
        goal.put(0, x)
        goal.put(1, y)
        goalSprite.x = x
        goalSprite.y = y
        textLabel.text = "Click to draw "+str(3)+" more walls"
    elif press == 3:
        textLabel.text = "Click to draw "+str(2)+" more walls"
        walls.append(Wall(x,y))
    elif press == 4:
        textLabel.text = "Click to draw "+str(1)+" more walls"
        walls.append(Wall(x,y))
    elif press == 5:
        walls.append(Wall(x,y))
        textLabel.delete() 
        start = True
    if start == True:
        peopleOfLemanburg = Population(400, window.width, window.height,startPos, goal, 400,100, walls)
        genLabel = pg.text.Label(text="Generation: 0", x=0, y= window.height-20, color=(255,255,255,255), anchor_x="left",)
        minStepsLabel = pg.text.Label(text="Min Steps: "+str(peopleOfLemanburg.minStep), x=0, y=window.height- 40, color=(255,255,255,255), anchor_x="left")
        maxStepsLabel = pg.text.Label(text="Max Steps: "+str(peopleOfLemanburg.maxSteps), x=0, y=window.height- 60, color=(255,255,255,255), anchor_x="left")
        


@window.event
def draw(dt):
    window.clear()
    startSprite.draw()
    goalSprite.draw()
    for i in walls:
        i.update()
    if start == True:
        if peopleOfLemanburg.allDead() == True:
            peopleOfLemanburg.clacFitness()
            peopleOfLemanburg.naturalSelection()
            peopleOfLemanburg.mutateDemBabies()
            genLabel.text = "Generation: "+str(round(peopleOfLemanburg.gen))
            minStepsLabel.text = "Min Steps: "+str(round(peopleOfLemanburg.minStep))
            maxStepsLabel.text = "Max Steps: "+str(round(peopleOfLemanburg.maxSteps))
        else:
            peopleOfLemanburg.updateDots()
        genLabel.draw()
        minStepsLabel.draw()
        maxStepsLabel.draw()
    else:
        textLabel.draw()

pg.clock.schedule_interval(draw, 1/120)
pg.app.run()