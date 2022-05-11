import numpy as np
from sympy import *
import time

file = input("\nEnter the file to be scanned: ")
strt_time = time.time()
vec = []
with open(file) as input_file:
    for line in input_file: 
        vec.append([float(x) for x in line.split()])
vert = int(vec[0][0])
edj = int(vec[0][1])
fcs = int(vec[0][2])
print("\nNumber of vertices in the file: ", vert)
print("Number of edges in the file: ", edj)
print("Number of faces: in the file: ", fcs)

# Calculating del1

colmns = edj
n_rows = vert
boundary_mat1 = [[0]*int(colmns) for i in range(int(n_rows))]
res = 0
for i in range(1+vert, 1+vert+edj):
    x = int(vec[i][0])
    y = int(vec[i][1])
    boundary_mat1[x-1][res] = -1
    boundary_mat1[y-1][res] = 1
    res += 1
last = np.array(Matrix(np.array(boundary_mat1)).nullspace())
final2 = []
for j in range(len(last)):
    final1 = []
    for i in last[j]:
        final1.append(int(i))
    final2.append(final1)
ker_del1 = np.transpose(final2);


# Calculating del2

colmns = fcs
n_rows = edj
bound_vec2 = [ [0] * int(colmns) for i in range(int(n_rows))]
res = 0
for i in range(1+vert+edj, 1+vert+edj+fcs):
    x = int(vec[i][0])
    a = int(vec[vert+x][0])
    b = int(vec[vert+x][1])
    
    y = int(vec[i][1])
    c = int(vec[vert+y][0])
    d = int(vec[vert+y][1])
    
    z = int(vec[i][2])
    e = int(vec[vert+z][0])
    f = int(vec[vert+z][1])
    bound_vec2[x-1][res] = 1
    if((a == e) or (b == f)):
        bound_vec2[z-1][res] = -1
    else:
        bound_vec2[z-1][res] = 1 
    if((a == c) or (b == d)):
        bound_vec2[y-1][res] = -1
    else:
        bound_vec2[y-1][res] = 1
    res += 1  

calc_del2 = np.array(bound_vec2)
final3 = np.concatenate((calc_del2,ker_del1),axis=1)
mtrx_rref = Matrix(final3).rref()
print(mtrx_rref)

rep1Cycle = []
for x in mtrx_rref[1]:
    if(x > fcs-1):
        rep1Cycle.append(x-fcs + 1)
print("1 Homology Group = ",rep1Cycle)
end = time.time()
print("\nExecution time:",(end - strt_time), "\n")