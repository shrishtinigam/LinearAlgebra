"""
Lab Expt 4
1. Using Python solve the following problem.
Given u = (1,8,5) determine for which vector v from the following
list, the projection has shortest length:

A = { (2,1,-3), (-3,4,1), (2,3,3), (1,1,5) , (4,0,3) }
"""
import numpy as np
import math
def proj_length(v1, v2): # proj of v1 on v2
    vx = v2*((np.dot(v1,v2))/(np.dot(v2,v2)))
    v = np.dot(vx,vx)
    return math.sqrt(v)

u = [1,8,5]
vectors = [[2,1,-3], [-3,4,1], [2,3,3], [1,1,5] , [4,0,3]]

minimum_proj_length = 99999
index = -1
for i in range(5):
    cur_proj_length = proj_length(np.array(u), np.array(vectors[i]))
    if(cur_proj_length < minimum_proj_length):
        minimum_proj_length = cur_proj_length
        index = i
    print(cur_proj_length)

print(minimum_proj_length)
print(index)

