"""Visualization Curves in 3D space"""
"""
Cartesian/Polar

3D
C(t) = (x(t), y(t), z(t))
"""

from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
plt.show()

# Drawing a 3D equation
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

ax.view_init(60, 35)
plt.show()

# Drawing circles in 3D
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2 * np.pi, 201)
print(theta)
y = 10*np.cos(theta)
z = 10*np.sin(theta)

for i in range(18):
    phi = i*np.pi/9
    ax.plot(y*np.sin(phi)+10*np.sin(phi),
            y*np.cos(phi)+10*np.cos(phi), z)

ax.plot((0,0),(0,0), (-10,10), '-k', label='z-axis')
ax.legend()
plt.show()
