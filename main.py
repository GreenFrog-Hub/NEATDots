import pyglet as pg
from Dots import Dots
from population import Population
import numpy as np

window = pg.window.Window(width = 800, height = 800)


goal = np.zeros(2)
goal.put(0,400)
goal.put(1,750)


peopleOfLemanburg = Population(100, window.width, window.height, goal)

genLabel = pg.text.Label(text="Generation: 0", x=340, y= 400, color=(255,255,255,255))

goalSprite = pg.shapes.Circle(x=goal[0], y=goal[1], radius=4, color=(255,0,0))

@window.event
def draw(dt):
    window.clear()
    goalSprite.draw()
    if peopleOfLemanburg.allDead() == True:
        peopleOfLemanburg.clacFitness()
        peopleOfLemanburg.naturalSelection()
        peopleOfLemanburg.mutateDemBabies()
        genLabel.text = "Generation: "+str(round(peopleOfLemanburg.gen))
    else:
        peopleOfLemanburg.updateDots()
    genLabel.draw()

pg.clock.schedule_interval(draw, 1/120)
pg.app.run()