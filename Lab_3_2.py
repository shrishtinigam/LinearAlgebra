"""
EXERCISE 2: Plot the parallelogram whose corners are
(1,2), (7, 6), (-3,4) and (3,8)
Now plot the parallelogram obtained by
rotating by 25 degrees around origin.

What is to be done?
Use matplotlib library
Do the plotting of original PRGM
Then the reflected PRGM
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

verts = np.array([[1,2],[-3,4],[3,8],[7,6]])
theta = 25*(math.pi)/180
R25 = np.array([[np.cos(theta), (-1) * np.sin(theta)], [np.sin(theta), np.cos(theta)]])

p = Polygon(verts, facecolor = 'b')
fig,ax = plt.subplots()
ax.add_patch(p)
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
plt.show()

verts2 = []
for i in verts:
    verts2.append(R25 @ i)
print(verts2)

p = Polygon(verts2, facecolor = 'b')
fig,ax = plt.subplots()
ax.add_patch(p)
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
plt.show()