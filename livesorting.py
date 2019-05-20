import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from matplotlib import style

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
x=[]
for aux in range(100):
    x.append(aux)
n = len(x)

def unsort():
    y=[]
    for aux in range(100):
        y.append(random.randint(1,101))
    return y


def bublesort():
    for i in range(n):
        for j in range(0, n-i-1):
            if(y[j]>y[j+1]):
                y[j], y[j+1] = y[j+1], y[j]

y=unsort()
bublesort()
