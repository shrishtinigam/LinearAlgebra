"""
Lab expt 3
EXERCISE 1: Plot the parallelogram for which THREE of the corners are
(0,0), (5, 3), and (2,9)
Now plot the parallelogram obtained by
reflecting wrt the line y = 5x.
https://math.stackexchange.com/questions/1138134/what-is-the-matrix-used-to-find-the-reflected-x-y-coordinate-in-the-line-y-mx
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math


# To find the 4th point of a parallelogram
p1 = [0,0]
p2 = [5,3]
p3 = [2,9]
p4 = []
p4.append(p1[0] + (p3[0] - p2[0]))
p4.append(p1[1] + (p3[1] - p2[1]))
verts =  np.array([p1,p2,p3,p4])

p = Polygon(verts, facecolor = 'b')
fig,ax = plt.subplots()
ax.add_patch(p)
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
plt.show()

T = np.array([[-12/3,5/13],[5/13,12/13]]) # Transformation matrix
verts2 = []
for i in verts:
    verts2.append(T @ i)
print(verts2)

p = Polygon(verts2, facecolor = 'b')
fig,ax = plt.subplots()
ax.add_patch(p)
ax.set_xlim([-20,18])
ax.set_ylim([-10,10])
plt.show()

