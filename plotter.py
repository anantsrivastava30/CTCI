import matplotlib.pyplot as plt
import numpy as np

file = np.loadtxt("queens-attack-test.txt")

X = file[:, 0]
Y = file[:, 1]

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(1, 100, 1))
ax.set_yticks(np.arange(1, 100, 1))
plt.plot([1,100],[54,54])
plt.plot([30,30],[1,100])
plt.plot([30,76],[54,100])
plt.plot([30,10],[54,34])
plt.plot([30,10],[54,74])
plt.plot([30,10],[54,74]) 

plt.scatter(Y, X)
plt.grid()
plt.legend()
plt.show()
