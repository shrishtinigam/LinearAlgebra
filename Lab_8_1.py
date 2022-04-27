"""Visualizing Curves in 2D

Cartesian/Polar
2D
C(t) = (x(t), y(t))
"""

import numpy as np
import matplotlib.pyplot as plt

# CURVES
def f(x):
    return x**2*np.exp(-x**2)

# generate 51 points between 0 and 3
x = np.linspace(start = 0., stop = 3, num = 51)
y = f(x) # applying function over all the values
plt.plot(x, y)

def g(x):
    return x*np.exp(-x)
xx = np.arange  ( start = 0., stop = 3., step = 0.05)
yy = g(xx)
plt.plot( xx, yy, 'r-')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend( [ 'f(x) = x^2*exp(-x^2)'   # This is f(x)
            , 'g(x) = x*exp(-x)'       # This is g(x)
            ] )
plt.title('Multiple Matplotlib curves in a single figure');
plt.show()

# CIRCLES
figure, axes = plt.subplots()
My_circle = plt.Circle(( 0.6 , 0.6 ), 0.2 )
 
axes.set_aspect( 1 )
axes.add_artist( My_circle )
plt.title( 'Circle using inbuilt function' )
plt.show()

# Manually making the equations

# Using Polar Equation of a Circle
theta = np.linspace( 0 , 2 * np.pi , 150 )
radius = 0.4
a = radius * np.cos( theta )
b = radius * np.sin( theta )
figure, axes = plt.subplots( 1 )
axes.plot( a, b )
axes.set_aspect( 1 )
plt.title( 'Circle using Polar Equation' )
plt.show()

x = np.linspace( -0.7 , 0.7 , 150 )
y = np.linspace( -0.7 , 0.7 , 150 )
a, b = np.meshgrid( x , y )
C = a ** 2 + b ** 2 - 0.2
figure, axes = plt.subplots()
axes.contour( a , b , C , [0] )
axes.set_aspect( 1 )
 
plt.title('Circle using Parametric Equation')
plt.show()

# ELLIPSES
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
angle = 45  # degrees)
ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1, color='red')
ax.add_artist(ellipse)
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
plt.title('Ellipse')
plt.show()