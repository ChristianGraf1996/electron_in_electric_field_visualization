from Electron import Electron
import numpy as np
def setup():
    global e
    e = Electron()
    size(1280, 1000)
    
def draw():
    global e
    background(255)
    fill(0)
    line(50,0,50, height)
    line(0, 3*height/4, width, 3*height/4)
    e.drawElectron() 

class Electron:
    def __init__(self):
        ellipseMode(CENTER)
        fill(100)
        self.angle = 12
        self.velocity = 10
        self.position_x = 50
        self.position_y = 3*height/4
    def drawElectron(self):
        ellipse(self.position_x,self.position_y,10,10)
    


