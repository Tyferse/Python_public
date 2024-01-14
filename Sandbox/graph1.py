from numpy import *
import matplotlib.pyplot as plt
t=linspace(0, 7, 73)
y1=t**2*2
y2=t**3*3
y3=t**4*4

plt.plot(t, y1, 'k-')
plt.plot(t, y2, 'b-.')
plt.plot(t, y3, 'yo--')

plt.xlabel('t')
plt.ylabel('y')
plt.title("This shit's cool!")
plt.legend(['t**2*2', 't**3*3', 't**4*4'], loc='upper left')
plt.savefig('graph.png')
