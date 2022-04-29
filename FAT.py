import numpy as np
from numpy.linalg import LinAlgError
A = np.array([[1,-2,-2],[1,-2,-1],[0,1,1]])
b = np.array([-2,-1,2])

try: 
    X = np.linalg.solve(A, b)
except LinAlgError:
    print("Error")
    
print("Result X: ", X)
print("\n\n")
B = np.array([[-4,8,6],[0,3,0],[-3,4,5]])
val,ver = np.linalg.eig(B)
print("Eigen value: ", val)
print("Eigen Vector: ", ver)
print("\n\n")
ver2 = []
for i in range(len(ver)):
    temp = []
    for j in range(len(ver[0])):
        temp.append(ver[j][i])
    ver2.append(temp)
print(ver2)

# Seaching for eigenvector 
print("\n\n")
for i in range(len(ver2)):
    x = []
    for j in range(len(ver2[0])):
        x.append(ver2[i][j]/X[j])
    if(all(ele == x[0] for ele in x)):
        print(f"Found at {i+1}. Therefore it corresponds to the {i+1} eigenvalue.")
        break
        
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 7*(x**2) + 7*x + 15

x = np.linspace(start = -30, stop = 30, num = 200)
y = f(x) 

plt.plot(x, y)
plt.axis([-30, 30, -30, 30])
plt.show()

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
print("\n\n")

p = 0.85
ones = np.ones((n,n))
A = np.array(A)
M = ((1-0.85)*A) + ((p/n)*ones)
print("M matrix: ", M)
print("\n\n")
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
print("\n\n")
# New ranks
print("Eigen Vector representing new ranks:", eigv)
print("\n\n")
# Verification
print("Verificiation:", np.dot(M,ver)[0][0], "\n\n", np.dot(M,ver))