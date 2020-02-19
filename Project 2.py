# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:26:43 2019

@author: hugo.halgreen
"""
# Armand Halgreen ah302

import numpy as np
import matplotlib.pyplot as plt


# Question 1

a=-1.0
b=2.0

n=6

# x values
x=[]
for i in xrange(n+1):
    x.append(((b-a)/(n))*i+a)

# function for f(x)
def f(x):
    f=(1.0-((x)**3.0))*np.sin(2.0*(np.pi)*x)
    return f

# y values
y=[]
for i in xrange(n+1):
    y.append(f(x[i]))

# Construct linear system
X=[[0]*(n+1) for i in xrange(n+1)]

for i in xrange(n+1):
    for j in xrange(n+1):
        X[i][j]=(x[i])**(n-j)

# Solve system of equations
Y=np.array(y)
X=np.array(X)
solution1=np.linalg.solve(X,Y)

def f1(x):
    f1=0
    for i in xrange(n+1):
        f1=(x**(i))*solution1[i]+f1
    return f1

# x values
x=[]
for i in xrange(12+1):
    x.append(((b-a)/(12))*i+a)

# y values
y1=[]
for i in xrange(12+1):
    y1.append(f1(x[i]))

maxi =0
for k in xrange(n+1):
    if abs(f(x[k])-y1[k])>maxi:
        maxi=abs(f(x[k])-y1[k])
print 'max error for Q1 part 2 n=6 is',maxi        
print 'red is n=6, blue is n=12'       








n=12

# x values
x=[]
for i in xrange(n+1):
    x.append(((b-a)/(n))*i+a)

# x values
x=[]
for i in xrange(n+1):
    x.append(((b-a)/(n))*i+a)

# y values
y=[]
for i in xrange(n+1):
    y.append(f(x[i]))

# Construct linear system
X=[[0]*(n+1) for i in xrange(n+1)]

for i in xrange(n+1):
    for j in xrange(n+1):
        X[i][j]=(x[i])**(n-j)

# Solve system of equations
Y=np.array(y)
X=np.array(X)
solution1=np.linalg.solve(X,Y)

def f2(x):
    f2=0
    for i in xrange(n+1):
        f2=(x**(i))*solution1[i]+f2
    return f2

# x values
x=[]
for i in xrange(n+1):
    x.append(((b-a)/(n))*i+a)


# y values
y2=[]
for i in xrange(n+1):
    y2.append(f2(x[i]))

maxi =0
for k in xrange(n+1):
    if abs(f(x[k])-y2[k])>maxi:
        maxi=abs(f(x[k])-y2[k])
print 'max error for Q1 part 2 n=12 is',maxi        
print 'red is n=6, blue is n=12'       

plt.plot(x, y1, 'r') 
plt.plot(x, y2, 'b') 
plt.show()


print x
#print 'hi', (f(x[11])













# Question 1 part 2

n=6
a=-1.0
b=2.0

xck=[]
xk=[]
fxk=[]

for k in xrange(n+1):
    xck.append(np.cos((2.0*k+1.0)*((np.pi)/(2.0*(n+1.0)))))
    xk.append(0.5*(a+b)+0.5*(b-a)*xck[k])
    fxk.append(f(xk[k]))

# x values
x=xk

# y values
y=fxk

# Construct linear system
X=[[0]*(n+1) for i in xrange(n+1)]

for i in xrange(n+1):
    for j in xrange(n+1):
        X[i][j]=(x[i])**(n-j)

# Solve system of equations
Y=np.array(y)
X=np.array(X)
solution1=np.linalg.solve(X,Y)

def f1(x):
    f1=0
    for i in xrange(n+1):
        f1=(x**(i))*solution1[i]+f1
    return f1

# x values
x=[]
for i in xrange(12+1):
    x.append(((b-a)/(12))*i+a)

# y values
y1=[]
for i in xrange(12+1):
    y1.append(f1(x[i]))


maxi =0
for k in xrange(n+1):
    if abs(f(x[k])-y1[k])>maxi:
        maxi=abs(f(x[k])-y1[k])
print 'max error for Q1 part 2 n=6 is',maxi        
print 'red is n=6, blue is n=12'       
  







n=12
a=-1.0
b=2.0
xck1=[]
xk1=[]
fxk1=[]
for k in xrange(n+1):
    xck1.append(np.cos((2.0*k+1.0)*((np.pi)/(2.0*(n+1.0)))))
    xk1.append(0.5*(a+b)+0.5*(b-a)*xck1[k])
    fxk1.append(f(xk1[k]))


# x values
x=xk1

# y values
y=fxk1

# Construct linear system
X=[[0]*(n+1) for i in xrange(n+1)]

for i in xrange(n+1):
    for j in xrange(n+1):
        X[i][j]=(x[i])**(n-j)

# Solve system of equations
Y=np.array(y)
X=np.array(X)
solution1=np.linalg.solve(X,Y)

def f2(x):
    f2=0
    for i in xrange(n+1):
        f2=(x**(i))*solution1[i]+f2
    return f2

# x values
x=[]
for i in xrange(12+1):
    x.append(((b-a)/(12))*i+a)

# y values
y2=[]
for i in xrange(12+1):
    y2.append(f2(x[i]))

maxi =0
for k in xrange(n+1):
    if abs(f(x[k])-y2[k])>maxi:
        maxi=abs(f(x[k])-y2[k])
print 'max error for Q1 part 2 n=12 is',maxi        
print 'red is n=6, blue is n=12'       
  
plt.plot(x, y1, 'r') 
plt.plot(x, y2, 'b') 
plt.show()




















 
# Question 1 part 3

n=6
a=-1.0
b=2.0
h=(b-a)/n
B=[]
xk=[]
for k in xrange(n+1):
    x=a+k*h
    xk.append(a+k*h)
    if x-a <= -2.0*h:
        B.append(0)
    elif x-a > -2.0*h and x-a <= -h:
        B.append((1.0/6.0)*(2.0*h+(x-a))**3)
    elif x-a > -h and x-a <= 0:
        B.append(2.0*(h**3)/3.0-(1.0/2.0)*((x-a)**2)*(2.0*h-(x-a)))
    elif x-a > 0 and x-a <= h:
        B.append(2.0*(h**3)/3-(1.0/2.0)*((x-a)**2)*(2.0*h+(x-a)))
    elif x-a > h and x-a <= 2.0*h:
        B.append((1.0/6.0)*(2.0*h-(x-a))**3) 
    else:
        B.append(0)

maxi =0
for k in xrange(n+1):
    if abs(f(xk[k])-B[k])>maxi:
        maxi=abs(f(xk[k])-B[k])
print 'max error for Q1 part 3 n=6 is',maxi        
print 'red is n=6, blue is n=12'       
  









n=12
a=-1.0
b=2.0
h=(b-a)/n
B1=[]
xk1=[]
for k in xrange(n+1):
    x=a+k*h
    xk1.append(a+k*h)
    if x-a <= -2.0*h:
        B1.append(0)
    elif x-a > -2.0*h and x-a <= -h:
        B1.append((1.0/6.0)*(2.0*h+(x-a))**3)
    elif x-a > -h and x-a <= 0:
        B1.append(2.0*(h**3)/3.0-(1.0/2.0)*((x-a)**2)*(2.0*h-(x-a)))
    elif x-a > 0 and x-a <= h:
        B1.append(2.0*(h**3)/3-(1.0/2.0)*((x-a)**2)*(2.0*h+(x-a)))
    elif x-a > h and x-a <= 2.0*h:
        B1.append((1.0/6.0)*(2.0*h-(x-a))**3) 
    else:
        B1.append(0)


maxi =0
for k in xrange(n+1):
    if abs(f(xk1[k])-B1[k])>maxi:
        maxi=abs(f(xk1[k])-B1[k])
print 'max error for Q1 part 3 n=12 is',maxi        
print 'red is n=6, blue is n=12'       
   

plt.plot(xk, B, 'r') 
plt.plot(xk1, B1, 'b') 
plt.show()












# Question 2
x=[1841,1851,1861,1871,1881,1891,1901,1911,1926,1936]
y=[8.53,5.11,4.4,4.05,3.87,3.47,3.22,3.14,2.97,2.97]


n=len(x)

# Construct linear system
X=[[0]*(n+1) for i in xrange(n+1)]

for i in xrange(n+1):
    for j in xrange(n+1):
        X[i][j]=(x[i])**(n-j)

# Solve system of equations
Y=np.array(y)
X=np.array(X)
solution1=np.linalg.solve(X,Y)

def f2(x):
    f2=0
    for i in xrange(n+1):
        f2=(x**(i))*solution1[i]+f2
    return f2

# x values
x=[]
for i in xrange(n+1):
    x.append(((b-a)/(n))*i+a)


# y values
y2=[]
for i in xrange(n+1):
    y2.append(f2(x[i]))


plt.plot(x, y1, 'r') 
plt.plot(x, y2, 'b') 
plt.show()


