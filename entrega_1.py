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
formatList = ["{:.4f}".format(electron.maxx),"{:.4f}".format(electron.maxy),"{:.4f}".format(electron.time*math.pow(10,6))]
text = "max X: {}, max Y: {}, time: {}*10^-6".format(*formatList)
plt.text(electron.maxx,electron.maxy,text,fontsize = 15)
plt.show()
