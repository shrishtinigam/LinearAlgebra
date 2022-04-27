"""
LAB EXPT 2
Using Cholesky decomposition get it from NUMPY
then solve
4x +y + 6z + 2w = 18
x + 5/4 y + 7/2 z -1/2 w = 9/2
6x+7/2 y + 53/4 z + 2w = 29
2x -1/2 y + 2z + 22w = 49
manually.
"""

import numpy as np
A = np.array([[4,1,6,2],[1,5/4,7/2,-1/2],[6,7/2,53/4,2],[2,-1/2,2,22]])
B = np.array([[18],[9/2],[29],[49]])
print("A : ", A)
l = np.linalg.cholesky(A)
print("Cholesky Decomposition: ")
print("L = ", l)
u = l.transpose()
ln = np.dot(u,l)
print("u = ", ln)
res = np.linalg.solve(A,B)
print("Result: ", res)