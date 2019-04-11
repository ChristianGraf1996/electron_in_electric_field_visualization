import math
import numpy as np
class Electron:
    def __init__(self,v0,alpha):
        self.x_array = []
        self.y_array = []
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
        (self.maxx,self.maxy,self.maxyx,self.time) = self.calculateMax() 
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
        highest_y_xcoord = 0
        curr_y = 0.000
        time = -1
        found = False
        for t in np.arange (0,1000,0.01):
            if (curr_x >= 0.1): 
                self.Ey=0
                self.Ex=0
            curr_x = self.calculateLength(self.v0x,self.ax,t*math.pow(10,-9))
            self.x_array.append(curr_x)
            curr_y = self.calculateLength(self.v0y,self.ay,t*math.pow(10,-9))
            self.y_array.append(curr_y)
            if curr_x > highest_x:  
                highest_x = curr_x
            else: 
                print("found max x")
                found = True
                time = t*math.pow(10,-9)
                break
            if curr_y > highest_y:
                highest_y = curr_y
            elif found == False:
                found = True
                time = t*math.pow(10,-9)
                highest_y_xcoord=curr_x
                print('found max y')
        return (highest_x,highest_y,highest_y_xcoord,time)

