"""
LAB EXPT 1
2. Define a 4x4 matrix with first row
arbitrary numbers of your choice. [ Use whole numbers!]
Let S be the sum of the entries in that row.
Now construct other rows arbirarily, but,
having the same number S as the row total.
Verify, for this matrix, that the column vector [1,1,1,1]
is an eigenvector. What is the eigen value?
"""

import numpy as np
A = np.array([[1,0,1,6],[0,2,2,4],[1,4,3,0],[0,1,0,7]])
print("A: ", A)
v = np.array([1,1,1,1])
res = np.dot(A,v)
print("\nResult: ", res)
r = res/v
print("Eigen value : ", r)