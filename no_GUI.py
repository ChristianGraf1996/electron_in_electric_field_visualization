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
print ("Max x, Max y, time", end ='= ')
maxx,maxy,time = electron.calculateMax()
print(maxx,maxy,time)
#print("Max x with time from maxy",end ='= ')
#print(electron.calculateLength(electron.v0x,electron.ax,timey))
#print("0.041 / v0x",end = "= ")
#time_teacher = 0.041/electron.v0x
#print(time_teacher)
#length_teacher = electron.calculateLength(electron.v0x,electron.ax,time_teacher)
#print(length_teacher)

