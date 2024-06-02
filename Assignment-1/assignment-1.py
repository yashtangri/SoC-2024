import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import math 

n = input(int)
m = input(int)
# n should be greater than m. 

c = []
for i in range(0,3):
    element = int(input("Enter the elements for vector c: "))
    c.append(element)

b = []
for i in range(0,2):
    element = int(input("enter the elements for vector b:"))
    b.append(element)

A = []
for i in range(0,2):
    row=[]
    for j in range(3):
        element = int(input("Enter the elements for matrix A: "))
        row.append(element)
    print("start new row")
    A.append(row)
c = np.array(c)
b = np.array(b)
A = np.array(A)
def simplex(c,A,b):
    #n is the number of variables 
    #m is the number of constraints
    n=3
    m=2
    #this is the initial Table
    table = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    coeff = np.hstack([(-1)*c, np.zeros(m+1)])
    table = np.vstack([coeff,table])

    basis_var = list(range(3,5))

    while True:
        if np.all(table[0:-1]>=0):
            break
        
        pivot_col = np.argmin(table[0,:-1])
         
        ratios = np.divide(table[:-1, -1], table[:-1, pivot_col], out=np.full_like(table[:-1, -1], np.inf), where=table[:-1, pivot_col] > 0)
        pivot_row = np.argmin(ratios)

        pivot_val = table[pivot_row, pivot_col]
        table[pivot_row] /= pivot_val
        for i in range(len(table)):
            if i != pivot_row:
                table[i] -= table[i, pivot_col] * table[pivot_row]

        basis_var[pivot_row] = pivot_col

    x = np.zeros(n)
    for i in range(m):
        if basis_var[i] < n:
            x[basis_var[i]] = table[i, -1]

    return x , table
print(simplex(c,A,b))