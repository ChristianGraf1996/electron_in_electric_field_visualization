import math
import matplotlib.pyplot as plt
from Electron import *
electron = Electron(5*math.pow(10,6),45)
print("e", end ='= ')
print(electron.e)  
print("Ey", end ='= ')
print(electron.Ey)
print ("Fy = e*Ey", end ='= ')
print(electron.Fy)
print ("Max x, Max y, time", end ='= ')
print(electron.maxx,electron.maxy,electron.time)
plt.plot(electron.x_array, electron.y_array, 'ro')
plt.axis([0,0.03,0,0.015])
plt.plot(electron.maxx,electron.maxy,'bo')
plt.show()
