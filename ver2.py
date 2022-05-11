import numpy as np
from sympy import *
import time

file = input("\nEnter the filename: ")

start = time.time()
arr = []
with open(file) as f:
    for line in f: 
        arr.append([float(x) for x in line.split()])
          
v = int(arr[0][0])
e = int(arr[0][1])
f = int(arr[0][2])
print("\nNumber of vertices:", v)
print("Number of edges:", e)
print("Number of faces:", f)
#---------------------------------------------------------------
cols = e
rows = v
bound_arr1 = [ [0] * int(cols) for i in range(int(rows))]

count = 0
for i in range(1+v, 1+v+e):
    n1 = int(arr[i][0])
    n2 = int(arr[i][1])
    bound_arr1[n2-1][count] = 1
    bound_arr1[n1-1][count] = -1
    count += 1

final = np.array(Matrix(np.array(bound_arr1)).nullspace())

final_arr2 = []

for j in range(len(final)):
    final_arr1 = []
    for i in final[j]:
        final_arr1.append(int(i))
    final_arr2.append(final_arr1)

kerdel1 = np.transpose(final_arr2);
#---------------------------------------------------------------
cols = f
rows = e
bound_arr2 = [ [0] * int(cols) for i in range(int(rows))]

count = 0
for i in range(1+v+e, 1+v+e+f):
    n1 = int(arr[i][0])
    x1 = int(arr[v+n1][0])
    x2 = int(arr[v+n1][1])
    
    n2 = int(arr[i][1])
    y1 = int(arr[v+n2][0])
    y2 = int(arr[v+n2][1])
    
    n3 = int(arr[i][2])
    z1 = int(arr[v+n3][0])
    z2 = int(arr[v+n3][1])
    
    bound_arr2[n1-1][count] = 1
    
    if((x1 == y1) or (x2 == y2)):
        bound_arr2[n2-1][count] = -1
    else:
        bound_arr2[n2-1][count] = 1
    
    if((x1 == z1) or (x2 == z2)):
        bound_arr2[n3-1][count] = -1
    else:
        bound_arr2[n3-1][count] = 1  
    
    count += 1  

del2 = np.array(bound_arr2)

# final3 = np.concatenate((del2,kerdel1),axis=1)

rref = Matrix(del2).rref()
print(rref)

print("Indices of the columns corresponding to the representative 1-cycles = ",rref[1])

end = time.time()
print("\nExecution time:",(end - start), "\n")