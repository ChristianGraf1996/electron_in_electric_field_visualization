import math
import matplotlib.pyplot as plt
from Electron import *

Vo = 3*math.pow(10,6)
degrees = 80
electron = Electron(Vo,degrees)
print("Using Vo = {:.2} and angle = ".format(Vo),degrees)
print("Max y was found in: ({:.2f},{:.2f})(cm)".format(electron.maxyx*math.pow(10,2),electron.maxy*math.pow(10,2)), " with time t = ",electron.time)

plt.plot(electron.x_array, electron.y_array, 'ro')
plt.axis([0,0.03,0,0.015])
plt.plot(electron.maxyx,electron.maxy,'bo')
formatList = ["{:.4f}".format(electron.maxyx),"{:.4f}".format(electron.maxy),"{:.4f}".format(electron.time*math.pow(10,6))]
text = "X: {}, max Y: {}, time: {}*10^-6".format(*formatList)
plt.text(electron.maxyx,electron.maxy,text,fontsize = 15)
plt.show()
