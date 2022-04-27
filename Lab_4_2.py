"""
2.
Given 3 vectors v1, v2 and v3
A = { (2,1,-3), (-3,4,1), (2,3,3)}
Do these vectors form a basis for 3d-space?
"""
import numpy as np
v = [[2,1,-3], [-3,4,1], [2,3,3]]
# Span
span = False
## Coefficient Matrix
M = []
for i in range(3):
    x = []
    for j in range(3):
        x.append(v[j][i])
    M.append(x)
print(M)
M2 = np.array(M)
det_val = np.linalg.det(M2)

if(det_val != 0):
    print("A Spans R")
    span = True

# Linear Independence

res = np.linalg.solve(M, [0,0,0])
print(res)
linindep = True
for i in res:
    if i != 0:
        False
        break

if(linindep):
    print("A is Linearly independent")

if(linindep and span):
    print("Yes A is a basis as it is linearly independent and spans R3")

