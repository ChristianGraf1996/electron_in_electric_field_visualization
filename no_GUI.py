import math
from Electron import *
#calculos sin GUI para comprobar correcto funcionamiento
electron = Electron(5*math.pow(10,6),45)
print("e", end ='= ')
print(electron.e)  
print("Ey", end ='= ')
print(electron.Ey)
print ("Fy = e*Ey", end ='= ')
print(electron.Fy)
#print( electron.calculateLength(electron.v0x,electron.ay,2.88*math.pow(10,-9) )  )
print ("Max y, time*10^9", end ='= ')
maxy,timey = electron.calculateMax(electron.ay,electron.v0y)
print(maxy,timey) 
print ("Max x, time*10^9", end ='= ')
print(electron.calculateMax(electron.ax,electron.v0x))
print("Max x with time from maxy",end ='= ')
print(electron.calculateLength(electron.v0x,electron.ax,timey*math.pow(10,-9)))
