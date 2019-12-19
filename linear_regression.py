import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,2,3,4,5,5])
y =np.array([7,8,7,9,11,10,12])

sloop = 1.25

h = 5 + (sloop * x) # The equation
fig1 = plt.figure()

plt.scatter(x,y,color='g')
plt.plot(x,h)
#plt.grid()
plt.show(fig1)