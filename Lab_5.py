"""
Gram Schmidt
"""
import numpy as np
import math
def proj(v1, v2): # proj of v1 on v2
    return v2*((np.dot(v1,v2))/(np.dot(v2,v2)))
def length(u):
    v = np.dot(u,u)
    return math.sqrt(v)
   
v1 = np.array([2,1,-1])
v2 = np.array([7,5,1])
v3 = np.array([5,12,-2])

u1 = v1
u2 = v2 - proj(v2, u1)
u3 = v3 - proj(v3, u1) - proj(v3, u2)
print(u1,u2,u3)
u1_norm = length(u1)
u2_norm = length(u2)
u3_norm = length(u3)
print(u1/u1_norm,u2/u2_norm,u3/u3_norm)
