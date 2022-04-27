"""Application of Matrix Multiplication"""

import numpy as np
from numpy.linalg import LinAlgError
A = []
number = int(input("Enter number of food items in given cases: "))
for i in range(number):
    print(f"Enter values {i+1}")
    st = list(map(int,input().split()))
    A.append(st)

B = []
for i in range(number):
    print(f"Enter nutrional target {i+1}")
    st = list(map(int,input().split()))
    B.append(st)

print("Matrix A:", A)
print("Matrix B:", B)
A2 = np.transpose(A)
print("Matrix A transpose", A2)

try: 
    res = np.linalg.solve(A2, B)
    if any(x[0] < 0 for x in res):
        print("Cannot be aceived")
    else:
        print("To achive target")
        print("Result", res)
except LinAlgError:
    print("Cannot Achieve Target")