"""Page Rank Algo"""
"""
Give rank 1/n to all webpages at first
Create a matrix from the weblinks, called A
Choose a phatic factor p, where 0 < p < 1 --> 0.85
Calculate M, where M = (1-p)A + p/n (1 1 1 ... 1 1 1)
"""

"""
4   2 1 3   3 0 2 3   1 0   1 1
"""

import numpy as np

n = int(input("No. of webpages"))

cols = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(n):
    n1 = int(input(f"No. of links from webpage {i} "))
    for j in range(n1):
        k = int(input(f"Enter the dest weblink {j + 1} "))
        cols[i][k] = 1/n1
A = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(cols[j][i])
    A.append(x)
print("Initial Matrix: ", A)
p = 0.85
ones = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
A = np.array(A)
M = ((1-0.85)*A) + ((p/n)*ones)
print("M matrix: ", M)

val,ver = np.linalg.eig(M)
print("Value:", val)
print("Vector:", ver)

# Find the eig vector with eig value = 1
s = 0
for i in val:
    if(i == 1):
        s = 1
        break
# eigv = ver[:,s]
eigv = []
for i in range(n):
    eigv.append(ver[i][s])

# New ranks
print("Eigen Vector:", eigv)

# Verification
print(np.dot(M,ver))