"""Page Rank Algo FINAL CORRECT"""
"""
Give rank 1/n to all webpages at first
Create a matrix from the weblinks, called A
Choose a phatic factor p, where 0 < p < 1 --> 0.85
Calculate M, where M = (1-p)A + p/n (1 1 1 ... 1 1 1)
"""

"""
4   2 1 3   3 0 2 3   1 0   1 1
5   3 1 2 4   2 0 2   1 4   3 1 2 4    2 1 3
"""
import numpy as np

n = int(input("No. of webpages"))

cols = [[0 for i in range(n)] for j in range(n)]

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
ones = np.ones((n,n))
A = np.array(A)
M = ((1-0.85)*A) + ((p/n)*ones)
print("M matrix: ", M)

val,vec = np.linalg.eig(M)
ind = -1
for i in range(len(val)):
    x = round(val[i].real, 3)
    if(x == 1):
        ind = i
v = []
vec = vec.tolist()
for i in range(len(vec)):
    v.append(vec[i][ind])
v = np.array(v)
mv = np.matmul(M,v)
mv = mv.tolist()
mv = np.array(mv)[0]
print("Eigen vector: ",v)
print("\nM x v", mv)