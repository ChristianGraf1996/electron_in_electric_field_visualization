import math
import numpy as np
class Electron:
    def __init__(self,v0,alpha):
        #ellipseMode(CENTER)
        #fill(100)
        self.angle = alpha
        self.v = v0
        self.v0 = v0
        self.e = -1.6*math.pow(10,-19)
        self.m = 9.11*math.pow(10,-31)
        self.Ex, self.Ey = (0, 3.5*1000)
        self.x,self.y = (0,0)
        self.v0x, self.v0y = self.calculatev0_x_y(v0,alpha)
        self.Fx, self.Fy = (self.e*self.Ex, self.e*self.Ey)
        self.ax, self.ay = (self.Fx/self.m, self.Fy/self.m)
    #def drawElectron(self):
        #ellipse(self.position_x,self.position_y,10,10)
    def calculatev0_x_y(self,v0,alpha):
        return ( v0*math.cos(math.radians(alpha)),
                 v0*math.sin(math.radians(alpha)))
    def calculateVelocity(self,a,t,v0):
        return ( (a*t) + v0)
    def calculateTime(self,v,v0,a):
        return ((v-v0)/a)
    def calculateLength(self,v0,a,t):
        return ((0.5*a*math.pow(t,2))+(v0*t))
    def calculateMax(self):
        highest_x = -999999.000
        curr_x = 0.000
        highest_y = -999999.000
        curr_y = 0.000
        for t in np.arange (0,100,0.01):
            curr_x = self.calculateLength(self.v0x,self.ax,t*math.pow(10,-9))
            curr_y = self.calculateLength(self.v0y,self.ay,t*math.pow(10,-9))
            if curr_x > highest_x:
                highest_x = curr_x
            else:
                print('found max x')
                return (highest_x,highest_y,t*math.pow(10,-9))            
            if curr_y > highest_y:
                highest_y = curr_y
            else:
                print('found max y')
                return (highest_x,highest_y,t*math.pow(10,-9))
