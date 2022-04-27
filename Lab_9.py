"""
A linear programming problem in two varibales: Maximize Z = 6x + 11y Subject to 
constraints: x+ 2y < 11, 3x+y< 15, 5x +3y < 22, x, y > 0. 
Each constraint is a list of 3 numbers: (x-coeff, y-coeff, rhs) -(1,2, 11), 
(3,1,15), (5,3, 22). 

STEP 1: 
Find all intersection pts 
One intersection point for every pair of constraint. If there are n constraints then 
n(n-1)/2 intersection points. 

STEP 2: 
Ignore points outside the convex region: How? An intersection point (p, q) is to be 
ignored if any constraint ax + by < c is violated at x = p, y = q 
From multiple intersection points on axis keep the ones closest to origin.

STEP 3:

Evaluate Objective function Z = Ax + By at every remaining intersection point. 
Choose the one giving maximal value for Z.
That is the solution.
"""

import numpy as np

def intersection(x1,x2):
    y = (x2[0]*x1[2] - x1[0]*x2[2])/(x2[0]*x1[1] - x1[0]*x2[1])
    x = (x1[2]*x2[1] - x1[1]*x2[2])/(x2[1]*x1[0] - x1[1]*x2[0])
    return [x,y]

def violates(x, p):
    if(x[0]*p[0] + x[1]*p[1] > x[2]):
        return True
    return False

def evaluate(X, Y, p):
    return X*p[0] + Y*p[1]

print("To maximise AX + BY")
X = int(input("Enter value of A: "))
Y = int(input("Enter value of B: "))
n = int(input("Number of constraints: "))
# X contains all the constraints
x = []
for i in range(n):
    print(f"Enter constraints {i+1}: ")
    y = []
    for j in range(3):
        k = int(input())
        y.append(k)
    x.append(y)

intersection_array = []
for i in range(n):
    k = i + 1
    while(k < n):
        intersection_array.append(intersection(x[i], x[k]))
        k += 1

print("Points of Intersection: ", intersection_array)

# ia_final ignores the points which violate any constraints
ia_final = []
for i in range(len(intersection_array)):
    m = 0
    for j in range(len(x)):
        if(violates(x[j],intersection_array[i])):
            break
        else:
            m += 1
    if(m == 3):
        ia_final.append(intersection_array[i])

print("Remaining Points of Intersection: ", ia_final)
 
maximized = -9999999
max_point = []
for i in range(len(ia_final)):
    c = evaluate(X,Y,ia_final[i])
    if(c > maximized):
        maximized = c
        max_point = ia_final[i]

print(f"\n\nMAX: {maximized} at point {max_point}")
