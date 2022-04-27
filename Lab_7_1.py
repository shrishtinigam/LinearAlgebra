import numpy as np
pages = [
    '1 2 3',
    '3',
    '0 1',
    '0'
]
P = 0.85
def getlinks(stri):
    return list(map(int, stri.split()))

PR = [1/4 for i in range(len(pages))]
scoremat = [[0 for i in range(len(pages))] for j in range(len(pages))]
for i in range(len(pages)):
    links = getlinks(pages[i])
    for j in links:
        scoremat[j][i] = PR[i]/len(links)

print("Scoremat", scoremat)
PR = (1-P)/len(pages)+ P*np.array(scoremat)
print("PR:", PR) 

ones = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])

def near(a, b, rtol = 10((-5)), atol = 10^(-8)):
    return np.abs(a-b) < (atol+rtol*np.abs(b))

D, V = np.linalg.eig(PR)
print("\n\nD", D)
print("V:", V)
print("Ranks: ", np.real(V[near(D,ones)]))