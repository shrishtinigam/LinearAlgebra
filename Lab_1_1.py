"""
LAB EXPT 1
1. Find eigen values and eigen vectors through commands and through
aided computation
[-18 -15 35]
[ -5 -8 15]
[-15 -15 32]
"""
import numpy as np
A = np.array([[-18,-15,35],[-5,-8,15],[-15,-15,32]])
# val, ver = np.array(A)
val,ver = np.linalg.eig(A)
print("Eigen value: ", val)
print("Eigen Vector: ", ver)

ax = np.dot(A, ver[:,0])
lx = val[0] * ver[:,0]
print("\n value of A * x : ", ax, "\n value of lambda", lx)