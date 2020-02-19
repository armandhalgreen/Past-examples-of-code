# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:57:42 2019

@author: hugo.halgreen
"""
#Project1 ah302

# Jacobi iterative method

# Write out A
A=[[10,7,1,3,4,2],[1,8,0,1,5,3],[2,1,9,5,1,1],[1,2,1,14,0,1],[0,1,2,1,9,0],[1,5,1,2,1,7]]

# Create a matrix for D and fill it with zeros
D=[[0]*len(A) for i in xrange(len(A))]

# Replace all the non diagonal entries in A with zeros and call this matrix D
for i in xrange(len(A)):
    for j in xrange(len(A[1])):
        if i==j:
            D[i][j]=A[i][j]
        elif i!=j:
            D[i][j]=0
            
# Create a matrix for D_inverse and fill it with zeros
D_inverse=[[0]*len(A) for i in xrange(len(A))]
     
# Calculate D_inverse
for i in xrange(len(A)):
    for j in xrange(len(A[1])):
         if i==j:
            D_inverse[i][j]=1.0/D[i][j]
         elif i!=j:
            D_inverse[i][j]=0

# Create a matrix for L_plus_U and fill it with zeros
L_plus_U=[[0]*len(A) for i in xrange(len(A))]

# Replace zeros by value when you subtract D-A for each ij
for i in xrange(len(A)):
    for j in xrange(len(A[1])):
        L_plus_U[i][j]=D[i][j]-A[i][j]

# Create a matrix for D_inverse_L_plus_U and fill it with zeros
D_inverse_L_plus_U=[[0]*len(A) for i in xrange(len(A))]

# Calculate D_inverse times (L_plus_U)
for i in xrange(len(A)):
    for j in xrange(len(A[1])):
        total=0
        for k in xrange(len(A[1])):
            x1=(D_inverse[i][k])*(L_plus_U[k][j])
            total=total+x1
            if k==len(A[1])-1:
                D_inverse_L_plus_U[i][j]=total

# Calculate matrix norm sub-ordinate to the infinity
Dk=0
for i in xrange(len(A)):
    for j in xrange(len(A[1])):
        if abs(D_inverse_L_plus_U[i][j])>Dk:
            matrix_norm_sub_ordinate=abs(D_inverse_L_plus_U[i][j])
            Dk=abs(D_inverse_L_plus_U[i][j])
if Dk<1:
  print 'Converges'  
            
# Create a vector for b
b=[14,31,12,-13,26,21] 

# Create a matrix for xk and fill it with ones as a estimate 
xk=[1 for i in xrange(len(A))]

# Create a matrix for xk1 and fill it with zeros
xk1=[0 for i in xrange(len(A))]

# Calculate D_inverse times (L_plus_U)
for k in xrange(30):
    for i in xrange(len(A)):
        total=0
        for j in xrange(len(A[1])):
                x1=(D_inverse_L_plus_U[i][j])*(xk[j])+(D_inverse[i][j])*(b[j])
                total=total+x1
        xk[i]=total
        xk1[i]=total
print xk1

c=[0 for i in xrange(len(A))]

for i in xrange(len(A)):
    total=0
    for j in xrange(len(A[1])):
        x1=(A[i][j])*(xk1[j])
        total=total+x1
    c[i]=total
print c

# Create a vector for b
b=[14,31,12,-13,26,21] 


